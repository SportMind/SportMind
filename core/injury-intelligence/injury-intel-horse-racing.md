# Injury Intelligence — Horse Racing

Sport-specific injury intelligence for horse racing. Applies the core framework from
`core/injury-intelligence/core-injury-intelligence.md` to horse racing's unique dynamics
where the athlete is the horse, not the jockey.
Load both files for full horse racing injury intelligence.

---

## The fundamental difference: the horse IS the athlete

In every other sport in this library, injury intelligence focuses on a human athlete
and what their absence means for the team or event. In horse racing, the horse is
the athlete — and horse injuries are in a category of their own:

- Horses cannot communicate discomfort or pain until it becomes observable behaviour
- A horse that "breaks down" mid-race (bone fracture under race conditions) is not just
  a racing withdrawal — it is often a life-threatening event requiring immediate
  veterinary intervention and potentially euthanasia
- Horses cannot consent to treatment or retirement; the trainer, owner, and vet
  make all decisions
- The window between "horse appears fine" and "horse has a serious injury" can be
  hours or days — far more compressed than human sports
- Form reversal in horse racing is frequently injury-related, even when no injury
  is officially announced

---

## Pre-race injury signal hierarchy

### Veterinary inspection signals

```
PRE-RACE VET CHECKS (mandatory at major meetings):
  All runners at major meetings (Cheltenham, Grand National, Royal Ascot, Breeders' Cup)
  undergo pre-race veterinary inspection.
  
  VET WITHDRAWAL: Horse fails pre-race inspection → withdrawn
    Signal: Significant issue detected. Horse typically re-examined before next race.
    Agent action: If invested in this horse's token/prediction, exit immediately.
    
  VET PASSED BUT OWNER/TRAINER WITHDRAWS: Voluntary withdrawal despite vet clearance
    Signal: Connections not satisfied with horse's condition.
    Far more informative than trainer stating "ground not suitable" (common cover story).
    Agent action: Flag this horse for next 2 races — issue may persist.
```

### Morning workout signals

```
MORNING GALLOPS / TRACKWORK:
  The most important pre-race signal available. Trainers monitor morning exercise
  closely. Public access is limited but several data points are available:
  
  Training times (published by racecourses and form databases):
    Faster than expected for the grade: strong preparation
    Significantly slower than recent workouts: trainer managing a problem
    Very short work (2-3 furlongs vs typical 4-6): protecting the horse
    
  Trainer descriptions of morning work:
    "Worked nicely this morning" → Normal; positive
    "Had an easy piece of work" → Conservation; possible concern
    "We kept him quiet" → Managing something
    "Working well at home" (without track work) → Avoiding public trackwork
    
  Absence from trackwork:
    Horse expected at gallops but not appearing: serious flag
    First absence before a major race: investigate urgently
```

### Paddock and pre-race visual assessment

The paddock walk (parade ring) is the last observable window before a race.
Experienced observers can detect injury signals that official sources don't disclose:

```
POSITIVE PHYSICAL SIGNALS:
  Moving freely, even stride length on all four legs
  Alert, engaged with environment (ears forward, eyes bright)
  Good coat condition, well-muscled, appropriate weight
  Relaxed sweat pattern (light sweat = normal pre-race activation)
  
NEGATIVE PHYSICAL SIGNALS — act on any of these:

  GAIT ABNORMALITIES:
    Any shortness of stride in one leg → lameness
    Head-nodding while walking → front leg lameness (front leg on nodding side is lame)
    Hip drop while walking → hindlimb lameness
    Stiffness or reluctance to turn in tight circles → back or pelvis issue
    
  BEHAVIOURAL SIGNALS:
    Excessive sweating on cold day (not effort-based) → pain or anxiety/distress
    Repeatedly turning head to look at flank → colic risk (gut pain)
    Refusing to enter the parade ring → pain threshold breached
    Reluctance to load into stalls → fear, pain, or both
    
  PHYSICAL APPEARANCE:
    Asymmetrical muscle development (one side vs other) → chronic one-sided issue
    Swelling on any leg joint → inflammation, possibly active injury
    Any visible bandaging / support boot on race day beyond standard:
      Front legs: hoof, fetlock, or tendon protection
      Hind legs: splint, check ligament, or hock issue
    Discharge from nose or eye → respiratory or systemic illness
```

---

## Injury types in horse racing

### Catastrophic race day injuries
```
BONE FRACTURES UNDER RACE CONDITIONS (highest risk at jumps racing):
  Foreleg fractures (fetlock, cannon bone, coffin bone): most common catastrophic
  Pelvic fractures: rare but immediately life-threatening
  Spinal injuries from falls (jumps racing): career/life-ending
  
  Agent rule: When a horse breaks down in a race, all prediction positions on that
  race become null. If horse racing tokens exist, expect significant negative price
  movement regardless of other results.
  
TENDON AND LIGAMENT INJURIES:
  Suspensory ligament: most common career-altering soft tissue injury
    Recovery: 6–18 months
    Recurrence: very high (30–50%) — career-threatening on second occurrence
  Flexor tendon (deep/superficial): serious, career-altering
    Recovery: 12–18 months
    Recurrence: high
    
  These injuries are often preceded by a subtle but detectable performance change
  in the 1–3 races before the acute injury occurs.
```

### Career-altering but recoverable
```
HOOF INJURIES:
  Foot abscess: most common; 1–4 weeks
  Laminitis: more serious; 4–16 weeks depending on severity
  Bruised sole: 1–3 weeks
  Hoof crack: ongoing management required
  
RESPIRATORY CONDITIONS:
  "Bleeding" (EIPH — Exercise Induced Pulmonary Haemorrhage):
    Horse bleeds from lungs during high-intensity exercise
    Treated with Lasix (furosemide) — controversial, banned in some jurisdictions
    Horse history of bleeding = structural risk at maximum effort
    
  Viruses and respiratory illness:
    Very contagious in racing yards
    "Something going through the yard" is common trainer language for viral outbreak
    Agent rule: If trainer mentions yard-wide illness, apply × 0.88 to all
    runners from that yard until recovery confirmed (typically 2–4 weeks)
    
BACK AND MUSCULOSKELETAL:
  Back pain / kissing spine: 4–12 weeks
  Muscle soreness / azoturia (tying up): 1–2 weeks
  Bone chip (joint): variable — may require surgery
```

---

## Post-race injury signals

Some injuries only become apparent after racing. The post-race period is informative:

```
IMMEDIATE POST-RACE:
  Horse not pulling up well after race → unusual fatigue or injury onset
  Jockey reporting "not themselves" or "didn't travel like usual" → flag next start
  Vet examination requested post-race → investigate; may be precautionary
  
DAYS AFTER RACE:
  Horse "stiff the morning after" → muscle soreness (common); usually clears
  Yard worker social media showing horse standing unusually → potential injury
  Training posts absent for 2+ weeks after race → more than standard recovery
  
RETURNING FROM A LONG ABSENCE (60+ days):
  Apply return-to-run curve: first race back from significant rest:
    Fitness: 85–90% of peak
    Match sharpness: 80–90% of peak
    Finishing ability: × 0.90 for first run back
    Second run: × 0.97 (usually fit and ready)
    Third run: × 1.00 (full condition restored)
```

---

## Trainer and owner intelligence

Trainer language is the most important human signal in horse racing injury intelligence.
Trainers walk a fine line between transparency and protecting their horses' market value.

```
TRAINER LANGUAGE DECODER:

"Fit and well" → Standard; no specific positive or negative
"He came out of his last race well" → Normal recovery; positive
"We've had him on the easy list" → Management period; possible minor issue
"Saved him for this" → Targeted preparation; positive if specific race is mentioned
"He needed that run" → Was not 100% fit; next run better
"Slight setback but fine now" → Real issue occurred; resolved (assess severity)
"We had to be patient with him" → Injury recovery took time
"He's not 100% but we're running" → Explicitly not fully fit → apply × 0.85 minimum
"Ground came up too firm/soft" (after poor performance) → Often not the real reason
                                                            → Genuine excuse OR covering injury
"We'll find out more about him today" → Unknown fitness; high variance race
"This is his prep run for X" → Today's race is secondary; fitness not maximised

WITHDRAWAL LANGUAGE:
"Bit of heat in a leg" → Swelling / inflammation; scratch probably correct
"Vet's advice" → Medical recommendation; not racing fitness
"Connections not happy" → Connections detected something; precautionary
"Ground conditions" → Legitimate OR cover for injury concern
  → Check if horse ran on similar ground previously (if yes, probably an excuse)
```

---

## Going (ground conditions) and injury interaction

Ground conditions in horse racing directly affect injury probability, not just performance:

```
FIRM/HARD GROUND:
  Increased bone concussion → higher fracture risk for horses with previous bone issues
  Particularly dangerous for: horses with splints, bone chips, past stress fractures
  High-risk horses on firm: apply × 0.90 for injury probability assessment
  
VERY SOFT / HEAVY GROUND:
  Increased tendon and ligament strain → higher soft-tissue injury risk
  Energy expenditure increases 15–25% (dragging through deep ground)
  High-risk horses on heavy: horses with past tendon issues → × 0.85 for completion
  
GOOD GROUND:
  Optimal condition; baseline injury probability
  
CHANGING CONDITIONS MID-RACE (rain during event):
  Creates variable going that amplifies fatigue-related injury risk
  Jumps racing particularly affected (take-off on firm, land on soft = inconsistent)
```

---

## Jockey signals

While the horse is the athlete, jockey condition and confidence provide secondary signals:

```
JOCKEY INJURY / REPLACEMENT:
  Champion/established jockey replaced by conditional (apprentice):
    RQD 0.15–0.25 depending on race type
    Conditional jockeys less effective in tight finishes
    Flat racing impact: moderate
    Jumps racing impact: more significant (experience in traffic, at fences)
    
  Jockey change without explanation:
    Established jockey booking → different booking → flag
    May indicate trainer concern about horse's readiness OR internal arrangement
    Often a very subtle but accurate signal
    
  Jockey losing claim (weight allowance):
    Conditional loses their allowance → slightly higher weight carried
    Minor but meaningful in handicaps (horse now carries true weight)
    
JOCKEY RIDING PATTERN:
  Experienced jockey riding notably out of system:
    Taking horse back further than usual → protecting horse from interference
    Pushing early rather than waiting → knows horse may not stay
    Both: may indicate trainer instruction based on horse's condition
```

---

## Injury intelligence integration with predictions

```
INJURY-ADJUSTED RACE ASSESSMENT WORKFLOW:

1. Check overnight declarations: any withdrawals from the field?
   (Reduce field quality assessment for remaining runners)
   
2. Check morning gallops reports: any abnormal workout times?

3. At declarations close: has the horse been declared fit and well?

4. On race day — paddock assessment window:
   Use visual checklist above. Flag any gait or behavioural signal.
   
5. Pre-race market movement:
   Strong late shortening = connections confident
   Drifting in market despite no obvious reason = stable concern leaked
   
6. Apply return-to-run curve if horse has been absent 60+ days

7. Check yard illness context: any reports of virus going through stable?

8. Apply ground conditions injury modifier if extreme going
```

---

## Data sources

- **Racing Post**: Most comprehensive UK/Ireland form and trainer comment database
- **At The Races / Racing TV**: Morning workout reports and paddock commentary
- **Timeform**: Historical form ratings and physical assessments
- **BHA / IHRB / racing authority injury reports**: Official veterinary withdrawals
- **Trainer social media**: Instagram and X for stable condition updates
- **Bloodstock.com / breeding data**: Physical background and family injury history

---

*MIT License · SportMind · sportmind.dev*
