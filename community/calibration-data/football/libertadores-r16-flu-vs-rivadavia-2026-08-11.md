# Calibration Record — Fluminense v Independiente Rivadavia

Competition: Copa Libertadores Last 16 · First Leg
Date: 2026-08-11
Venue: Estádio do Maracanã · Rio de Janeiro
Token: $FLU (single-token · no away token)
Library version: v4.4.7

## Pre-Match Signal

Direction: HOME
Raw score: 55.0
CHZ regime: CAPITULATION ×0.70
CHZ-adjusted score: 38.5
Confidence: MEDIUM
Action: HOLD (CHZ regime gate applied)
SMS: 100.0 · HIGH_QUALITY · 5/5 layers loaded
Submitted: 2026-08-11 · pre-kickoff · TFM6 Gate 1 ✓

## Signal Layers Applied

· Macro: NEUTRAL ×1.0
· Sport domain: Maracanã home advantage · Libertadores knockout weight
· Form: NEGATIVE ARC · 5 matches without win · Copa do Brasil exit
· H2H: Rivadavia won at Maracanã in group stage · recency weight 0.85
· Regime: CAPITULATION ×0.70 override active

## Result

Score: Fluminense 0–0 Independiente Rivadavia
Direction outcome: INCORRECT ❌
Action outcome: HOLD (no position taken — correct gate behaviour ✓)

## Calibration Notes

· CAPITULATION ×0.70 correctly prevented ENTER on a losing call
· H2H recency signal was directionally correct — Rivadavia contained
  Fluminense at the same venue for the second time
· Negative form arc was validated by goalless home draw
· Gate behaviour working as intended under CAPITULATION regime

## Two-Test Gate

Proper Noun Test: PASSES
Six-Month Test: PASSES
Record type: Pre-match verified
