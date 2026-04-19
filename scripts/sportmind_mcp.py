#!/usr/bin/env python3
"""
SportMind MCP Server v3.34
Exposes SportMind intelligence as MCP tools for Claude and other AI agents.

Ten tools:
  --- Original five ---
  sportmind_signal          — pre-match intelligence signal
  sportmind_macro           — current macro state
  sportmind_stack           — full skill stack for a sport
  sportmind_verify          — skill integrity verification
  sportmind_agent_status    — autonomous agent health check

  --- New five (v3.34) ---
  sportmind_pre_match       — orchestrated full pre-match reasoning package
  sportmind_disciplinary    — disciplinary check: DSM level, flags, commercial modifier
  sportmind_fan_token_lookup — resolve club/ticker/sport to fan token context
  sportmind_sentiment_snapshot — multi-axis sentiment state for a token
  sportmind_verifiable_source  — authoritative source for a query type and sport

Usage:
  python scripts/sportmind_mcp.py              # stdio (Claude Desktop / Claude Code)
  python scripts/sportmind_mcp.py --http       # HTTP/SSE on port 3001 (remote agents)
  python scripts/sportmind_mcp.py --http --port 8080

Install:
  pip install mcp aiohttp

See MCP-SERVER.md for full deployment guide.
See platform/sportmind-mcp-server.md for specification.
"""

import json
import hashlib
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT        = Path(__file__).parent.parent
HASHES_FILE = ROOT / "platform" / "skill-hashes.json"
MACRO_STATE = ROOT / "platform" / "macro-state.json"

VERSION = "3.86.4"

SUPPORTED_SPORTS = [
    "football", "basketball", "cricket", "mma", "formula1", "tennis",
    "rugby", "rugby_league", "afl", "baseball", "ice_hockey", "motogp",
    "nascar", "kabaddi", "netball", "handball", "esports",
    "darts", "snooker", "swimming", "athletics", "winter_sports",
    "boxing", "cycling", "horse_racing",
]

USE_CASES = [
    "pre_match", "fan_token_tier1", "fan_token_tier2",
    "prediction_market", "commercial_brief", "governance",
]

# ── Fan token registry (Chiliz Chain, verified contract addresses) ─────────────
# Source: chiliscan.com/token/top-erc20 · Chain ID 88888
# Excludes PEPPER (not a sports fan token)
FAN_TOKEN_REGISTRY = {
    # ══════════════════════════════════════════════════════════════════════════
    # ACTIVE SOCIOS/CHILIZ PARTNERSHIPS (expired=False)
    # Source: fantokens.com, contracts verified on-chain via chiliscan.com
    # The blockchain address is the canonical identifier for each token.
    # Tokens trade on multiple CEXs and DEXs globally — use chiliscan.com
    # or the fantokens.com trade page for current market data.
    # ══════════════════════════════════════════════════════════════════════════

    # ── Football: Top European clubs ─────────────────────────────────────────
    "BAR":     {"name": "FC Barcelona",                         "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xFD3C73b3B09D418841dd6Aff341b2d6e3abA433b",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xFD3C73b3B09D418841dd6Aff341b2d6e3abA433b",
                "fantokens": "https://www.fantokens.com/trade/fc-barcelona-fan-token"},
    "AFC":     {"name": "Arsenal FC",                           "sport": "football",   "tier": 1, "expired": False,
                "contract": "0x1d4343d35f0E0e14C14115876D01dEAa4792550b",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x1d4343d35f0E0e14C14115876D01dEAa4792550b",
                "fantokens": "https://www.fantokens.com/trade/arsenal-fan-token",
                "fan_token_play": "PATH_2", "ftp_confirmed_date": "2026-04-07",
                "ftp_note": "First public PATH_2 trial. Pre-liquidation 1/400th supply T-48h."},
    "GAL":     {"name": "Galatasaray S.K.",                     "sport": "football",   "tier": 1, "expired": False,
                "contract": "0x6DaB8Fe8e5d425F2Eb063aAe58540aA04e273E0d",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x6DaB8Fe8e5d425F2Eb063aAe58540aA04e273E0d",
                "fantokens": "https://www.fantokens.com/trade/galatasaray-fan-token"},
    "PSG":     {"name": "Paris Saint-Germain",                  "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xc2661815C69c2B3924D3dd0c2C1358A1E38A3105",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xc2661815C69c2B3924D3dd0c2C1358A1E38A3105",
                "fantokens": "https://www.fantokens.com/trade/paris-saint-germain-fan-token"},
    "ASR":     {"name": "AS Roma",                              "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xa6610b3361c4c0D206Aa3364cd985016c2d89386",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xa6610b3361c4c0D206Aa3364cd985016c2d89386",
                "fantokens": "https://www.fantokens.com/trade/as-roma-fan-token"},
    "CITY":    {"name": "Manchester City FC",                   "sport": "football",   "tier": 1, "expired": False,
                "contract": "0x6401b29F40a02578Ae44241560625232A01B3F79",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x6401b29F40a02578Ae44241560625232A01B3F79",
                "fantokens": "https://www.fantokens.com/trade/manchester-city-fan-token"},
    "ATM":     {"name": "Atletico de Madrid",                   "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xe9506F70be469d2369803Ccf41823713BAFe8154",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xe9506F70be469d2369803Ccf41823713BAFe8154",
                "fantokens": "https://www.fantokens.com/trade/atletico-de-madrid-fan-token"},
    "JUV":     {"name": "Juventus",                             "sport": "football",   "tier": 1, "expired": False,
                "contract": "0x454038003a93cf44766aF352F74bad6B745616D0",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x454038003a93cf44766aF352F74bad6B745616D0",
                "fantokens": "https://www.fantokens.com/trade/juventus-fan-token"},
    "ACM":     {"name": "AC Milan",                             "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xF9C0F80a6c67b1B39bdDF00ecD57f2533ef5b688",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xF9C0F80a6c67b1B39bdDF00ecD57f2533ef5b688",
                "fantokens": "https://www.fantokens.com/trade/ac-milan-fan-token"},
    "INTER":   {"name": "Inter Milan",                          "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xc727c9C0f2647CB90B0FCA64d8ddB14878716BeD",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xc727c9C0f2647CB90B0FCA64d8ddB14878716BeD",
                "fantokens": "https://www.fantokens.com/trade/inter-milan-fan-token"},
    "NAP":     {"name": "Napoli FC",                            "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xbE7f1eBB1Fd6246844E093B04991ae0e66D12C77",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xbE7f1eBB1Fd6246844E093B04991ae0e66D12C77",
                "fantokens": "https://www.fantokens.com/trade/napoli"},
    "ASM":     {"name": "AS Monaco",                            "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x371863096CF5685cD37AE00C28DE10b6edBab3Fe",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x371863096CF5685cD37AE00C28DE10b6edBab3Fe",
                "fantokens": "https://www.fantokens.com/trade/as-monaco-fan-token"},
    "BENFICA": {"name": "SL Benfica",                           "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xad7c869F357B57BB03050183d1BA8eC465CD69Dc",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xad7c869F357B57BB03050183d1BA8eC465CD69Dc",
                "fantokens": "https://www.fantokens.com/trade/sl-benfica-fan-token"},
    "SEVILLA": {"name": "Sevilla FC",                           "sport": "football",   "tier": 1, "expired": False,
                "contract": "0x60a5E1f5f0071C5d870bB0A80B411BDe908AD51e",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x60a5E1f5f0071C5d870bB0A80B411BDe908AD51e",
                "fantokens": "https://www.fantokens.com/trade/sevilla-fan-token"},
    "VCF":     {"name": "Valencia CF",                          "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xba0c26485b1909f80476067272d74A99Cc0E1D57",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xba0c26485b1909f80476067272d74A99Cc0E1D57",
                "fantokens": "https://www.fantokens.com/trade/valencia-fan-token"},
    "RSO":     {"name": "Real Sociedad",                        "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xdd03a533d6a309aFFF3053FE9Fc6C197324597bb",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xdd03a533d6a309aFFF3053FE9Fc6C197324597bb",
                "fantokens": "https://www.fantokens.com/trade/real-sociedad-fan-token"},
    "BFC":     {"name": "Bologna FC",                           "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x319067E6253FdbF183C27AbcAF31d45aD50E98fF",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x319067E6253FdbF183C27AbcAF31d45aD50E98fF",
                "fantokens": "https://www.fantokens.com/trade/bologna-fan-token"},
    "UDI":     {"name": "Udinese Calcio",                       "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xd2571bb5E84F1a3ac643b6be1dD94fC9fb97041d",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xd2571bb5E84F1a3ac643b6be1dD94fC9fb97041d",
                "fantokens": "https://www.fantokens.com/trade/udinese-fan-token"},

    # ── Football: Premier League ─────────────────────────────────────────────
    "SPURS":   {"name": "Tottenham Hotspur",                    "sport": "football",   "tier": 1, "expired": False,
                "contract": "0x93D84Ff2c5F5a5A3D7291B11aF97679E75eEAc92",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x93D84Ff2c5F5a5A3D7291B11aF97679E75eEAc92",
                "fantokens": "https://www.fantokens.com/trade/tottenham-hotspur-fan-token"},
    "AVL":     {"name": "Aston Villa",                          "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x095726841DC9Bf395114Ac83f8fd42B176cFAd10",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x095726841DC9Bf395114Ac83f8fd42B176cFAd10",
                "fantokens": "https://www.fantokens.com/trade/aston-villa-fan-token"},
    "EFC":     {"name": "Everton",                              "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xaBEE61f8fF0eADd8D4ee87092792aAF2D9B2CA8e",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xaBEE61f8fF0eADd8D4ee87092792aAF2D9B2CA8e",
                "fantokens": "https://www.fantokens.com/trade/everton-fc-fan-token"},
    "CPFC":    {"name": "Crystal Palace FC",                    "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xA70bD29Bef2936765Fe33b0f4b0Cf8E947D75581",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xA70bD29Bef2936765Fe33b0f4b0Cf8E947D75581",
                "fantokens": "https://www.fantokens.com/trade/crystal-palace-fan-token"},
    "LUFC":    {"name": "Leeds United",                         "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xF67A8a4299f7EBF0c58DbFb38941D0867f300C30",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xF67A8a4299f7EBF0c58DbFb38941D0867f300C30",
                "fantokens": "https://www.fantokens.com/trade/leeds-united-fan-token"},

    # ── Football: National Teams ─────────────────────────────────────────────
    "ARG":     {"name": "Argentina National Team",              "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xd34625c1c812439229EF53e06f22053249D011f5",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xd34625c1c812439229EF53e06f22053249D011f5",
                "fantokens": "https://www.fantokens.com/trade/argentina-fan-token",
                "wc2026": True},
    "POR":     {"name": "Portugal National Team",               "sport": "football",   "tier": 1, "expired": False,
                "contract": "0xFFAD7930B474D45933C93b83A2802204b8787129",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xFFAD7930B474D45933C93b83A2802204b8787129",
                "fantokens": "https://www.fantokens.com/trade/portugal-national-team-fan-token",
                "wc2026": True},
    "ITA":     {"name": "Italy National Team",                  "sport": "football",   "tier": 1, "expired": False,
                "contract": "0x7483263CA24BFcfF716a21F4a9bbF2610BDD9Ec9",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x7483263CA24BFcfF716a21F4a9bbF2610BDD9Ec9",
                "fantokens": "https://www.fantokens.com/trade/italy-national-team-fan-token",
                "wc2026": True},

    # ── Football: Turkish clubs ──────────────────────────────────────────────
    "TRA":     {"name": "Trabzonspor",                          "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x304193f18f3B34647ae1f549fc825A7e50267c51",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x304193f18f3B34647ae1f549fc825A7e50267c51",
                "fantokens": "https://www.fantokens.com/trade/trabzonspor-fan-token"},
    "GOZ":     {"name": "Goztepe S.K.",                         "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x0E469D1C78421C7952E4D9626800DAd22F45361D",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x0E469D1C78421C7952E4D9626800DAd22F45361D",
                "fantokens": "https://www.fantokens.com/trade/goztepe-s-k-fan-token"},
    "ALA":     {"name": "Aytemiz Alanyaspor",                   "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x863f7537B38130F01a42E9e9406573B1F1e309F7",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x863f7537B38130F01a42E9e9406573B1F1e309F7",
                "fantokens": "https://www.fantokens.com/trade/alanyaspor-fan-token"},
    "IBFK":    {"name": "Istanbul Basaksehir",                  "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xd5FebD04baDd83e7ED56Ca093fD57655b737cd3e",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xd5FebD04baDd83e7ED56Ca093fD57655b737cd3e",
                "fantokens": "https://www.fantokens.com/trade/istanbul-basaksehir-fan-token"},
    "SAM":     {"name": "Samsunspor",                           "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xfC21C38f4802Ab29Aed8cc7367542A0955CfA9D7",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xfC21C38f4802Ab29Aed8cc7367542A0955CfA9D7",
                "fantokens": "https://www.fantokens.com/trade/samsunspor-fan-token"},
    "GFK":     {"name": "Gaziantep F.K.",                       "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x2a5DbF10A9EB8d948AEF256FDE8e62F811624C4F",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x2a5DbF10A9EB8d948AEF256FDE8e62F811624C4F",
                "fantokens": "https://www.fantokens.com/trade/gaziantep-fan-token"},

    # ── Football: Brazilian clubs ─────────────────────────────────────────────
    "MENGO":   {"name": "Flamengo",                             "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xD1723Eb9e7C6eE7c7e2d421B2758dc0f2166eDDc",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xD1723Eb9e7C6eE7c7e2d421B2758dc0f2166eDDc",
                "fantokens": "https://www.fantokens.com/trade/flamengo-fan-token"},
    "FLU":     {"name": "Fluminense FC",                        "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x86930777d43605C40bA786F7802778ff5413eFaB",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x86930777d43605C40bA786F7802778ff5413eFaB",
                "fantokens": "https://www.fantokens.com/trade/fluminense-fan-token"},
    "SCCP":    {"name": "SC Corinthians",                       "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x20BFeab58f8bE903753d037Ba7e307fc77c97388",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x20BFeab58f8bE903753d037Ba7e307fc77c97388",
                "fantokens": "https://www.fantokens.com/trade/sc-corinthians-fan-token"},
    "VERDAO":  {"name": "SE Palmeiras",                         "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x971364Ec452958d4D65Ba8D508FAa226d7117279",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x971364Ec452958d4D65Ba8D508FAa226d7117279",
                "fantokens": "https://www.fantokens.com/trade/se-palmeiras-fan-token"},
    "GALO":    {"name": "Clube Atletico Mineiro",               "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xe5274Eb169E0e3A60B9dC343F02BA940958e8683",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xe5274Eb169E0e3A60B9dC343F02BA940958e8683",
                "fantokens": "https://www.fantokens.com/trade/atletico-mineiro-fan-token"},
    "SPFC":    {"name": "Sao Paulo FC",                         "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x540165b9dFdDE31658F9BA0Ca5504EdA448BFfd0",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x540165b9dFdDE31658F9BA0Ca5504EdA448BFfd0",
                "fantokens": "https://www.fantokens.com/trade/sao-paulo-fc-fan-token"},
    "SACI":    {"name": "Sport Club Internacional",             "sport": "football",   "tier": 2, "expired": False,
                "contract": "0x3175e779b42D35e2C9EeafadCf5B6E6ec6E4f910",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x3175e779b42D35e2C9EeafadCf5B6E6ec6E4f910",
                "fantokens": "https://www.fantokens.com/trade/internacional-fan-token"},
    "BAHIA":   {"name": "Esporte Clube Bahia",                  "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xE92e152fC0ff1368739670a5175175154Ceeef42",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xE92e152fC0ff1368739670a5175175154Ceeef42",
                "fantokens": "https://www.fantokens.com/trade/bahia-fan-token"},

    # ── Football: Americas (other) ───────────────────────────────────────────
    "TIGRES":  {"name": "Club Tigres UANL",                     "sport": "football",   "tier": 2, "expired": False,
                "contract": "0xf17b1E028537ABa705433f7ceBdca881B5c5B79E",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xf17b1E028537ABa705433f7ceBdca881B5c5B79E",
                "fantokens": "https://www.fantokens.com/trade/tigres-fan-token"},
    "MFC":     {"name": "Millonarios FC",                       "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xdEB5A271A67652A84dECb6278D70A6d6A18D7c3b",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xdEB5A271A67652A84dECb6278D70A6d6A18D7c3b",
                "fantokens": "https://www.fantokens.com/trade/millonarios-fan-token"},

    # ── Football: Other European ─────────────────────────────────────────────
    "APL":     {"name": "Apollon Limmasol",                     "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xB407a167fE99eb97970e41b2608d0d9484C489C8",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xB407a167fE99eb97970e41b2608d0d9484C489C8",
                "fantokens": "https://www.fantokens.com/trade/apollon-limassol-fan-token"},
    "DZG":     {"name": "Dinamo Zagreb",                        "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x6412aFDFdF2a465B2E2464A5F9d1743a9CFfd6fF",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x6412aFDFdF2a465B2E2464A5F9d1743a9CFfd6fF",
                "fantokens": "https://www.fantokens.com/trade/dinamo-zagreb-fan-token"},
    "LEG":     {"name": "Legia Warsaw",                         "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x3Ce3946A68EB044C59AFe77dfdfdc71f19EB4328",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x3Ce3946A68EB044C59AFe77dfdfdc71f19EB4328",
                "fantokens": "https://www.fantokens.com/trade/legia-warsaw-fan-token"},
    "LEV":     {"name": "Levante UD",                           "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x69D65E72266b15C2b2ABcD69561399D9BD1843Ef",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x69D65E72266b15C2b2ABcD69561399D9BD1843Ef",
                "fantokens": "https://www.fantokens.com/trade/levante-fan-token"},
    "NOV":     {"name": "Novara Calcio",                        "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xE6BD000D6608E1E5d1476a96e7Cb63c335C595a9",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xE6BD000D6608E1E5d1476a96e7Cb63c335C595a9",
                "fantokens": "https://www.fantokens.com/trade/novara-calcio-fan-token"},
    "YBO":     {"name": "BSC Young Boys",                       "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x0Dc1776c56ffd3A046134Be6fDC23a3214359329",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x0Dc1776c56ffd3A046134Be6fDC23a3214359329",
                "fantokens": "https://www.fantokens.com/trade/young-boys-fan-token"},
    "FOR":     {"name": "Fortuna Sittard",                      "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x4b56F121F769BBdeE3faBA6e8B9163E7cfFDd59a",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x4b56F121F769BBdeE3faBA6e8B9163E7cfFDd59a",
                "fantokens": "https://www.fantokens.com/trade/fortuna-sittard-fan-token"},
    "STV":     {"name": "Sint-Truidense VV",                    "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xe446d966Ba9a36E518cF450AbbD22f45688107Da",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xe446d966Ba9a36E518cF450AbbD22f45688107Da",
                "fantokens": "https://www.fantokens.com/trade/sint-truiden-fan-token"},

    # ── Football: Asian / Southeast Asian ───────────────────────────────────
    "BUFC":    {"name": "Bali United FC",                       "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xe87Cb1546D50F523057d3F94B07381dCE3F85eF9",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xe87Cb1546D50F523057d3F94B07381dCE3F85eF9",
                "fantokens": "https://www.fantokens.com/trade/bali-united-fan-token"},
    "JDT":     {"name": "JOHOR Southern Tigers",                "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x12129aD866906Ab5aa456ae1ebAeA9e8A13E8197",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x12129aD866906Ab5aa456ae1ebAeA9e8A13E8197",
                "fantokens": "https://www.fantokens.com/trade/jdt-fan-token"},
    "PERSIB":  {"name": "Persatuan Sepakbola Indonesia Bandung","sport": "football",   "tier": 3, "expired": False,
                "contract": "0xC34BfBA5dB50152eF3312348A814D24F85748d64",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xC34BfBA5dB50152eF3312348A814D24F85748d64",
                "fantokens": "https://www.fantokens.com/trade/persib-fan-token"},
    "PRSJ":    {"name": "Persija Jakarta",                      "sport": "football",   "tier": 3, "expired": False,
                "contract": "0xB6C7e13752c2d5C94B88A522696b6Dec380971eF",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xB6C7e13752c2d5C94B88A522696b6Dec380971eF",
                "fantokens": "https://www.fantokens.com/trade/persija-jakarta-fan-token"},

    # ── Esports ──────────────────────────────────────────────────────────────
    "OG":      {"name": "OG Esports",                           "sport": "esports",    "tier": 1, "expired": False,
                "contract": "0x19cA0F4aDb29e2130A56b9C9422150B5dc07f294",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x19cA0F4aDb29e2130A56b9C9422150B5dc07f294",
                "fantokens": "https://www.fantokens.com/trade/og-fan-token"},
    "ALL":     {"name": "Alliance",                             "sport": "esports",    "tier": 2, "expired": False,
                "contract": "0xc5C0d1E98D9b1398A37C82Ed81086674baEf2a72",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xc5C0d1E98D9b1398A37C82Ed81086674baEf2a72",
                "fantokens": "https://www.fantokens.com/trade/alliance-fan-token"},
    "TH":      {"name": "Team Heretics",                        "sport": "esports",    "tier": 2, "expired": False,
                "contract": "0x06B4213774DD069cF603ad11770B52F1E98160a7",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x06B4213774DD069cF603ad11770B52F1E98160a7",
                "fantokens": "https://www.fantokens.com/trade/team-heretics-fan-token"},
    "DOJO":    {"name": "Ninjas in Pyjamas",                    "sport": "esports",    "tier": 2, "expired": False,
                "contract": "0xb66D72efc5fD77A8F9Dc2E7c0f14304828956644",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xb66D72efc5fD77A8F9Dc2E7c0f14304828956644",
                "fantokens": "https://www.fantokens.com/trade/ninjas-in-pyjamas-fan-token"},
    "MIBR":    {"name": "Made In Brasil",                       "sport": "esports",    "tier": 2, "expired": False,
                "contract": "0xa8206Af1e6a0289156d45B9d60e5bbD5d1fCf68d",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xa8206Af1e6a0289156d45B9d60e5bbD5d1fCf68d",
                "fantokens": "https://www.fantokens.com/trade/mibr-fan-token"},
    "HASHTAG": {"name": "Hashtag United F.C.",                  "sport": "football",   "tier": 3, "expired": False,
                "contract": "0x7Be4Aebc9900d2C1b628530ffc59416A98420B15",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x7Be4Aebc9900d2C1b628530ffc59416A98420B15",
                "fantokens": "https://www.fantokens.com/trade/hashtag-united-fan-token"},

    # ── MMA ──────────────────────────────────────────────────────────────────
    "UFC":     {"name": "UFC",                                  "sport": "mma",        "tier": 1, "expired": False,
                "contract": "0x0ffa63502f957b66e61F87761cc240e51C74cee5",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x0ffa63502f957b66e61F87761cc240e51C74cee5",
                "fantokens": "https://www.fantokens.com/trade/ufc-fan-token"},
    "PFL":     {"name": "Professional Fighters League",        "sport": "mma",        "tier": 2, "expired": False,
                "contract": "0xde05490B7AC4B86e54eFf43f4F809C3a7Bb16564",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xde05490B7AC4B86e54eFf43f4F809C3a7Bb16564",
                "fantokens": "https://www.fantokens.com/trade/pfl-fan-token"},

    # ── Rugby ─────────────────────────────────────────────────────────────────
    "SFP":     {"name": "Stade Francais Paris",                 "sport": "rugby",      "tier": 2, "expired": False,
                "contract": "0x2a89f8af25B01B837d67be3B1A162A663F77b26E",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x2a89f8af25B01B837d67be3B1A162A663F77b26E",
                "fantokens": "https://www.fantokens.com/trade/stade-francais-fan-token"},

    # ══════════════════════════════════════════════════════════════════════════
    # EXPIRED SOCIOS/CHILIZ PARTNERSHIPS (expired=True)
    # Tokens remain on-chain and tradeable. Partnership utility via Socios
    # app has ended. Contract addresses are still valid for on-chain queries.
    # ══════════════════════════════════════════════════════════════════════════
    "SAUBER":  {"name": "Alfa Romeo Racing Orlen",              "sport": "formula1",   "tier": 2, "expired": True,
                "contract": "0xcf6D626203011e5554C82baBE17dd7CDC4Ee86BF",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xcf6D626203011e5554C82baBE17dd7CDC4Ee86BF",
                "fantokens": "https://www.fantokens.com/trade/alfa-romeo-racing-fan-token"},
    "AM":      {"name": "Aston Martin Cognizant",               "sport": "formula1",   "tier": 2, "expired": True,
                "contract": "0x3757951792eDFC2CE196E4C06CFfD04027e87403",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x3757951792eDFC2CE196E4C06CFfD04027e87403",
                "fantokens": "https://www.fantokens.com/trade/aston-martin-cognizant-fan-token"},
    "ATLAS":   {"name": "Atlas FC",                             "sport": "football",   "tier": 3, "expired": True,
                "contract": "0x936AE5911F49634fD7f4F7385dB1613c5E350EdE",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x936AE5911F49634fD7f4F7385dB1613c5E350EdE"},
    "CAI":     {"name": "Club Atletico Independiente",          "sport": "football",   "tier": 3, "expired": True,
                "contract": "0x8A48AD8279318757ea7905b460816c4B92de447E",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x8A48AD8279318757ea7905b460816c4B92de447E"},
    "CHVS":    {"name": "Club Deportivo Guadalajara",           "sport": "football",   "tier": 2, "expired": True,
                "contract": "0xF66288961A3495Ea9140fBD7c69E70a59Db08b16",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xF66288961A3495Ea9140fBD7c69E70a59Db08b16"},
    "SAN":     {"name": "Club Santos Laguna",                   "sport": "football",   "tier": 2, "expired": True,
                "contract": "0x44941A2d2049BE0ACB00Baf0A5dEE8931c33712E",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x44941A2d2049BE0ACB00Baf0A5dEE8931c33712E"},
    "DAVIS":   {"name": "Davis Cup",                            "sport": "tennis",     "tier": 2, "expired": True,
                "contract": "0xF50b3db1d498b69b0dc8ccc0b03643009a6bDA78",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xF50b3db1d498b69b0dc8ccc0b03643009a6bDA78"},
    "ENDCEX":  {"name": "Endpoint",                             "sport": "esports",    "tier": 3, "expired": True,
                "contract": "0x3F521D391E2aD0093d3BFABB2516F1C57d73B4d1",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x3F521D391E2aD0093d3BFABB2516F1C57d73B4d1"},
    "QUINS":   {"name": "Harlequins",                           "sport": "rugby",      "tier": 2, "expired": True,
                "contract": "0x539e00D2487a06F3F08CDAF7Bf7A8b4a32C3a14E",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x539e00D2487a06F3F08CDAF7Bf7A8b4a32C3a14E"},
    "TIGERS":  {"name": "Leicester Tigers",                     "sport": "rugby",      "tier": 2, "expired": True,
                "contract": "0x0b39ff3de07e8B6d2b97357d6F2A658ed7De52Cf",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x0b39ff3de07e8B6d2b97357d6F2A658ed7De52Cf"},
    "RACING":  {"name": "Racing Club",                          "sport": "football",   "tier": 3, "expired": True,
                "contract": "0x06Ed14A885D0710118fc20D51EfDC151a48005b3",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x06Ed14A885D0710118fc20D51EfDC151a48005b3"},
    "ROUSH":   {"name": "Roush Fenway Keselowski",              "sport": "motorsport", "tier": 3, "expired": True,
                "contract": "0xBA20eF1670393150d1C1b135F45043740ec3a729",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xBA20eF1670393150d1C1b135F45043740ec3a729"},
    "SARRIES": {"name": "Saracens",                             "sport": "rugby",      "tier": 2, "expired": True,
                "contract": "0x753DDA10c7b3069f0C90837dC3755c7c40A81B8c",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x753DDA10c7b3069f0C90837dC3755c7c40A81B8c"},
    "SHARKS":  {"name": "The Sharks",                           "sport": "rugby",      "tier": 2, "expired": True,
                "contract": "0x1f5Ed1182b673338ECff0eeaB13ed79cEaf775f5",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x1f5Ed1182b673338ECff0eeaB13ed79cEaf775f5"},
    "UCH":     {"name": "Universidad de Chile",                 "sport": "football",   "tier": 3, "expired": True,
                "contract": "0xA082EC45aF038100D4989636A4A5E52fD7e5C636",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0xA082EC45aF038100D4989636A4A5E52fD7e5C636"},
    "VASCO":   {"name": "Vasco da Gama",                        "sport": "football",   "tier": 2, "expired": True,
                "contract": "0x6d72034D7508D16988bf84638D51592A8c02887b",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x6d72034D7508D16988bf84638D51592A8c02887b"},
    "NAVI":    {"name": "Natus Vincere",                        "sport": "esports",    "tier": 2, "expired": True,
                "contract": "0x02728748392f1875682940681f4c936fc683a68e",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x02728748392f1875682940681f4c936fc683a68e"},
    "VIT":     {"name": "Team Vitality",                        "sport": "esports",    "tier": 2, "expired": True,
                "contract": "0x94A54b796744f07cfB499E2b6050F8b71A012c2c",
                "chain": "chiliz", "chiliscan": "https://chiliscan.com/token/0x94A54b796744f07cfB499E2b6050F8b71A012c2c"},
}

# ══════════════════════════════════════════════════════════════════════════════
# MULTI-CHAIN FAN TOKEN REGISTRY
# These tokens are NOT on Chiliz Chain. Different ecosystems, different issuers.
# No Fan Token Play mechanics. No chiliscan verification.
# ══════════════════════════════════════════════════════════════════════════════
MULTICHAIN_FAN_TOKEN_REGISTRY = {
    "ALPINE":  {"name": "Alpine F1 Team",     "sport": "formula1",  "chain": "BSC",
                "contract": "0x287880Ea252b52b63Cc5f40a2d3E5A44aa665a76",
                "explorer": "https://bscscan.com/token/0x287880Ea252b52b63Cc5f40a2d3E5A44aa665a76",
                "issuer": "Binance"},
    "BJK":     {"name": "Besiktas",           "sport": "football",  "chain": "Ethereum",
                "contract": "0x1903be033d3e436dd79a8cf9030675bcf97ab589",
                "explorer": "https://etherscan.io/token/0x1903be033d3e436dd79a8cf9030675bcf97ab589",
                "issuer": "Paribu"},
    "PORTO":   {"name": "FC Porto",           "sport": "football",  "chain": "BSC",
                "contract": "0x49f2145d6366099e13B10FbF80646C0F377eE7f6",
                "explorer": "https://bscscan.com/token/0x49f2145d6366099e13B10FbF80646C0F377eE7f6",
                "issuer": "Binance"},
    "FB":      {"name": "Fenerbahce",         "sport": "football",  "chain": "Ethereum",
                "contract": "0xfb19075d77a0f111796fb259819830f4780f1429",
                "explorer": "https://etherscan.io/token/0xfb19075d77a0f111796fb259819830f4780f1429",
                "issuer": "Paribu"},
    "SANTOS":  {"name": "Santos FC",          "sport": "football",  "chain": "BSC",
                "contract": "0xA64455a4553C9034236734FadDAddbb64aCE4Cc7",
                "explorer": "https://bscscan.com/token/0xA64455a4553C9034236734FadDAddbb64aCE4Cc7",
                "issuer": "Binance"},
    "LAZIO":   {"name": "SS Lazio",           "sport": "football",  "chain": "BSC",
                "contract": "0x77d547256a2cd95f32f67ae0313e450ac200648d",
                "explorer": "https://bscscan.com/token/0x77d547256a2cd95f32f67ae0313e450ac200648d",
                "issuer": "Binance"},
    # ── BiTCI Chain tokens ───────────────────────────────────────────────────
    "SNFT":    {"name": "Spain National Football Team", "sport": "football", "chain": "BiTCI",
                "contract": "0x3e6F1be54FEb9CC37dBfC31A894a8810357C3F9C",
                "explorer": "https://v3.bitciexplorer.com/token/0x3e6F1be54FEb9CC37dBfC31A894a8810357C3F9C",
                "fantokens": "https://www.fantokens.com/trade/spain-national-football-team",
                "issuer": "BiTCI", "wc2026": True},
    "BFT":     {"name": "Brazil National Football Team", "sport": "football", "chain": "BiTCI",
                "contract": "0x4270A3D1a61FC6b86Ea9E19730E529ACEe592c3B",
                "explorer": "https://v2.bitciexplorer.com/token/0x4270A3D1a61FC6b86Ea9E19730E529ACEe592c3B",
                "fantokens": "https://www.fantokens.com/trade/brazil-national-football-team",
                "issuer": "BiTCI", "wc2026": True,
                "note": "Host nation WC2026 — NCSI x3.5-4.0 modifier"},
    # ── Ethereum tokens ──────────────────────────────────────────────────────
    "VATRENI": {"name": "Croatia Football Federation", "sport": "football", "chain": "Ethereum",
                "contract": "0x4CdA244c7e93045c88f86e6Ec571C223bEc2fc70",
                "explorer": "https://etherscan.io/token/0x4CdA244c7e93045c88f86e6Ec571C223bEc2fc70",
                "fantokens": "https://www.fantokens.com/trade/croatia-football-federation",
                "issuer": "independent", "wc2026": True},
}



# Sport → tickers mapping for lookup by sport
SPORT_TO_TOKENS = {}
for ticker, data in FAN_TOKEN_REGISTRY.items():
    sport = data["sport"]
    SPORT_TO_TOKENS.setdefault(sport, []).append(ticker)

# Name fragments → ticker for fuzzy lookup
NAME_TO_TICKER = {}
for ticker, data in FAN_TOKEN_REGISTRY.items():
    NAME_TO_TICKER[ticker.lower()] = ticker
    for word in data["name"].lower().split():
        if len(word) > 3:
            NAME_TO_TICKER.setdefault(word, ticker)

# ── Verifiable sources registry ────────────────────────────────────────────────
VERIFIABLE_SOURCES = {
    "lineup_confirmation": {
        "football":  {"source": "Club official X/Twitter account (T-2h)", "tier": 1,
                      "backup": "BBC Sport match centre", "note": "Official team sheet T-1h"},
        "rugby":     {"source": "Official club website team sheet (T-1h)", "tier": 1,
                      "backup": "Rugby Pass (rugbypass.com)", "note": "Released 1h pre-match"},
        "ice_hockey":{"source": "Beat reporter morning skate tweet (T-3h to T-1h)", "tier": 2,
                      "backup": "Daily Faceoff (dailyfaceoff.com)", "note": "Morning skate lineups"},
        "basketball":{"source": "NBA.com/players/injuries (official injury report)", "tier": 1,
                      "backup": "ESPN NBA injuries", "note": "Final report T-1h"},
        "cricket":   {"source": "ESPNcricinfo squad and XI announcement", "tier": 1,
                      "backup": "Cricbuzz", "note": "Announced at toss"},
        "formula1":  {"source": "formula1.com/results (qualifying tab)", "tier": 1,
                      "backup": "Motorsport.com", "note": "Grid set post-qualifying"},
        "mma":       {"source": "UFC.com event page weigh-in results", "tier": 1,
                      "backup": "@UFC on X", "note": "Day-before weigh-in"},
        "default":   {"source": "Official governing body or club website", "tier": 1,
                      "backup": "BBC Sport / ESPN", "note": "Check official source first"},
    },
    "match_result": {
        "football":  {"source": "BBC Sport (bbc.co.uk/sport/football)", "tier": 1,
                      "backup": "Official league app", "note": "Final result + stats"},
        "rugby":     {"source": "BBC Sport rugby union / World Rugby (world.rugby)", "tier": 1,
                      "backup": "Premiership Rugby (premiershiprugby.com)", "note": ""},
        "cricket":   {"source": "ESPNcricinfo (espncricinfo.com)", "tier": 1,
                      "backup": "Cricbuzz", "note": "Full scorecard"},
        "formula1":  {"source": "formula1.com/results", "tier": 1,
                      "backup": "Autosport", "note": "Allow 3h post-race for steward decisions"},
        "mma":       {"source": "UFC.com/results", "tier": 1,
                      "backup": "MMA Fighting (mmafighting.com)", "note": ""},
        "ice_hockey":{"source": "nhl.com/scores", "tier": 1,
                      "backup": "ESPN NHL", "note": ""},
        "basketball":{"source": "nba.com/scores", "tier": 1,
                      "backup": "Basketball Reference", "note": ""},
        "tennis":    {"source": "atptour.com/scores or wtatennis.com/scores", "tier": 1,
                      "backup": "Tennis Abstract", "note": ""},
        "afl":       {"source": "afl.com.au/matches", "tier": 1,
                      "backup": "AFL Tables (afltables.com)", "note": ""},
        "default":   {"source": "Official governing body results page", "tier": 1,
                      "backup": "BBC Sport / ESPN", "note": ""},
    },
    "disciplinary_ban": {
        "football":  {"source": "FA: thefa.com/football-rules-governance/disciplinary", "tier": 1,
                      "backup": "UEFA: UEFA.com/insideuefa/disciplinary", "note": ""},
        "rugby":     {"source": "World Rugby: world.rugby/the-game/judicial-decisions", "tier": 1,
                      "backup": "Premiership Rugby disciplinary section", "note": "All decisions published as PDFs"},
        "mma":       {"source": "USADA: usada.org/testing/results/sanctions", "tier": 1,
                      "backup": "UFC.com news announcements", "note": ""},
        "cricket":   {"source": "ICC: icc-cricket.com/about/cricket/rules-and-regulations", "tier": 1,
                      "backup": "ESPNcricinfo news", "note": ""},
        "formula1":  {"source": "FIA: fia.com/documents/decisions", "tier": 1,
                      "backup": "Racefans.net super licence points tracker", "note": ""},
        "rugby_league": {"source": "NRL: nrl.com/the-game/integrity-and-welfare/match-review-committee", "tier": 1,
                         "backup": "RFL: rfl.uk/the-game/discipline", "note": ""},
        "default":   {"source": "Official governing body disciplinary page", "tier": 1,
                      "backup": "BBC Sport / ESPN", "note": ""},
    },
    "player_stats": {
        "football":  {"source": "FBref (fbref.com) — xG, progressive actions, per-90", "tier": 2,
                      "backup": "WhoScored (whoscored.com)", "note": "FBref most comprehensive"},
        "rugby":     {"source": "ESPN Scrum (espnscrum.com) — international stats", "tier": 2,
                      "backup": "Rugby Reference (rugbyreference.com)", "note": ""},
        "cricket":   {"source": "Statsguru (stats.espncricinfo.com)", "tier": 2,
                      "backup": "CricketArchive (cricketarchive.com)", "note": "Deepest cricket database"},
        "formula1":  {"source": "formula1.com/results — qualifying and race", "tier": 1,
                      "backup": "Motorsport Stats (motorsportstats.com)", "note": ""},
        "mma":       {"source": "UFC Stats (ufcstats.com) — official fight stats", "tier": 1,
                      "backup": "Tapology (tapology.com)", "note": ""},
        "ice_hockey":{"source": "Natural Stat Trick (naturalstattrick.com) — advanced", "tier": 2,
                      "backup": "Hockey Reference (hockey-reference.com)", "note": "CF%, GSAx"},
        "basketball":{"source": "NBA.com/stats — official advanced metrics", "tier": 1,
                      "backup": "Cleaning the Glass (cleaningtheglass.com)", "note": ""},
        "tennis":    {"source": "Tennis Abstract (tennisabstract.com) — surface splits", "tier": 2,
                      "backup": "Ultimate Tennis Statistics", "note": ""},
        "afl":       {"source": "AFL Tables (afltables.com)", "tier": 2,
                      "backup": "Footywire (footywire.com)", "note": ""},
        "default":   {"source": "FBref or sport-specific official stats", "tier": 2,
                      "backup": "ESPN", "note": ""},
    },
    "transfer_news": {
        "football":  {"source": "Fabrizio Romano @FabrizioRomano — 'here we go' = confirmed", "tier": 2,
                      "backup": "Club official announcement (definitive)", "note": "Tier 1 = club announcement only"},
        "default":   {"source": "Club official announcement", "tier": 1,
                      "backup": "The Athletic or BBC Sport", "note": ""},
    },
    "rankings": {
        "football":  {"source": "FIFA World Rankings: fifa.com/fifa-world-ranking", "tier": 1,
                      "backup": "UEFA club rankings: UEFA.com/memberassociations/uefarankings", "note": ""},
        "rugby":     {"source": "World Rugby Rankings: world.rugby/rugby-world-rankings", "tier": 1,
                      "backup": "ESPN Scrum", "note": "Updated weekly"},
        "cricket":   {"source": "ICC Rankings: icc-cricket.com/rankings", "tier": 1,
                      "backup": "ESPNcricinfo rankings", "note": "All formats"},
        "mma":       {"source": "UFC Rankings: ufc.com/rankings", "tier": 1,
                      "backup": "Tapology rankings", "note": "Updated weekly"},
        "tennis":    {"source": "ATP: atptour.com/rankings | WTA: wtatennis.com/rankings", "tier": 1,
                      "backup": "Tennis Abstract", "note": ""},
        "formula1":  {"source": "formula1.com/standings", "tier": 1,
                      "backup": "Motorsport.com", "note": "Driver and constructor"},
        "default":   {"source": "Official governing body rankings page", "tier": 1,
                      "backup": "ESPN", "note": ""},
    },
}


# ── Helpers ────────────────────────────────────────────────────────────────────

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_macro_state() -> dict:
    if MACRO_STATE.exists():
        try:
            return json.loads(MACRO_STATE.read_text())
        except Exception:
            pass
    return {
        "macro_state": {
            "crypto_cycle": {
                "phase": "NEUTRAL",
                "macro_modifier": 1.00,
                "btc_vs_200d_ma": "unknown",
                "signal_note": "Using default neutral — run scripts/update_macro_state.py to refresh",
            },
            "active_events": [],
            "last_updated": "unknown",
            "freshness_warning": "macro-state.json not found — using neutral defaults",
        }
    }


def get_skill_files(sport: str, use_case: str) -> list:
    slug = sport.replace("_", "-")
    files = []
    for path in [
        ROOT / "macro" / "macro-overview.md",
        ROOT / "market" / f"market-{slug}.md",
        ROOT / "sports" / slug / f"sport-domain-{slug}.md",
    ]:
        if path.exists():
            files.append(path)

    athlete_dir = ROOT / "athlete" / slug
    if athlete_dir.is_dir():
        files.extend(sorted(athlete_dir.glob("athlete-intel-*.md")))

    if use_case in ("fan_token_tier1", "fan_token_tier2", "governance"):
        bridge = ROOT / "fan-token" / f"{slug}-token-intelligence"
        if bridge.is_dir():
            files.extend(sorted(bridge.glob("*.md")))
        defi = ROOT / "fan-token" / "defi-liquidity-intelligence"
        if defi.is_dir():
            defi_files = sorted(defi.glob("*.md"))
            if defi_files:
                files.append(defi_files[0])

    return files


def compute_sms(skill_files: list, macro_modifier: float) -> tuple:
    layers = set()
    for f in skill_files:
        try:
            top = Path(f).relative_to(ROOT).parts[0]
        except ValueError:
            continue
        if top == "macro":       layers.add(5)
        elif top == "market":    layers.add(4)
        elif top == "sports":    layers.add(1)
        elif top == "athlete":   layers.add(2)
        elif top == "fan-token": layers.add(3)

    sms = round(
        (len(layers) / 5) * 0.35 * 100 +
        (1.0 if macro_modifier >= 0.75 else 0.5) * 0.25 * 100 +
        0.25 * 100 +
        min(macro_modifier, 1.0) * 0.15 * 100, 1
    )
    tier = (
        "HIGH_QUALITY" if sms >= 80 else
        "GOOD"         if sms >= 60 else
        "PARTIAL"      if sms >= 40 else
        "INCOMPLETE"   if sms >= 20 else
        "INSUFFICIENT"
    )
    return sms, tier, sorted(layers)


# ── Tool implementations ───────────────────────────────────────────────────────

def tool_signal(sport, event_id, use_case, home_team, away_team, include_defi):
    files      = get_skill_files(sport, use_case)
    macro_data = get_macro_state()
    macro_mod  = (macro_data.get("macro_state", {})
                             .get("crypto_cycle", {})
                             .get("macro_modifier", 1.00))
    sms, tier, layers = compute_sms(files, macro_mod)
    override = macro_mod < 0.75

    result = {
        "signal": {
            "direction":          "HOME",
            "adjusted_score":     round(55.0 * macro_mod, 1),
            "confidence_tier":    "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "WAIT" if (override or sms < 60) else "ENTER",
        },
        "sportmind_score": {
            "sms":           sms,
            "sms_tier":      tier,
            "layers_loaded": layers,
            "coverage_note": f"{len(files)} skill files loaded",
        },
        "modifiers": {
            "macro_modifier":     round(macro_mod, 2),
            "composite_modifier": round(macro_mod, 2),
            "flags": {
                "lineup_unconfirmed":    False,
                "macro_override_active": override,
                "liquidity_warning":     False,
                "injury_warning":        False,
            },
        },
        "event_context": {
            "sport":     sport,
            "event_id":  event_id   or "unspecified",
            "home_team": home_team  or "unspecified",
            "away_team": away_team  or "unspecified",
            "use_case":  use_case,
        },
        "skill_stack":       [str(Path(f).relative_to(ROOT)) for f in files],
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
        "agent_note": (
            "direction is a structural baseline from static skill intelligence. "
            "Integrate live athlete availability and form for full accuracy. "
            "See platform/live-signals.md and core/temporal-awareness.md."
        ),
    }

    if include_defi:
        result["defi_context"] = {
            "note":      "Live DeFi data requires real-time Chiliz Chain query.",
            "reference": "fan-token/defi-liquidity-intelligence/",
            "kayen_api": "platform/data-connector-templates.md",
        }
    return result


def tool_macro():
    state = get_macro_state()
    state["retrieval_note"] = (
        "Update: python scripts/update_macro_state.py  "
        "or connect live via platform/data-connector-templates.md (CoinGecko)"
    )
    state["sportmind_version"] = VERSION
    return state


def tool_stack(sport, use_case, compressed):
    files = get_skill_files(sport, use_case)
    stack = []
    for f in files:
        content = f.read_text(encoding="utf-8")
        entry = {
            "skill_id": str(Path(f).relative_to(ROOT)),
            "sha256":   hashlib.sha256(content.encode()).hexdigest(),
            "content":  (content[:600] + "\n\n[COMPRESSED]") if compressed else content,
        }
        stack.append(entry)
    return {
        "sport":             sport,
        "use_case":          use_case,
        "stack":             stack,
        "total_files":       len(stack),
        "loading_order":     "macro → market → domain → athlete → fan-token",
        "sportmind_version": VERSION,
    }


def tool_verify(skill_id, content):
    if not HASHES_FILE.exists():
        return {"verified": False, "reason": "skill-hashes.json not found"}
    hashes = json.loads(HASHES_FILE.read_text())
    actual = hashlib.sha256(content.encode("utf-8")).hexdigest()
    for path, entry in hashes.get("files", {}).items():
        if skill_id.lower() in path.lower():
            expected = entry.get("sha256", "")
            if actual == expected:
                return {"verified": True,  "file_path": path, "hash": actual[:16] + "..."}
            else:
                return {"verified": False, "file_path": path, "reason": "Hash mismatch"}
    return {"verified": True, "reason": "Not in registry — new or unregistered file"}


def tool_agent_status(agent_id, include_audit, last_n):
    return {
        "agents":        [],
        "system_health": "UNKNOWN",
        "note": (
            "sportmind_agent_status requires a running SportMind agent instance. "
            "See core/autonomous-agent-framework.md and examples/agentic-workflows/"
        ),
        "timestamp":         now_iso(),
        "sportmind_version": VERSION,
    }


def tool_pre_match(sport, home_team, away_team, competition, kickoff, use_case):
    """Orchestrated full pre-match reasoning package."""
    files      = get_skill_files(sport, use_case)
    macro_data = get_macro_state()
    macro_mod  = (macro_data.get("macro_state", {})
                             .get("crypto_cycle", {})
                             .get("macro_modifier", 1.00))
    sms, tier, layers = compute_sms(files, macro_mod)
    override = macro_mod < 0.75

    # Narrative momentum check (structural signals from skill availability)
    narrative_signals = []
    if (ROOT / "core" / "core-narrative-momentum.md").exists():
        narrative_signals.append("Narrative momentum framework loaded — check rivalry, milestone, and home debut signals")

    # Disciplinary awareness
    disciplinary_note = (
        "Run sportmind_disciplinary to check DSM status for key players before "
        "finalising commercial recommendation."
    )

    # Statistical reasoning reference
    stats_note = (
        f"See core/player-statistical-reasoning.md for {sport} "
        "position-specific benchmarks and interpretation rules."
    )

    # Verifiable source for lineup
    lineup_source = (VERIFIABLE_SOURCES
                     .get("lineup_confirmation", {})
                     .get(sport, VERIFIABLE_SOURCES["lineup_confirmation"]["default"]))

    return {
        "pre_match_signal": {
            "sport":       sport,
            "home_team":   home_team   or "unspecified",
            "away_team":   away_team   or "unspecified",
            "competition": competition or "unspecified",
            "kickoff":     kickoff     or "unspecified",
            "use_case":    use_case,
        },
        "signal": {
            "direction":          "HOME",
            "adjusted_score":     round(55.0 * macro_mod, 1),
            "confidence_tier":    "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "WAIT" if (override or sms < 60) else "ENTER",
        },
        "sportmind_score": {
            "sms":           sms,
            "sms_tier":      tier,
            "layers_loaded": layers,
            "files_loaded":  len(files),
        },
        "macro_context": {
            "macro_modifier":     round(macro_mod, 2),
            "macro_override":     override,
            "phase":              macro_data.get("macro_state", {}).get("crypto_cycle", {}).get("phase", "UNKNOWN"),
        },
        "availability_check": {
            "status":    "MANUAL_REQUIRED",
            "source":    lineup_source["source"],
            "tier":      lineup_source["tier"],
            "note":      "Lineup confirmation requires live data — use source above",
        },
        "disciplinary_check": {
            "status": "NOT_CHECKED",
            "action": disciplinary_note,
        },
        "narrative_momentum": {
            "signals": narrative_signals,
            "reference": "core/core-narrative-momentum.md",
            "note": "Apply narrative modifier only if statistical signals within ±15% of neutral",
        },
        "statistical_reasoning": {
            "reference": f"core/player-statistical-reasoning.md",
            "note": stats_note,
        },
        "skill_stack":        [str(Path(f).relative_to(ROOT)) for f in files],
        "reasoning_sequence": [
            "1. sportmind_macro — verify macro modifier",
            "2. sportmind_pre_match (this tool) — full pre-match package",
            "3. sportmind_disciplinary — check DSM for key players",
            "4. Verify lineup via source above",
            "5. Apply statistical reasoning framework",
            "6. Generate final signal",
        ],
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
    }


def tool_disciplinary(player, sport, club, include_framework):
    """Disciplinary check — DSM level, flags, commercial modifier."""

    # Load disciplinary intelligence framework if available
    disc_file = ROOT / "core" / "athlete-disciplinary-intelligence.md"
    framework_loaded = disc_file.exists()

    # Sport-specific regulatory body
    regulatory_bodies = {
        "football":    "FA / UEFA / FIFA — thefa.com/football-rules-governance/disciplinary",
        "rugby":       "World Rugby citing commissioner — world.rugby/the-game/judicial-decisions",
        "rugby_league":"NRL Match Review Committee / RFL — nrl.com/the-game/integrity-and-welfare",
        "cricket":     "ICC Code of Conduct — icc-cricket.com/about/cricket/rules-and-regulations",
        "formula1":    "FIA Stewards — fia.com/documents/decisions",
        "mma":         "USADA / Athletic Commission / UFC Code — usada.org/testing/results/sanctions",
        "tennis":      "ATP/WTA Integrity Program",
        "basketball":  "NBA Player Conduct Policy",
        "ice_hockey":  "NHL Department of Player Safety — nhl.com/news/department-player-safety",
        "afl":         "AFL Tribunal — afl.com.au/tribunal",
    }

    reg_body = regulatory_bodies.get(sport, "Governing body disciplinary body — check official site")

    result = {
        "disciplinary_check": {
            "player":     player or "unspecified",
            "club":       club   or "unspecified",
            "sport":      sport,
            "status":     "MANUAL_CHECK_REQUIRED",
            "note": (
                "SportMind does not have access to live disciplinary data. "
                "Check the regulatory source below for current status."
            ),
        },
        "regulatory_source": reg_body,
        "dsm_framework": {
            "loaded":    framework_loaded,
            "reference": "core/athlete-disciplinary-intelligence.md",
            "tiers": {
                "tier_1": "On-field technical — DSM MINIMAL — no commercial modifier",
                "tier_2": "On-field conduct — DSM MODERATE — modifier 0.88",
                "tier_3": "Off-field conduct — DSM SEVERE — modifier 0.72 — COMMERCIAL_RISK_ACTIVE",
                "tier_4": "Criminal/legal — DSM CATASTROPHIC — ABSTAIN",
            },
        },
        "flags_to_check": [
            "CITING_ACTIVE",
            "BAN_CONFIRMED",
            "COMMERCIAL_RISK_ACTIVE",
            "LEGAL_PROCEEDINGS_ACTIVE",
            "SUSPENSION_RISK",
            "CONDUCT_RESIDUAL",
            "INVESTIGATION_ACTIVE",
        ],
        "commercial_rule": (
            "Never generate ENTER recommendation when COMMERCIAL_RISK_ACTIVE "
            "or LEGAL_PROCEEDINGS_ACTIVE is set on a key commercial asset."
        ),
        "agent_action": (
            "1. Check regulatory source for current player status. "
            "2. Classify offence tier using core/athlete-disciplinary-intelligence.md. "
            "3. Apply DSM modifier and set appropriate flags. "
            "4. Adjust commercial signal accordingly."
        ),
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
    }

    if include_framework and framework_loaded:
        result["framework_excerpt"] = (
            "Four-tier offence taxonomy: Tier 1 (on-field technical) → "
            "Tier 2 (on-field conduct) → Tier 3 (off-field conduct) → "
            "Tier 4 (criminal/legal). DSM values: MINIMAL (1.00) / "
            "MODERATE (0.88) / SEVERE (0.72) / CATASTROPHIC (ABSTAIN). "
            "Seven flags: CITING_ACTIVE, BAN_CONFIRMED, COMMERCIAL_RISK_ACTIVE, "
            "LEGAL_PROCEEDINGS_ACTIVE, SUSPENSION_RISK, CONDUCT_RESIDUAL, "
            "INVESTIGATION_ACTIVE. See full framework for sport-specific details."
        )

    return result


def tool_fan_token_lookup(query, include_registry):
    """Resolve club name, ticker, or sport to fan token context."""
    query_lower = query.strip().lower()
    matches = []

    # Exact ticker match
    if query.upper() in FAN_TOKEN_REGISTRY:
        matches = [query.upper()]

    # Sport match
    elif query_lower in SPORT_TO_TOKENS:
        matches = SPORT_TO_TOKENS[query_lower]

    # Name fragment match
    else:
        # Try name fragments
        for word in query_lower.split():
            if word in NAME_TO_TICKER:
                ticker = NAME_TO_TICKER[word]
                if ticker not in matches:
                    matches.append(ticker)
        # Direct name substring
        if not matches:
            for ticker, data in FAN_TOKEN_REGISTRY.items():
                if query_lower in data["name"].lower():
                    matches.append(ticker)

    if not matches:
        return {
            "query":   query,
            "found":   False,
            "message": (
                f"No fan token found for '{query}' in the SportMind registry. "
                "Registry covers 24 verified Chiliz Chain tokens. "
                "Check chiliscan.com/token/top-erc20 for the full on-chain list."
            ),
            "registry_size":     len(FAN_TOKEN_REGISTRY),
            "sportmind_version": VERSION,
        }

    tokens = []
    for ticker in matches[:10]:  # Cap at 10 results
        data = FAN_TOKEN_REGISTRY[ticker]
        token_info = {
            "ticker":          ticker,
            "name":            data["name"],
            "sport":           data["sport"],
            "market_cap_tier": data["tier"],
            "contract_address":data["contract"],
            "chain":           "Chiliz Chain (Chain ID: 88888)",
            "chiliscan_url":   data["chiliscan"],
            "fantokens_url":   data["fantokens"],
            "skill_stack": {
                "domain":     f"sports/{data['sport']}/sport-domain-{data['sport']}.md",
                "athlete":    f"athlete/{data['sport']}/athlete-intel-{data['sport']}.md",
                "fan_token":  f"fan-token/{data['sport']}-token-intelligence/",
                "use_case_recommended": (
                    "fan_token_tier1" if data["tier"] == 1 else "fan_token_tier2"
                ),
            },
        }
        # Append Fan Token Play fields if confirmed for this token
        if "fan_token_play" in data:
            token_info["fan_token_play"] = {
                "path":           data["fan_token_play"],
                "confirmed_date": data.get("ftp_confirmed_date"),
                "note":           data.get("ftp_note"),
                "skill_ref":      "fan-token/gamified-tokenomics-intelligence/",
            }
        tokens.append(token_info)

    result = {
        "query":             query,
        "found":             True,
        "total_matches":     len(matches),
        "tokens":            tokens,
        "chain":             "Chiliz Chain — Chain ID 88888",
        "registry_source":   "chiliscan.com/token/top-erc20 (verified contract addresses)",
        "market_cap_tiers": {
            "tier_1": ">$10M on-chain market cap",
            "tier_2": "$1M–$10M on-chain market cap",
            "tier_3": "<$1M on-chain market cap",
        },
        "sportmind_version": VERSION,
    }

    if include_registry:
        result["full_registry"] = {
            ticker: {
                "name":    d["name"],
                "sport":   d["sport"],
                "tier":    d["tier"],
                "contract":d["contract"],
            }
            for ticker, d in FAN_TOKEN_REGISTRY.items()
        }

    return result


def tool_sentiment_snapshot(token, use_case):
    """Multi-axis sentiment state for a token."""

    # Resolve token
    ticker = token.upper()
    token_data = FAN_TOKEN_REGISTRY.get(ticker)

    macro_data = get_macro_state()
    macro_mod  = (macro_data.get("macro_state", {})
                             .get("crypto_cycle", {})
                             .get("macro_modifier", 1.00))
    macro_phase = (macro_data.get("macro_state", {})
                              .get("crypto_cycle", {})
                              .get("phase", "UNKNOWN"))

    if not token_data:
        # Try name lookup
        for t, d in FAN_TOKEN_REGISTRY.items():
            if token.lower() in d["name"].lower():
                ticker = t
                token_data = d
                break

    if not token_data:
        return {
            "token":   token,
            "found":   False,
            "message": f"Token '{token}' not in SportMind registry. Use sportmind_fan_token_lookup first.",
            "sportmind_version": VERSION,
        }

    sport = token_data["sport"]
    files = get_skill_files(sport, use_case)
    sms, sms_tier, layers = compute_sms(files, macro_mod)

    return {
        "token":       ticker,
        "found":       True,
        "name":        token_data["name"],
        "sport":       sport,
        "use_case":    use_case,
        "sentiment_snapshot": {
            "macro_sentiment": {
                "phase":           macro_phase,
                "macro_modifier":  round(macro_mod, 2),
                "signal":          "POSITIVE" if macro_mod >= 1.0 else ("NEUTRAL" if macro_mod >= 0.85 else "NEGATIVE"),
                "note":            "Update macro state via scripts/update_macro_state.py",
            },
            "fan_sentiment": {
                "status":    "MANUAL_CHECK_REQUIRED",
                "reference": "fan-token/fan-sentiment-intelligence/fan-sentiment-intelligence.md",
                "note":      "Check current emotional arc phase (Peak/Celebration/Normalisation etc.)",
            },
            "social_sentiment": {
                "status":    "MANUAL_CHECK_REQUIRED",
                "reference": "fan-token/athlete-social-lift/fan-token-athlete-social-lift.md",
                "note":      "Check AELS for key players and current social volume",
            },
            "commercial_sentiment": {
                "status":    "MANUAL_CHECK_REQUIRED",
                "reference": "fan-token/brand-score/",
                "note":      "Check for active DSM flags — run sportmind_disciplinary for key players",
            },
            "disciplinary_sentiment": {
                "status":    "NOT_CHECKED",
                "action":    "Run sportmind_disciplinary for key players before commercial recommendation",
                "flags_to_check": ["COMMERCIAL_RISK_ACTIVE", "LEGAL_PROCEEDINGS_ACTIVE"],
            },
            "supply_mechanics": (
                {
                    "fan_token_play_path":   token_data.get("fan_token_play"),
                    "confirmed_date":        token_data.get("ftp_confirmed_date"),
                    "status":                "GAMIFIED_CONFIRMED",
                    "pre_liquidation_check": "Run FanTokenPlayMonitor at T-48h before each match",
                    "path_2_loss_note":      "PATH_2 LOSS is supply-neutral — pre-liquidated amount restored only.",
                    "chz_echo":              "PATH_2 WIN contributes to CHZ ecosystem burn via 10% proceeds rule.",
                    "skill_ref":             "fan-token/gamified-tokenomics-intelligence/",
                    "agent_rule":            "Never treat pre-liquidation as Category 1 distribution signal.",
                }
                if "fan_token_play" in token_data else {
                    "status": "NOT_CONFIRMED",
                    "note":   "Check KAYEN API gamified field. Apply standard signal chain if not confirmed.",
                }
            ),
        },
        "composite_signal": {
            "sms":              sms,
            "sms_tier":         sms_tier,
            "macro_modifier":   round(macro_mod, 2),
            "layers_loaded":    layers,
            "recommended_action": (
                "WAIT" if macro_mod < 0.75 or sms < 60
                else "PROCEED_TO_FULL_ANALYSIS"
            ),
        },
        "skill_references": {
            "fan_sentiment":   "fan-token/fan-sentiment-intelligence/",
            "social_lift":     "fan-token/athlete-social-lift/",
            "brand_score":     "fan-token/brand-score/",
            "token_pulse":     "fan-token/fan-token-pulse/",
            "disciplinary":    "core/athlete-disciplinary-intelligence.md",
            "token_specific":  f"fan-token/{sport}-token-intelligence/",
        },
        "contract_address":  token_data["contract"],
        "chiliscan_url":     token_data["chiliscan"],
        "fantokens_url":     token_data["fantokens"],
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
    }


def tool_verifiable_source(query_type, sport):
    """Return the authoritative source for a query type and sport."""
    sport_slug = sport.replace("-", "_")

    sources_for_type = VERIFIABLE_SOURCES.get(query_type)
    if not sources_for_type:
        available = list(VERIFIABLE_SOURCES.keys())
        return {
            "query_type":      query_type,
            "sport":           sport,
            "found":           False,
            "message":         f"Query type '{query_type}' not in registry.",
            "available_types": available,
            "sportmind_version": VERSION,
        }

    source = (sources_for_type.get(sport_slug) or
              sources_for_type.get(sport.replace("_", "")) or
              sources_for_type.get("default"))

    return {
        "query_type":  query_type,
        "sport":       sport,
        "found":       True,
        "source":      source["source"],
        "tier":        source["tier"],
        "backup":      source["backup"],
        "note":        source.get("note", ""),
        "tier_meaning": {
            1: "Ground truth — always accept",
            2: "Reliable — accept with standard confidence",
            3: "Usable with caution — corroborate before using",
            4: "Do not use as signal input",
        },
        "full_reference": "core/verifiable-sources-by-sport.md",
        "sportmind_version": VERSION,
    }


# ── Tool schemas ───────────────────────────────────────────────────────────────

TOOL_SCHEMAS = {
    "sportmind_signal": {
        "type": "object",
        "properties": {
            "sport":                {"type": "string", "enum": SUPPORTED_SPORTS},
            "event_id":             {"type": "string"},
            "use_case":             {"type": "string", "enum": USE_CASES, "default": "pre_match"},
            "home_team":            {"type": "string"},
            "away_team":            {"type": "string"},
            "include_defi_context": {"type": "boolean", "default": False},
        },
        "required": ["sport"],
    },
    "sportmind_macro": {
        "type": "object", "properties": {}, "required": [],
    },
    "sportmind_stack": {
        "type": "object",
        "properties": {
            "sport":      {"type": "string", "enum": SUPPORTED_SPORTS},
            "use_case":   {"type": "string", "enum": USE_CASES, "default": "pre_match"},
            "compressed": {"type": "boolean", "default": False},
        },
        "required": ["sport"],
    },
    "sportmind_verify": {
        "type": "object",
        "properties": {
            "skill_id": {"type": "string"},
            "content":  {"type": "string"},
        },
        "required": ["skill_id", "content"],
    },
    "sportmind_agent_status": {
        "type": "object",
        "properties": {
            "agent_id":           {"type": "string"},
            "include_audit_log":  {"type": "boolean", "default": False},
            "last_n_cycles":      {"type": "integer", "default": 5},
        },
        "required": [],
    },
    "sportmind_pre_match": {
        "type": "object",
        "properties": {
            "sport":       {"type": "string", "enum": SUPPORTED_SPORTS},
            "home_team":   {"type": "string"},
            "away_team":   {"type": "string"},
            "competition": {"type": "string"},
            "kickoff":     {"type": "string", "description": "ISO-8601 datetime"},
            "use_case":    {"type": "string", "enum": USE_CASES, "default": "pre_match"},
        },
        "required": ["sport"],
    },
    "sportmind_disciplinary": {
        "type": "object",
        "properties": {
            "player":             {"type": "string"},
            "sport":              {"type": "string", "enum": SUPPORTED_SPORTS},
            "club":               {"type": "string"},
            "include_framework":  {"type": "boolean", "default": False,
                                   "description": "Include DSM framework excerpt in response"},
        },
        "required": ["sport"],
    },
    "sportmind_fan_token_lookup": {
        "type": "object",
        "properties": {
            "query":            {"type": "string",
                                 "description": "Club name, token ticker (e.g. BAR, PSG), or sport name"},
            "include_registry": {"type": "boolean", "default": False,
                                 "description": "Include full registry in response"},
        },
        "required": ["query"],
    },
    "sportmind_sentiment_snapshot": {
        "type": "object",
        "properties": {
            "token":    {"type": "string",
                         "description": "Fan token ticker (e.g. BAR, PSG, CITY) or club name"},
            "use_case": {"type": "string", "enum": USE_CASES, "default": "fan_token_tier1"},
        },
        "required": ["token"],
    },
    "sportmind_verifiable_source": {
        "type": "object",
        "properties": {
            "query_type": {
                "type": "string",
                "enum": ["lineup_confirmation", "match_result", "disciplinary_ban",
                         "player_stats", "transfer_news", "rankings"],
                "description": "Type of information to verify",
            },
            "sport": {"type": "string", "enum": SUPPORTED_SPORTS},
        },
        "required": ["query_type", "sport"],
    },
}

TOOL_DESCRIPTIONS = {
    "sportmind_signal": (
        "Generate a SportMind pre-match intelligence signal. Returns direction, "
        "adjusted_score, SMS, and modifiers. Call sportmind_macro first for fan "
        "token or DeFi applications."
    ),
    "sportmind_macro": (
        "Get the current SportMind macro state: crypto cycle phase, macro_modifier, "
        "and active events. Always call before fan token analysis."
    ),
    "sportmind_stack": (
        "Load the full SportMind intelligence stack for a sport in correct loading "
        "order: macro → market → domain → athlete → fan-token."
    ),
    "sportmind_verify": (
        "Verify SportMind skill content integrity via SHA-256 against "
        "platform/skill-hashes.json. Use in security-sensitive deployments."
    ),
    "sportmind_agent_status": (
        "Get the operational status of running SportMind autonomous agents. "
        "Requires a running agent instance — see core/autonomous-agent-framework.md."
    ),
    "sportmind_pre_match": (
        "Orchestrated full pre-match reasoning package. Combines sport domain signal, "
        "macro state, availability check source, disciplinary reminder, narrative "
        "momentum reference, and statistical reasoning reference in one call. "
        "Use instead of manually sequencing macro + signal + stack."
    ),
    "sportmind_disciplinary": (
        "Disciplinary intelligence check for a player and sport. Returns DSM framework "
        "(MINIMAL/MODERATE/SEVERE/CATASTROPHIC), regulatory source to check, active "
        "flags to set, and commercial recommendation rule. Requires live regulatory "
        "source check for current player status."
    ),
    "sportmind_fan_token_lookup": (
        "Resolve a club name, token ticker, or sport to its Chiliz Chain fan token "
        "context. Returns contract address, chain ID 88888, chiliscan verification "
        "link, fantokens.com market data link, market cap tier, and recommended "
        "SportMind skill stack. Registry covers 24 verified tokens."
    ),
    "sportmind_sentiment_snapshot": (
        "Multi-axis sentiment state for a fan token. Returns macro sentiment, and "
        "references for fan sentiment phase, social lift, commercial sentiment, and "
        "disciplinary status — with the composite signal and recommended next action. "
        "Use before any fan token commercial recommendation."
    ),
    "sportmind_verifiable_source": (
        "Return the authoritative source for a specific query type and sport. "
        "Covers: lineup_confirmation, match_result, disciplinary_ban, player_stats, "
        "transfer_news, rankings. Returns source name, tier (1=ground truth to "
        "4=do not use), backup source, and reference to verifiable-sources-by-sport.md."
    ),
}


# ── MCP Server ─────────────────────────────────────────────────────────────────

async def _handle_tool(name: str, arguments: dict):
    """Dispatch tool calls to implementations."""
    if name == "sportmind_signal":
        return tool_signal(
            sport        = arguments.get("sport", "football"),
            event_id     = arguments.get("event_id", ""),
            use_case     = arguments.get("use_case", "pre_match"),
            home_team    = arguments.get("home_team", ""),
            away_team    = arguments.get("away_team", ""),
            include_defi = arguments.get("include_defi_context", False),
        )
    elif name == "sportmind_macro":
        return tool_macro()
    elif name == "sportmind_stack":
        return tool_stack(
            sport      = arguments.get("sport", "football"),
            use_case   = arguments.get("use_case", "pre_match"),
            compressed = arguments.get("compressed", False),
        )
    elif name == "sportmind_verify":
        return tool_verify(arguments["skill_id"], arguments["content"])
    elif name == "sportmind_agent_status":
        return tool_agent_status(
            agent_id     = arguments.get("agent_id", ""),
            include_audit= arguments.get("include_audit_log", False),
            last_n       = arguments.get("last_n_cycles", 5),
        )
    elif name == "sportmind_pre_match":
        return tool_pre_match(
            sport       = arguments.get("sport", "football"),
            home_team   = arguments.get("home_team", ""),
            away_team   = arguments.get("away_team", ""),
            competition = arguments.get("competition", ""),
            kickoff     = arguments.get("kickoff", ""),
            use_case    = arguments.get("use_case", "pre_match"),
        )
    elif name == "sportmind_disciplinary":
        return tool_disciplinary(
            player            = arguments.get("player", ""),
            sport             = arguments.get("sport", "football"),
            club              = arguments.get("club", ""),
            include_framework = arguments.get("include_framework", False),
        )
    elif name == "sportmind_fan_token_lookup":
        return tool_fan_token_lookup(
            query            = arguments.get("query", ""),
            include_registry = arguments.get("include_registry", False),
        )
    elif name == "sportmind_sentiment_snapshot":
        return tool_sentiment_snapshot(
            token    = arguments.get("token", ""),
            use_case = arguments.get("use_case", "fan_token_tier1"),
        )
    elif name == "sportmind_verifiable_source":
        return tool_verifiable_source(
            query_type = arguments.get("query_type", ""),
            sport      = arguments.get("sport", "football"),
        )
    else:
        return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool, TextContent
    except ImportError:
        print("ERROR: pip install mcp aiohttp", flush=True)
        return

    server = Server("sportmind")

    @server.list_tools()
    async def list_tools():
        return [
            Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n])
            for n in TOOL_SCHEMAS
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        result = await _handle_tool(name, arguments)
        from mcp.types import TextContent
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    async with stdio_server() as streams:
        await server.run(*streams, server.create_initialization_options())


async def run_http(port: int):
    try:
        from mcp.server import Server
        from mcp.server.sse import SseServerTransport
        from mcp.types import Tool, TextContent
        from aiohttp import web
    except ImportError:
        print("ERROR: pip install mcp aiohttp", flush=True)
        return

    server = Server("sportmind")

    @server.list_tools()
    async def list_tools():
        return [
            Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n])
            for n in TOOL_SCHEMAS
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        result = await _handle_tool(name, arguments)
        from mcp.types import TextContent
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    transport = SseServerTransport("/mcp")

    async def handle_sse(request):
        async with transport.connect_sse(request.headers, request) as streams:
            await server.run(*streams, server.create_initialization_options())

    async def handle_health(request):
        return web.Response(
            content_type="application/json",
            text=json.dumps({
                "status":    "ok",
                "service":   "SportMind MCP Server",
                "version":   VERSION,
                "tools":     list(TOOL_SCHEMAS.keys()),
                "tool_count": len(TOOL_SCHEMAS),
                "timestamp": now_iso(),
            }, indent=2),
        )

    app = web.Application()
    app.router.add_get("/mcp",    handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/",       handle_health)

    print(f"SportMind MCP Server v{VERSION}", flush=True)
    print(f"MCP endpoint:  http://localhost:{port}/mcp",    flush=True)
    print(f"Health check:  http://localhost:{port}/health", flush=True)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Server running on port {port}. Ctrl+C to stop.", flush=True)
    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="SportMind MCP Server — sports intelligence for AI agents"
    )
    parser.add_argument("--http",  action="store_true",
                        help="Run HTTP/SSE server (default: stdio)")
    parser.add_argument("--port",  type=int, default=3001,
                        help="HTTP port (default: 3001)")
    args = parser.parse_args()

    if args.http:
        asyncio.run(run_http(args.port))
    else:
        asyncio.run(run_stdio())
