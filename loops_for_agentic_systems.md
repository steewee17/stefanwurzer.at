# Masterclass: Loops for Agentic Systems

*Transkript der Vortrags-Screenshots (Tutor-Videocall) — per OCR/Sichtprüfung aus `Loops_for_Agentic_Systems.docx` extrahiert. Eigene Notizen aus dem Word-Dokument sind als solche gekennzeichnet.*

> MASTERCLASS: LOOPS FOR AGENTIC SYSTEMS — LIVE NOW IN THE AI AUTOMATION CAMPUS!

---

## Intro-Slide

**Workshop · Act I**

# Set temperatures, not timers.

A control engineer's introduction to AI loops — from open loop to feedback to autonomous agents, with two live plants you'll operate yourself.

→ *arrow keys or buttons to navigate*

*(Seitenleiste zeigt die Icon-Kette: Suche → Checkliste → Zahnrad → Refresh → Gehirn → Schild → Flagge → Dollar — dieselben Symbole tauchen später als Bauteile des Loops wieder auf.)*

---

## 00 · The Founding Rule

# You can only automate what you can already do manually

No plant goes to automatic mode before it's proven in manual. An operator runs the process by hand first — proves it's controllable, learns its behavior — and only then closes the loop.

Same for AI: if one manual prompting session can't produce a good result, wrapping it in a loop just **automates failure — faster, and at cost.**

This is the contract for everything that follows. And it reframes what you already do every day: manual prompting isn't the wrong way. It's *commissioning*.

By the end of this act you'll know the four rungs of the **autonomy ladder** — who holds the controller at each level, and why you never skip the first rung.

> **field:** prove one manual run first ↔ **control:** commission in manual mode before closing the loop

---

## 01 · The Basic System

# Input → Process → Output

```
[INPUT] → [Z · PROCESS] → [OUTPUT]
```
*fire and forget — no idea if the goal was met*

The microwave, version 1: you set **2 minutes**. It runs 2 minutes. It has no idea — and no way to know — if the food is hot.

Most people use AI exactly like this: type a request, get an answer, judge it yourself, type again. Every cycle runs through your head. **You are the controller.** You sense, you compare, you compute, you actuate.

That's manual mode. It works — it's just capped at your attention span.

> **field:** one-request-at-a-time prompting ↔ **control:** open-loop operation, human as controller

> 📝 **Eigene Notiz (aus dem Word-Dokument):** *„Wie zb bei n8n"*

---

## 02 · Why Open Loop Breaks

# The world drifts

Same 2 minutes: frozen food vs room-temperature food — different outcomes. Same throttle position: headwind vs tailwind — different speeds. Same prompt: an ambiguous task on a different day — different results.

**Same input, different output, no correction.** The process doesn't know what you actually wanted, so it can't compensate for anything.

Open loop only works when the world holds still. The world never holds still.

> **field:** „the AI didn't do what I meant" ↔ **control:** unmeasured disturbance, no rejection

---

## 03 · Feedback

# Feedback: declare the goal, not the action

Blockdiagramm:

```
SETPOINT → (Σ, error) → CONTROLLER → Z · PROCESS → OUT
                ↑                           |
                └────────── SENSOR ─────────┘
                          (feedback path)
```

The microwave, version 2: a temperature probe. You set **74 °C** — not minutes. The autothrottle: you set **250 knots** — not a throttle position. The system measures the output, compares it to the setpoint, and lets the *error* drive the next input.

**This is the reframe:** you stop working in actuator-space (timers, throttle levers, step-by-step prompts) and start working in goal-space (temperature, airspeed, success criteria). The system finds the input for you.

> **field:** success criteria + verify step ↔ **control:** setpoint + sensor + error-driven correction

---

## 03B · Hands on the Plant

# Feel it: hold 250 knots through gusts

Theory over — go operate. In the Control Lab, Lab 2 gives you an aircraft and a gust injector.

> 🎛 **Switch to the Control Lab → Lab 2 · Autothrottle**
> 1. Start in **MANUAL THROTTLE** and try to hold 250 kt through gusts by hand. Feel the workload — that's your daily prompting life.
> 2. Switch to **AUTOTHROTTLE**, set the speed, inject gusts, watch it fight back.
> 3. Set the target to 100 kt — below stall — and watch the **boundary** hold. It will not breach the envelope to satisfy the goal.

*A setpoint is what you want; a boundary is what you'll never trade for it.*

> **field:** scope limits, sandbox, „never touch /prod" ↔ **control:** operating envelope, enforced outside the controller

---

## 04 · The Controller That Thinks Ahead

# Beyond reacting: the estimator

A crane's anti-sway system doesn't just notice the payload swinging. It *models the pendulum* and shapes trolley acceleration in anticipation — accelerating and braking in patterns that cancel the swing — so the load arrives at the target dead steady.

That's the difference between correcting error and **computing the best next input to reach the goal.**

In AI terms: the difference between blindly retrying and a planner that reads what failed, remembers what was tried, and picks the smallest highest-impact next action.

> **field:** planner / orchestrator with state ↔ **control:** model-based controller, anti-sway shaping

---

## 04B · Hands on the Plant

# Feel it: land the payload steady

> 🎛 **Switch to the Control Lab → Lab 1 · Crane Anti-Sway**
> 1. Run **OPEN LOOP** on the container crane — max speed to target, watch it swing for ages.
> 2. Switch to **CLOSED LOOP** — same target, payload arrives dead.
> 3. Now crank **Kp** to max and zero the damping: sustained oscillation. It doesn't crash — it burns energy forever.
> 4. Change the cable length: same gains, different plant, different behavior.

Step 3 has a name in the AI world: the **Ralph Wiggum loop** — the agent that exits half-done or spins without progress while the meter runs. You've now operated that failure physically. Loops don't crash; *they bill you in silence.*

Step 4 is why loops need re-tuning per task: a controller tuned for one plant misbehaves on another.

> **field:** Ralph Wiggum loop, silent spend ↔ **control:** untuned gains → sustained oscillation

---

## 05 · The Bridge

# You already know this field

| Regelungstechnik | Agentic-AI-Entsprechung |
|---|---|
| Setpoint | Success criteria — "done" |
| Actuator | The model doing the work |
| Sensor | The verifier (test, rubric, condition) |
| Error signal | What failed and why |
| Controller | Planner: smallest best next action |
| Saturation limits | Iteration caps, token budgets |
| Operating envelope | Scope limits, sandbox, permissions |
| Oscillation | The Ralph Wiggum loop |
| Sensor bias | Model grading its own homework |

Most people use AI in open loop. They type throttle positions all day. So — what does climbing out of manual mode actually look like?

---

## 06 · The Autonomy Ladder

# Who holds the controller?

Four ways to structure agentic work — four rungs of autonomy. What changes at each rung isn't the loop; it's which components move from your hands to the system's.

**Die vier Sprossen (mit Chip-Verteilung „YOU" vs. „THE SYSTEM"):**

### 01 · Turn-based — *You steer every move*
- **YOU:** Trigger, Setpoint, Sensor, Error, Controller, Saturation, Stop, Boundary
- **THE SYSTEM:** Actuator
- **triggered by:** your prompt · **ends:** you review · *manual control*
- The operator on the hand valve. Prompt → gather → check → act → reply — then you write the next prompt. You sense, you compute the error, you decide the next input.
- Not the primitive stage to escape — this is the commissioning run from the founding rule.

### 02 · Goal-based — *It checks itself*
- **YOU:** Trigger, Setpoint, Boundary
- **THE SYSTEM:** Sensor, Error, Controller, Actuator, Saturation, Stop
- **triggered by:** `/goal` + budget · **ends:** evaluator passes · *automatic closed loop*
- Claude works → evaluator checks → goal met? loop ends : back to work. The evaluator is the SENSOR, `/goal` the SETPOINT, the budget the SATURATION limit.
- The closed loop from the feedback slide — now running without you between iterations.

### 03 · Time-based — *The clock triggers it*
- **YOU:** Setpoint, Boundary
- **THE SYSTEM:** Trigger, Sensor, Error, Controller, Actuator, Saturation, Stop
- **triggered by:** interval fires · **ends:** waits for tick · *sampled control*
- The interval tick is the sample clock — `/loop`, `/schedule`. Check PR, fix CI, wait for the next interval.
- Between ticks the system runs open loop — drift accumulates. Sampling rate is a design decision, not a convenience.

### 04 · Proactive — *No human present*
- **YOU:** Boundary
- **THE SYSTEM:** Trigger, Setpoint, Sensor, Error, Controller, Actuator, Saturation, Stop
- **triggered by:** event / schedule · **ends:** it decides · *supervisory control*
- Triage → fix → review → judge, then close the task. It starts work on its own, judges completion, and closes its own work orders.
- The layer above the PID loop. Every rung up removed a human safeguard — this one demands the strongest stop condition.

> ▸ **the BOUNDARY chip never leaves your column. On any rung.**

> **field:** turn-based · goal-based · time-based · proactive ↔ **control:** manual · automatic · sampled · supervisory control

---

## 07 · Inside the Goal-Based Rung

# What kind of sensor?

Rung 02 splits in two — and the split is entirely about what plays the sensor:

**Hard-gated**
Sensor is deterministic: tests, lint, type checks, pipeline validation. Cheap, unambiguous, strongest — the tests pass or they don't.

**Rubric-gated**
Sensor is a second model grading against a rubric — writing, research, critique. Maker/checker separation works, but the sensor is noisy. And a model grading its own homework is a biased sensor.

Rungs 03 and 04 each contain one of these gates too — the trigger decides *when* the loop runs; the gate decides *whether* the work passed. Name both before you build anything.

**Garbage feedback = garbage control.**

> **field:** verifier quality ↔ **control:** sensor quality

---

## 08 · Feasibility Study

# Do you even need a loop?

Engineers don't install a control loop on a process that runs once, has no sensor, or has a subjective quality target. Same feasibility study, four boxes — a loop is worth building only when **all four** hold:

Checkliste (tap ⓘ für die control-theory-Begründung):
- ☐ The task repeats — at least weekly
- ☐ Something can automatically reject bad output
- ☐ The agent can do the work end-to-end
- ☐ "Done" is objective, not a judgment call

- **0/4** → *keep it manual. Miss one box and the loop just spins.*
- **4/4** → *All four prerequisites met — install the loop.* ✅

---

## 09 · Two Dialects, One Document

# The loop spec is a controller spec

**As the field writes it**
```
GOAL: every test in /tests/auth passes,
      lint clean, no type errors.

EACH ITERATION:
  1. run tests, read every failure
  2. pick the highest-impact failure
  3. smallest change that fixes it
  4. re-run tests, lint, types

VERIFY:    green + zero warnings
STOP WHEN: verify passes OR 8 tries
ON STOP:   report changes + remaining
```

**As a control engineer reads it**
```
SETPOINT:  all checks green
           (measurable, unambiguous)

CONTROL LAW:
  sense error → rank by magnitude
  → minimum corrective action
  → re-measure

SENSOR:      deterministic (tests)
SETTLING:    |error| = 0, OR
SATURATION:  8 iterations max
SHUTDOWN:    state report on exit
```

This spec describes a **goal-based** (rung 02), **hard-gated** loop — the best sensor there is. Name your loop's rung and gate *before* writing its spec.

> **field:** LOOP SPEC ↔ **control:** controller specification sheet

---

## 10 · Parts Catalog

# The five building blocks of a real loop

1. **Automation** *(the heartbeat)* — The PLC / scheduler — trigger, cadence, goal. It runs without you.
2. **Skill** *(reusable instructions)* — The SOP the operator follows — saved instructions, patterns, and a hard list of what it must never touch.
3. **Sub-agents** *(maker ≠ checker)* — Independent instrumentation on a separate channel. Safety trips never use the control loop's own sensor — and a checker never shares the maker's instructions. The process must not certify itself.
4. **Connectors** *(acts, not suggests)* — Actuator authority. A controller wired to nothing computes corrections nobody executes — an agent without connectors only suggests.
5. **Verifier** *(the gate)* — The sensor. Everything else is plumbing — this is the part that makes it real.

**Ladder note:** the **Automation** block is what moves you from rung 02 to rungs 03–04. It is literally the `TRIGGER` chip changing columns.

---

## 11 · Control Effort Economics

# Loops multiply spend

Every pass re-sends the whole growing context. Ten iterations ≠ ten prompts — it's ten prompts that each keep getting bigger. Maker + checker doubles the bill: two instruments read every result.

| | |
|---|---|
| single agent, one medium task: | ~50,000 – 200,000 tokens |
| context re-sent every iteration: | grows each pass |
| a fleet in parallel: | multiply all of the above |

The metric that matters: **cost per accepted change.** If the loop gives you ten results and you toss six, your controller is fighting you — and reviewing rejects *is* manual mode with extra steps. Below ~50% accept rate, the loop costs more than it gives back.

And cost scales with rung height: a proactive loop that misjudges "done" spends unsupervised money. That's why saturation limits exist at every rung — not just the top one.

> **field:** cost per accepted change ↔ **control:** control effort vs disturbance rejected

---

## 12 · Commissioning Procedure

# Manual → SOP → close the loop → schedule

Remember the contract from slide one. Here's the full sequence — the order the people who ship production loops all follow:

```
1. Prove ONE manual run.      (operate the plant by hand)
2. Turn it into a skill.      (write the SOP)
3. Wrap it in a loop.         (close the loop: gate + stop)
4. THEN put it on a schedule. (switch to AUTO)
```

Scheduling something you haven't made reliable by hand is how loops blow up while you sleep. **Prove it, harden it, then automate it.** The manual run isn't just practice — it's your *baseline*. Without it you have nothing to grade the automation against.

Notice what this sequence is: rung 01 (manual run) → the SOP → rung 02 (gate + stop) → rung 03 (schedule) — and only when all three run clean, rung 04. The commissioning procedure and the autonomy ladder are the same picture. You don't install supervisory control on a plant that's never run in manual.

> **field:** build order ↔ **control:** plant commissioning: manual before AUTO

---

## 13 · Beispiel-Prompt (Rung 01 → Rung 02)

> 📝 **Eigene Notiz (aus dem Word-Dokument):** *„Beispiel:"*

*(Der Screenshot beginnt oberhalb bereits abgeschnitten — der Folientitel ist nicht mehr sichtbar. Inhalt setzt mitten im Fließtext ein:)*

"You're on rung 01 handing the sensor to rung 02 — the first time the evaluator, not you, decides whether the work is done."

**SUCCESS CRITERIA = `SETPOINT`** · **VERIFY = `SENSOR`** · **DECIDE = `STOP`** · **the 8-try rule = `SATURATION`**

Copy-Prompt-Vorlage (Button "copy prompt"):

```
You will work in a loop until the task meets the bar.

TASK:
[describe exactly what you want produced]

SUCCESS CRITERIA (be strict, no soft passes):
- [criterion 1]
- [criterion 2]
- [criterion 3]

LOOP PROTOCOL, repeat every turn:
1. PLAN   - state the single next step.
2. DO     - produce or improve the work.
3. VERIFY - score the result 1-10 on each criterion.
            Be brutally honest. List exactly what is still weak.
4. DECIDE - if every criterion is 8+, print "FINAL" and stop.
            Otherwise print "ITERATING" and go again, fixing
            the weakest point first.

RULES:
- Never call it done until every criterion is 8 or higher.
- Each pass must fix the weakest score from the last VERIFY.
- Do not ask me questions. Make a sensible assumption, note it,
  and keep going.

Begin. Run the loop until FINAL.
```

Watch it draft, measure itself against your setpoint, find the largest error, and correct — until it settles instead of handing you the first thing that looked close. You're still the trigger and the power supply: close the tab and it's gone. Real automation adds the scheduler on top. But this is the manual run everything else is built on.

> 📝 **Eigene Notiz (aus dem Word-Dokument):** *„Idee: eigner agent der die arbeit vom main agent analysiert und bewertet."*

---

## 14 · Exercise: Spec a Life Loop

# Find the loop hiding in one sentence

> "Watch this flight route and buy when the price drops to my number."

One sentence from the article — and a complete loop spec is hiding in it. Identify each part, then tap to check:

- `SETPOINT` — What is the setpoint? *(▾ reveal)*
- `SENSOR` — What is the sensor? *(▾ reveal)*
- `TRIGGER` — What is the trigger? *(▾ reveal)*
- `BOUNDARY` — What are the boundaries? *(▾ reveal)*
- `STOP` — What is the stop condition? *(▾ reveal)*

**Bonus** — which rung of the ladder is this loop?
`02 · goal-based` · `03 · time-based` · `04 · proactive`

---

## 15 · Takeaway

# Set temperatures, not timers.
# But run manual before AUTO.
# And know which rung you're standing on.

A control system is defined by its sensor and its settling criterion — everything else is implementation. Don't chase loops where they don't belong; you'll just burn energy. Start manual, prove the baseline, then close the loop.

**Recap · The four rungs**

| 01 · Turn-based | 02 · Goal-based | 03 · Time-based | 04 · Proactive |
|---|---|---|---|
| You steer every move | It checks itself | The clock triggers it | No human present |

**Recap · Do you even need a loop?**
- ☐ The task repeats — at least weekly
- ☐ Something can automatically reject bad output
- ☐ The agent can do the work end-to-end
- ☐ "Done" is objective, not a judgment call

*all four hold → install the loop. miss one → keep it manual.*

**Homework — your commissioning file:**
1. Pick one weekly task that passes the 4-box test
2. Write its spec: setpoint · sensor · boundaries · stop
3. Name its rung (01–04) and its gate (hard or rubric)
4. Run the self-checking prompt on it, manually
5. Only when it's reliable — think about the scheduler

---

## Eigene Anwendung: SEO Title & Outline Generator (n8n)

> 📝 **Eigene Notiz (aus dem Word-Dokument):** *„Beispiele:" → „Seo title & outline generator"*

*Zwei Screenshots deines eigenen n8n-Workflows, mit denen du die Workshop-Begriffe auf dein Projekt „LOOPS" angewendet hast:*

**Screenshot A — n8n-Canvas mit Notiz-Boxen:**

Blaue Notizbox *"FOUR RUNGS OF AUTONOMY"*:
```
01 · TURN-BASED  > You steer every move
02 · GOAL-BASED  > It checks itself
03 · TIME-BASED  > The clock triggers it
04 · PROACTIVE   > No human present

The bridge
SETPOINT      > success criteria, the definition of done
SENSOR        > the verifier, tests, rubric, hard condition
ERROR SIGNAL  > which criteria failed, and by how much
CONTROLLER    > the planner deciding the next action
ACTUATOR      > the model making the change
SATURATION LIMIT > iteration cap / token budget
INSTABILITY   > the Ralph Wiggum loop
```

Grüne Notizbox: *"Self-scoring generator"*

Workflow-Kette: `SEO Input Form → Config - Scoring Weights (manual) → Claude - Generate & ... → Parse JSON → Rank Results → Final Output → Code in JavaScript → SEO Report (send: message, Gmail)`

Test-Input (lila Box): *„best coffee grinders 2026 / budget-conscious home baristas, commercial intent / 5"*

**Screenshot B — dasselbe Canvas, dazu das Test-Formular:**

Formular-Ansicht (`n8n.trw-aaa.site/form-test/seo-gen-workshop-form`):
- Titel: **SEO Title & Outline Generator**
- Untertitel: *"Generate, self-score, and rank SEO title variants — then get a full outline for the winner."*
- Feld „Target Keyword / Topic": `best coffee grinders 2026`
- Feld „Target Audience / Search Intent": `budget-conscious home baristas, commercial intent`
- Feld „Number of Title Variants": `5`
- Button: **Submit** (Formular via n8n automatisiert)

---

*Ende des Transkripts — 27 Screenshots vollständig erfasst, inkl. aller im Word-Dokument getippten Notizen an ihrer ursprünglichen Position.*
