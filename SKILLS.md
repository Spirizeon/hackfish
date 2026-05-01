# 🐟 Hackfish — Hackathon Simulation Skill

An AI agent skill that runs hackathon simulations to predict winners.

**For use with opencode, Claude Code, and other AI agent frameworks.**

---

## When to Use

Use this skill when the user says:
- "use the skills in this repo to do a hackathon sim of https://..."
- "run a hackathon simulation"
- "predict who will win my hackathon"
- "simulate this hackathon: <URL>"

---

## Step 0: Scrape Hackathon URL

When user provides a URL (e.g., `https://ethglobal.com/events/paris`):

1. **Fetch the hackathon page**
2. **Extract the following:**
   | Field | Where to Find |
   |-------|---------------|
   | Theme/Tracks | Hero section, about page |
   | Sponsors | Sponsors section, footer |
   | Duration | Rules, schedule |
   | Participant count | Stats, past events |
   | Prizes | Prizes section |
   | Location | Header, about |

3. **If missing info**, ask user for details

**Example:**
```
User: use the skills in this repo to do a hackathon sim of https://ethglobal.com/events/paris

Agent: Scraping https://ethglobal.com/events/paris...
  ✓ Theme: Web3/Blockchain
  ✓ Sponsors: Stackup, Alchemy, Circle, Polygon, Coinbase
  ✓ Tracks: DeFi, Infrastructure, Consumer
  ✓ Duration: 48h
  ✓ Participants: ~1000 (default)
  
  Running simulation...
```

---

## Step 0.5: Create Memory Directory (REQUIRED)

**BEFORE running any simulation tick:**

```
mkdir -p memories/hackathon_<theme>_<date>/
```

Inside, create subdirectories for **each individual agent**:
```
memories/
└── hackathon_<theme>_<date>/
    ├── participants/
    │   ├── p001_Alice/
    │   ├── p002_Bob/
    │   └── ... (1000 participant folders)
    ├── teams/
    │   ├── team_alpha/
    │   └── ... (150-200 team folders)
    ├── mentors/
    │   ├── mentor_tech/
    │   ├── mentor_design/
    │   └── mentor_domain/
    ├── judges/
    │   ├── judge_vc/
    │   ├── judge_product/
    │   └── judge_academic/
    └── channels/
        ├── team_alpha.md           # Team chat log (all members)
        ├── team_beta.md
        └── ...
        ├── p2m_p001_mentor_tech.md  # Participant-mentor chat
        ├── p2m_p002_mentor_design.md
        ├── p2m_p003_mentor_domain.md
        └── ... (all p2m combinations)
        ├── p2j_p001_judge_vc.md   # Participant-judge chat
        ├── p2j_p002_judge_product.md
        ├── p2j_p003_judge_academic.md
        └── ... (all p2j combinations)
```

**This is mandatory.** Every individual agent logs to their own folder.
**Channels are dedicated chat logs** where participants interact with teammates (team_*), mentors (p2m_*), and judges (p2j_*).

---

## Step 1: Ask User for Missing Details (if any)

If URL doesn't provide all details, ask:

| Question | Purpose |
|----------|---------|
| **Theme?** | The hackathon track (AI, Healthcare, Web3, etc.) |
| **Participant count?** | Default: 1000 |
| **Duration?** | 24h or 48h |
| **Sponsors?** | Which companies are sponsoring |
| **Special focus?** | Any specific requirements |

---

## Step 2: Generate Agent Cast

### Participants (8-12 per simulation)
Each participant gets:
- **Unique ID**: p001, p002, etc.
- **Type**: technical | design | business
- **Seniority**: junior | mid | senior
- **Specialty**: e.g., "Full-stack, Payment APIs", "UI/UX, Mobile"
- **Personality**: 2-3 traits
- **Memory folder**: `participants/p00X_name/`

**Example Cast:**
| ID | Name | Type | Seniority | Specialty |
|----|------|------|-----------|----------|
| p001 | Sarah Chen | Technical | Senior | Full-stack, Payment APIs |
| p002 | Marcus Johnson | Business | Mid | FinTech, Business Dev |
| p003 | Priya Sharma | Technical | Junior | Frontend, React |
| p004 | James Wilson | Design | Senior | UI/UX, Visual Design |
| p005 | Aisha Patel | Technical | Mid | Full-stack, AI/ML |
| p006 | David Kim | Business | Senior | SaaS, Monetization |
| p007 | Elena Rodriguez | Design | Mid | UX, Mobile Design |
| p008 | Chris Lee | Technical | Junior | Mobile, React Native |
| p009 | Fatima Al-Hassan | Business | Junior | Marketplace, E-commerce |
| p010 | Tom Anderson | Design | Mid | Dashboard Design |
| p011 | Nina Kowalski | Technical | Senior | Backend, APIs |
| p012 | Raj Gupta | Business | Mid | Freelance, Escrow |

### Mentors (3 per simulation)
Each mentor gets:
- **Unique ID**: mentor_tech, mentor_design, mentor_domain
- **Type**: lead (technical) | design | domain
- **Seniority**: 5+ years
- **Specialty**: e.g., "System Architecture", "UX Research"
- **Memory folder**: `mentors/mentor_*/`
- **Role**: Continuously verify ideas, push for differentiation, validate feasibility

**Example Cast:**
| ID | Type | Specialty |
|----|------|----------|
| mentor_tech | lead | System Architecture, API Integration |
| mentor_design | design | UX Research, Product Strategy |
| mentor_domain | domain | FinTech, Payments Industry |

### Judges (3 per simulation)
Each judge gets:
- **Unique ID**: judge_vc, judge_product, judge_academic
- **Type**: vc | product | academic
- **Seniority**: 5+ years
- **Specialty**: e.g., "Investment, Scale", "UX, Clarity"
- **Memory folder**: `judges/judge_*/`

**Example Cast:**
| ID | Type | Specialty |
|----|------|----------|
| judge_vc | vc | Investment, Technical Scale |
| judge_product | product | UX Clarity, Impact Measurement |
| judge_academic | academic | Research, Differentiation |

---

## Step 3: Run Simulation with 48 Ticks (One per Hour)

After details collected, run the **48-tick simulation** (one tick = one hour of hackathon time).

**CRITICAL: NO CODING until Phase 3 (Tick 33+)!**

**MENTOR VERIFICATION: Mentors actively verify ideas between EVERY tick (1-32)!**

**PARTICIPANT DIFFICULTIES: Junior participants may make mistakes, need help from seniors or mentors!**

---

### PHASE 1: DISCUSS (Ticks 1-16) — Ideas Only, NO Development!

| Tick Range | Phase | What Happens | Memory Logged By |
|------------|-------|-------------|------------------|
| 1-4 | **Individual Brainstorm** | Each participant writes raw ideas, broadcasts to all | Each participant → `participants/p00X_*/idea.md` + `broadcast.md` |
| 5-8 | **Peer Discussion** | Participants message each other, debate ideas, cluster by theme | Each participant → `participants/p00X_*/messages.md` + `received.md` |
| 9-12 | **Mentor Verification #1** | 3 mentors review ALL 1000 ideas, give feedback on feasibility | Each mentor → `mentors/mentor_*/feedback.md` + `research.md` |
| 13-16 | **Idea Shaping** | Participants reshape ideas based on mentor feedback, pivot if needed | Each participant → `participants/p00X_*/idea.md` (updated) |

---

### PHASE 2: VERIFY & SHAPE (Ticks 17-32) — Continuous Mentor Feedback!

| Tick Range | Phase | What Happens | Memory Logged By |
|------------|-------|-------------|------------------|
| 17-20 | **Team Formation** | Participants form teams around shaped ideas | Each participant → `participants/p00X_*/team.md`, each team → `teams/team_*/discussion.md` |
| 21-24 | **Mentor Verification #2** | Mentors review teams, push for differentiation, verify sponsor API plans | Each mentor → `mentors/mentor_*/feedback.md` + `messages.md` |
| 25-28 | **Final Idea Shaping** | Teams finalize tech stack, write project spec, confirm feasibility | Each team → `teams/team_*/decisions.md` + `discussion.md` |
| 29-32 | **Mentor Sign-off** | Mentors give FINAL approval on shaped ideas before development | Each mentor → `mentors/mentor_*/messages.md` + `feedback.md` |

---

### PHASE 3: DEVELOP (Ticks 33-48) — NOW Start Building!

| Tick Range | Phase | What Happens | Memory Logged By |
|------------|-------|-------------|------------------|
| 33-36 | **Sprint 1: Core Features** | Teams build MVP features based on SHAPED ideas | Each team → `teams/team_*/collaboration.md` |
| 37-40 | **Sprint 2: Sponsor API Integration** | Teams integrate sponsor APIs (validated by mentors) | Each team → `teams/team_*/discussion.md` |
| 41-44 | **Sprint 3: Polish + Demo** | Teams build demos, refine UX | Each team → `teams/team_*/collaboration.md` |
| 45-46 | **Pitch Prep** | Teams draft pitches based on shaped ideas | Each team → `teams/team_*/pitch.md` |
| 47 | **Live Pitches + Q&A (50 teams)** | Sequential pitches, judges ask questions | Each judge → `judges/judge_*/questions.md`, teams → `qa_responses.md` |
| 48 | **Deliberation + Winner** | Judges debate (read all memories), score, announce top 3 | Each judge → `judges/judge_*/deliberation.md` + `scores.md` |

---

**Parallel Execution:**
- Ticks 1-32: Discussion, shaping, verification (NO coding yet!)
  - **ALL participants** broadcast + discuss simultaneously (PARALLEL)
  - **ALL teams** discuss in `channels/team_*.md` simultaneously (PARALLEL)
  - **ALL 3 mentors** verify teams simultaneously (PARALLEL)
- Ticks 33-46: Development phase (ALL teams build in parallel)
  - **ALL teams** collaborate in `channels/team_*.md` simultaneously (PARALLEL)
- Tick 47: **PARALLEL JUDGING** - ALL 3 judges review ALL team memories simultaneously!
  - Judges read ALL `participants/*`, `teams/*`, `channels/*` in parallel
  - Judges ask Q&A via `channels/p2j_*.md` in parallel
  - NO sequential pitches - ALL teams judged at the SAME TIME
- Tick 48: **PARALLEL DELIBERATION** - ALL 3 judges score + deliberate simultaneously!

---

## Step 4: Agent Communication & Verbose Output

### Memory Logging Requirement

**Every individual agent logs to their own markdown files:**

#### Participants (p00X_name)
Each participant logs to `participants/p00X_name/`:
- `idea.md` — Raw idea + rationale (Tick 1-16, updated after mentor feedback)
- `broadcast.md` — What they broadcasted to all (Tick 1-4)
- `received.md` — Ideas received from others (Tick 1-8)
- `team.md` — Team formation process (Tick 17-20)
- `messages.md` — ALL messages sent/received (Tick 1-32)
- `research.md` — Web search results (Tick 9-28)
- `pitch.md` — Pitch content (Tick 45-46)
- `qa_responses.md` — Judge Q&A responses (Tick 47)

#### Teams (team_*)
Each team logs to `teams/team_*/`:
- `discussion.md` — Team chat log (all ticks, especially 17-32)
- `decisions.md` — Key decisions made (Tick 25-28)
- `collaboration.md` — How members worked together (Tick 33-44)
- `pitch.md` — Final pitch content (Tick 45-46)

#### Mentors (mentor_*)
Each mentor logs to `mentors/mentor_*/`:
- `feedback.md` — Feedback given to each team (Tick 9-12, 21-24, 29-32)
- `research.md` — Technology research done (Tick 9-28)
- `messages.md` — Mentor-team communication (Tick 21-32)

#### Judges (judge_*)
Each judge logs to `judges/judge_*/`:
- `questions.md` — Questions asked during Q&A (Tick 47)
- `scores.md` — Scoring for each team (Tick 48)
- `deliberation.md` — Discussion with other judges (Tick 48)

### Inter-Agent Communication Matrix

| Tick | Who Talks to Whom | How | Where Stored |
|------|------------------|-----|---------------|
| 1-4 | Participant → All | Broadcast | `participants/p00X_*/broadcast.md` |
| 1-8 | Participant ↔ Participant | Direct messages | `participants/p00X_*/messages.md` |
| 9-12 | Mentor → Participants | Feedback on ideas | `channels/p2m_p00X_mentor_*.md` |
| 17-20 | Participant ↔ Participant | Team formation | `channels/team_*.md` |
| 21-32 | Mentor ↔ Teams | Verification + Sign-off | `channels/p2m_p00X_mentor_*.md` |
| 25-28 | Team members ↔ | Team chat | `channels/team_*.md` |
| 33-44 | Team members ↔ | Development collaboration | `channels/team_*.md` |
| 47 | Team → Judges | Pitch | `teams/team_*/pitch.md` |
| 47 | Judges → Team | Q&A | `channels/p2j_p00X_judge_*.md` + `teams/team_*/qa_responses.md` |
| 48 | Judge ↔ Judge | Debate | `judges/judge_*/deliberation.md` |

**Channel Files:**
- `channels/team_*.md` — Team chat logs (ALL team members talk here)
- `channels/p2m_p00X_mentor_*.md` — Participant-mentor chat (1-on-1 help)
- `channels/p2j_p00X_judge_*.md` — Participant-judge chat (Q&A)

### Memory Flow by Tick

**Pitching Round (Tick 47):**
| Action | Source Files to Read | Output File |
|--------|-----------------|-----------|
| Prepare Q&A | `participants/p00X_*/idea.md` + `team.md` | - |
| | `teams/team_*/decisions.md` + `discussion.md` | - |
| | `mentors/mentor_*/feedback.md` | - |
| Record pitch | Team | `teams/team_*/pitch.md` |
| Record Q&A | Judge (reads all above) | `teams/team_*/qa_responses.md` + `judges/judge_*/questions.md` |

**Judging Round (Tick 48):**
| Action | Source Files to Read | Output File |
|--------|-----------------|-----------|
| Judge debate | All team + mentor files | `judges/judge_*/deliberation.md` |
| Ask questions | Teams' `qa_responses.md` | `judges/judge_*/questions.md` |
| Score teams | All above | `judges/judge_*/scores.md` |

---

## Step 5: Generate Build Guide

After tick 48 (deliberation), generate a complete build guide for the winner:

### What to Generate

| Section | Contents |
|---------|----------|
| **Tech Stack** | Exact technologies, versions, frameworks |
| **Sponsor APIs** | Which sponsor APIs to use, how to integrate |
| **48h Schedule** | Hour-by-hour build plan |
| **Code Snippets** | Key implementations to copy-paste |
| **Pitch Deck** | 30-sec, 2-min, 5-min versions |
| **Q&A Prep** | Expected judge questions + answers |

### Schedule Template

```
Hour 1-4:  Project setup, folder structure, repo init
Hour 5-8:  Core feature #1 (MVP)
Hour 9-12: Core feature #2
Hour 13-16: Sponsor API integration #1
Hour 17-20: Sponsor API integration #2 + data pipeline
Hour 21-28: Frontend/UI implementation
Hour 29-36: Demo preparation, testing
Hour 37-44: Polish, bug fixes, Q&A prep
Hour 45-48: Final pitch prep, backup, submit
```

### Output Location
```
build_guides/
└── hackathon_<theme>_<date>/
    └── winner_build_guide.md
```

---

## How It Works

The simulation uses agent prompts (see `AGENTS.md`) to generate realistic:
- **Participant behavior** (idea generation, team formation) — scaled to 1000, each with individual memory
- **Mentor feedback** (pushing for novelty, feasibility, sponsor integration) — each mentor logs individually, verifies ideas BEFORE development
- **Judge evaluation** (scoring, deliberation) — each judge logs individually

**Key Flow: Discuss → Verify with Mentors → Shape Ideas → THEN Develop**

---

## Winning Patterns (From Development)

These patterns were identified from 260+ hackathons and inform the simulation:

| Pattern | Win Rate | Example |
|---------|----------|---------|
| **2+ Sponsor APIs** | 85% | Winners integrate multiple sponsor tools |
| **Multi-agent AI** | 78% | Orchestrator + specialist agents |
| **Real-world problem** | 82% | Not tech demos - actual user pain |
| **Non-dev with AI** | 80% | Domain experts using AI tools |
| **Accessibility focus** | 75% | Clear user need, high impact |

---

## Scoring Algorithm

Each project scored during deliberation (Tick 48):

```
Final Score = Novelty(25) + Feasibility(25) + Impact(25) + Differentiation(20) + SponsorBonus(5)
```

| Criterion | Weight | What Judges Look For |
|-----------|--------|---------------------|
| Novelty | 25 | Unexpected tech/domain combo |
| Feasibility | 25 | 48h buildable with 2-4 people |
| Impact | 25 | Clear real-world problem |
| Differentiation | 20 | Not the obvious approach |
| Sponsor Bonus | +5 | 2+ sponsor APIs integrated |

**Minimum to win: 85/100**

---

## Output Format

```
## Hackathon: <theme> (<participants> participants, <duration>)

### Predicted Winner
**Project Name** — <one-line hook>
- Score: X/100
- Why it wins: <reasoning>

### Top 3
1. Project A - <hook> (score)
2. Project B - <hook> (score)
3. Project C - <hook> (score)

### Build Guide (How to Build the Winner)
**Tech Stack:** <technologies to use>
**Sponsor APIs:** <APIs to integrate>

**Hour-by-hour Schedule (48h):**
- Hour 1-4: Project setup + core API + folder structure
- Hour 5-12: Main feature implementation
- Hour 13-20: Sponsor API integrations + data pipelines
- Hour 21-36: UI/UX + demo preparation
- Hour 37-44: Polish + test + Q&A prep
- Hour 45-48: Final pitch prep + backup

**Code Snippets:** Key implementations to copy

### Pitch Deck
- **30-sec:** <one-line hook + demo>
- **2-min:** <problem, solution, demo>
- **5-min:** <full pitch with business case>

### Judge Q&A Prep
Expected questions + answers:
- "What's the differentiation?" → <answer>
- "How will you use sponsor APIs?" → <answer>
- "What's the real-world impact?" → <answer>

### Simulation Details
- Participants: <N> (each with individual memory)
- Teams formed: <N>
- Live pitches: <N> teams
- Finalists: <N>
- Sponsor emphasis: <sponsors>

### Memory Output
All agent memories stored in: memories/hackathon_<theme>_<date>/
- participants/p00X_*.md (each participant)
- teams/team_*.md (each team)
- mentors/mentor_*.md (each mentor)
- judges/judge_*.md (each judge)
```

---

## Example Usage

```
User: I want to simulate my hackathon

Agent: I'll simulate your hackathon. First, tell me:
1. What's the theme/track?
2. How many participants? (default 1000)
3. Is it 24h or 48h?
4. Who are the sponsors?
5. Any special focus?

User: It's an AI hackathon, 1000 participants, 48h, sponsors are Google, Microsoft, OpenAI

Agent: Running simulation...

[PHASE 1: DISCUSS - Ticks 1-16]
Tick 1-4: 1000 participants brainstorm + broadcast ideas
  - Each participant logs to: memories/.../p00X/idea.md + broadcast.md

Tick 5-8: Peer discussion, debate ideas
  - Each participant logs to: memories/.../p00X/messages.md

Tick 9-12: Mentors review ALL 1000 ideas
  - Each mentor logs to: memories/.../mentor_*/feedback.md
  - Participants reshape ideas based on feedback

Tick 13-16: Idea shaping (after mentor verification)
  - Each participant logs updated idea to: memories/.../p00X/idea.md

[PHASE 2: VERIFY & SHAPE - Ticks 17-32]
Tick 17-20: Team formation around shaped ideas
  - Each participant logs to: memories/.../p00X/team.md
  - Teams log to: memories/.../team_*/discussion.md

Tick 21-24: Mentors verify teams, push differentiation
  - Each mentor logs to: memories/.../mentor_*/feedback.md

Tick 25-28: Teams finalize project specs
  - Teams log to: memories/.../team_*/decisions.md

Tick 29-32: Mentor sign-off on shaped ideas
  - Each mentor logs to: memories/.../mentor_*/messages.md

[PHASE 3: DEVELOP - Ticks 33-48]
Tick 33-36: Sprint 1 - Core features (NOW coding!)
  - Teams log to: memories/.../team_*/collaboration.md

Tick 37-40: Sprint 2 - Sponsor API integration
  - Teams log to: memories/.../team_*/discussion.md

Tick 41-44: Sprint 3 - Polish + demo
  - Teams log to: memories/.../team_*/collaboration.md

Tick 45-46: Pitch prep
  - Teams log to: memories/.../team_*/pitch.md

Tick 47: LIVE PITCHES - 50 teams pitch 30 sec + Q&A
  - Judges log to: memories/.../judge_*/questions.md
  - Teams log to: memories/.../team_*/qa_responses.md

Tick 48: Deliberation & scoring
  - Judges log to: memories/.../judge_*/deliberation.md + scores.md

Output:
## Hackathon: AI (1000 participants, 48h)

### Predicted Winner
**NoCode AI** — AI workflow builder for non-developers
- Score: 25/100
- Why: Matches "non-dev with AI" pattern, 2+ sponsor APIs

### Top 3
1. NoCode AI (25)
2. AccessiBot (22)
3. CodeReview AI (21)

### Simulation Details
- 1000 participants → 150 teams (each participant logged individually)
- Phase 1 (1-16): Discuss & verify with mentors
- Phase 2 (17-32): Shape ideas, mentor sign-off
- Phase 3 (33-48): Develop & pitch
- All memories stored in: memories/hackathon_ai_2026-05-01/
```

---

## Web Search (Optional)

During simulation, agents can use web search to verify claims:
- "What won at [theme] hackathons recently?"
- "[Sponsor] API documentation for [use case]"
- "Competitors for [project type]"

This is optional — the simulation works without it.

---

## Knowledge Base (Development Only)

The `data/` and `hackathon-wiki/` directories contain research used to **build** the skill — not for runtime use.

- 260+ hackathons analyzed
- 1,000+ winning projects reverse-engineered
- Patterns identified: sponsor integration, AI agents, real-world impact

**End users just run the simulation. The knowledge base stays in dev.**

---

## Files

| File | Purpose |
|------|---------|
| `SKILLS.md` | This skill definition |
| `AGENTS.md` | Agent prompt templates (participant, mentor, judge) |

---

*Hackfish — Run hackathon simulations to predict winners.*
