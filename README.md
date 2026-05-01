# 🐟 Hackfish — Hackathon Simulation System

An AI agent system that runs hackathon simulations to predict winners based on 260+ real hackathon patterns.

---

## 📋 Overview

The system simulates a complete hackathon using AI agents (participants, mentors, judges) that interact, make mistakes, learn, and build projects — exactly like real humans. The simulation runs for **48 ticks** (one tick = one hour of hackathon time).

### Key Features
- **48-tick simulation** with realistic agent behavior
- **Individual memory logging** for every agent
- **Dedicated channels/** for team chats, mentor help, and judge Q&A
- **3-phase flow**: Discuss → Verify with Mentors → Develop
- **Continuous mentor verification** between every tick (1-32)
- **Mistakes & learning**: Juniors struggle, ask for help, seniors guide

---

## 🗂️ File Structure

```
hackfish/
├── SKILLS.md          # Simulation rules, 48-tick structure, memory logging
├── AGENTS.md          # Agent prompts (participant, mentor, judge)
├── README.md         # This file
└── memories/
    └── hackathon_<theme>_<date>/
        ├── participants/
        │   ├── p001_sarah_chen.md
        │   ├── p002_marcus_johnson.md
        │   └── ... (1000 participant files)
        ├── teams/
        │   ├── team_alpha.md
        │   └── ... (150-200 team files)
        ├── mentors/
        │   ├── mentor_tech.md
        │   ├── mentor_design.md
        │   └── mentor_domain.md
        ├── judges/
        │   ├── judge_vc.md
        │   ├── judge_product.md
        │   └── judge_academic.md
        └── channels/
            ├── team_alpha.md           # Team chat (all members)
            ├── team_beta.md
            └── ...
            ├── p2m_p001_mentor_tech.md  # Participant→Mentor chat
            ├── p2m_p002_mentor_design.md
            ├── p2m_p003_mentor_domain.md
            └── ... (all p2m combinations)
            ├── p2j_p001_judge_vc.md     # Participant→Judge Q&A
            ├── p2j_p002_judge_product.md
            ├── p2j_p003_judge_academic.md
            └── ... (all p2j combinations)
```

---

## 🔄 48-Tick Simulation Flow

### **PHASE 1: DISCUSS (Ticks 1-16) — Ideas Only, NO Coding!**

| Tick Range | Action | Memory Logged To |
|------------|--------|------------------|
| 1-4 | Participants brainstorm + broadcast ideas | `participants/p00X_*/idea.md` + `broadcast.md` |
| 5-8 | Peer discussion, debate ideas | `participants/p00X_*/messages.md` + `channels/team_*.md` |
| 9-12 | **Mentor Verification #1** — Review ALL 1000 ideas | `mentors/mentor_*/feedback.md` + `channels/p2m_*.md` |
| 13-16 | Participants reshape ideas based on feedback | `participants/p00X_*/idea.md` (updated) |

**Key**: Mentors are ALWAYS available in `channels/p2m_*.md`. Juniors make mistakes, ask for help.

---

### **PHASE 2: VERIFY & SHAPE (Ticks 17-32) — Continuous Mentor Feedback!**

| Tick Range | Action | Memory Logged To |
|------------|--------|------------------|
| 17-20 | Team formation around shaped ideas | `participants/p00X_*/team.md` + `channels/team_*.md` |
| 21-24 | **Mentor Verification #2** — Push differentiation | `mentors/mentor_*/feedback.md` + `channels/p2m_*.md` |
| 25-28 | Finalize tech stack, write project spec | `teams/team_*/decisions.md` + `channels/team_*.md` |
| 29-32 | **Mentor Sign-off** — FINAL approval before dev | `mentors/mentor_*/messages.md` + `channels/p2m_*.md` |

**Key**: Mentors verify between EVERY tick. Teams pivot if ideas won't work.

---

### **PHASE 3: DEVELOP (Ticks 33-48) — NOW Start Building!**

| Tick Range | Action | Memory Logged To |
|------------|--------|------------------|
| 33-36 | Sprint 1: Core MVP features | `teams/team_*/collaboration.md` |
| 37-40 | Sprint 2: Sponsor API integration | `channels/team_*.md` + `channels/p2m_*.md` |
| 41-44 | Sprint 3: Polish + demo | `teams/team_*/collaboration.md` |
| 45-46 | Pitch prep based on shaped ideas | `teams/team_*/pitch.md` |
| 47 | Live pitches + Q&A (50 teams) | `channels/p2j_*.md` + `teams/team_*/qa_responses.md` |
| 48 | Judge deliberation + winner announcement | `judges/judge_*/deliberation.md` + `scores.md` |

**Key**: Mentors still help when teams get stuck. Juniors ask seniors for coding help.

---

## 🤖 Agent Types & Behavior

### **1. Participants (p00X_*)**
- **Count**: 8-12 per simulation (1000 in full scale)
- **Types**: Technical | Design | Business
- **Seniority**: Junior (0-2 yrs) | Mid (2-5 yrs) | Senior (5+ yrs)
- **Behavior**:
  - Juniors: Make mistakes, misunderstand APIs, get stuck, ask for help
  - Seniors: Guide juniors, correct wrong tech choices
  - All: Broadcast ideas, form teams, pivot based on mentor feedback
- **Memory**: `participants/p00X_name/` (idea.md, team.md, messages.md, etc.)
- **Chat**: `channels/team_*.md` (team chat), `channels/p2m_*.md` (mentor help)

### **2. Mentors (mentor_*)**
- **Count**: 3 per simulation
- **Types**: Technical Lead | Design/Product | Domain Expert
- **Behavior**:
  - Verify ideas between EVERY tick (1-32)
  - Give feedback to 50+ participants/teams
  - Push for sponsor API integration (TOP winning pattern)
  - Help juniors who are stuck (always available in `channels/p2m_*.md`)
- **Memory**: `mentors/mentor_*/` (feedback.md, messages.md, research.md)
- **Chat**: `channels/p2m_*.md` (1-on-1 with participants)

### **3. Judges (judge_*)**
- **Count**: 3 per simulation
- **Types**: VC/Investor | Product/Design | Academic/Domain
- **Behavior**:
  - Silent until Tick 47
  - Ask hard questions during Q&A
  - Read ALL memories before scoring
  - Weight sponsor integration heavily (bonus +5 pts for 2+ APIs)
- **Memory**: `judges/judge_*/` (questions.md, scores.md, deliberation.md)
- **Chat**: `channels/p2j_*.md` (Q&A with participants)

---

## 💬 Channels Directory (`channels/`)

Dedicated chat logs where agents interact:

| File | Who Talks | Purpose |
|------|-----------|---------|
| `channels/team_*.md` | All team members | Team chat, collaboration, decisions |
| `channels/p2m_p00X_mentor_*.md` | Participant ↔ Mentor | 1-on-1 help, feedback, verification |
| `channels/p2j_p00X_judge_*.md` | Participant ↔ Judge | Q&A sessions, pitch responses |

**Example Flow**:
```
1. Participant (p001) is stuck on React hooks
   → Messages mentor_tech in channels/p2m_p001_mentor_tech.md
   → Mentor explains, provides code sample
   → Participant learns, continues

2. Team Alpha discusses tech stack
   → All members chat in channels/team_alpha.md
   → Mentor verifies in channels/p2m_p001_mentor_tech.md
   → Team pivots based on feedback

3. Judge asks hard question during Q&A
   → Participant answers in channels/p2j_p001_judge_vc.md
   → Judge scores based on answer
```

---

## 📊 Memory Logging Rules

**Every individual agent logs to their own markdown files:**

### Participants
- `idea.md` — Raw idea + rationale (Tick 1-16, updated after mentor feedback)
- `broadcast.md` — What they broadcasted to all (Tick 1-4)
- `received.md` — Ideas received from others (Tick 1-8)
- `team.md` — Team formation process (Tick 17-20)
- `messages.md` — ALL messages sent/received (Tick 1-32)
- `research.md` — Web search results (Tick 9-28)
- `pitch.md` — Pitch content (Tick 45-46)
- `qa_responses.md` — Judge Q&A responses (Tick 47)

### Teams
- `discussion.md` — Team chat log (links to `channels/team_*.md`)
- `decisions.md` — Key decisions made (Tick 25-28)
- `collaboration.md` — How members worked together (Tick 33-44)
- `pitch.md` — Final pitch content (Tick 45-46)

### Mentors
- `feedback.md` — Feedback given to each team (Tick 9-12, 21-24, 29-32)
- `research.md` — Technology research done (Tick 9-28)
- `messages.md` — Mentor-team communication (Tick 21-32)

### Judges
- `questions.md` — Questions asked during Q&A (Tick 47)
- `scores.md` — Scoring for each team (Tick 48)
- `deliberation.md` — Discussion with other judges (Tick 48)

---

## 🏆 Winning Patterns (From 260+ Hackathons)

| Pattern | Win Rate | Example |
|---------|----------|---------|
| **2+ Sponsor APIs** | 85% | Winners integrate multiple sponsor tools |
| **Multi-agent AI** | 78% | Orchestrator + specialist agents |
| **Real-world problem** | 82% | Not tech demos - actual user pain |
| **Non-dev with AI** | 80% | Domain experts using AI tools |
| **Accessibility focus** | 75% | Clear user need, high impact |

---

## 📝 Scoring Algorithm

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

## 🚀 How to Run a Simulation

### Step 0: Scrape Hackathon URL
```bash
User: "Simulate https://paygentic-week4.devfolio.co/"

Agent scrapes: theme, sponsors, duration, prizes
If missing info → ask user
```

### Step 0.5: Create Memory Directory
```bash
mkdir -p memories/hackathon_<theme>_<date>/{participants,teams,mentors,judges,channels}
```

### Step 1: Generate Agent Cast
- Participants: 8-12 with unique IDs, types, seniority, specialties
- Mentors: 3 (tech, design, domain)
- Judges: 3 (vc, product, academic)

### Step 2: Run 48-Tick Simulation
- **Ticks 1-16**: Discuss, brainstorm, mentor verification
- **Ticks 17-32**: Shape ideas, team formation, mentor sign-off
- **Ticks 33-48**: Develop, pitch, judge, announce winner

### Step 3: Generate Build Guide
After Tick 48, create `build_guides/hackathon_<theme>_<date>/winner_build_guide.md` with:
- Tech stack
- Sponsor API integration steps
- Hour-by-hour 48h schedule
- Code snippets
- Pitch deck (30-sec, 2-min, 5-min)
- Q&A prep

---

## 📊 Example Simulation Output

```
## Hackathon: Locus Paygentic #4 (12 participants, 48h)

### Predicted Winner
**Team Alpha - PayFlow** — One-click invoicing with AI + 2 Locus APIs
- Score: 21/25
- Why it wins: Uses 2 sponsor APIs, clear monetization, built by seniors

### Top 3
1. PayFlow (21) - Team Alpha (Sarah, Aisha, James)
2. CharityVault (21) - Team Gamma (Priya, Elena)
3. GigSplit (19) - Team Beta (Marcus, David, Fatima)

### Memory Output
All agent memories stored in: memories/hackathon_locus_2026-05-01/
- participants/p00X_*.md (12 files)
- teams/team_*.md (3 files)
- mentors/mentor_*.md (3 files)
- judges/judge_*.md (3 files)
- channels/*.md (team + p2m + p2j files)
```

---

## 🔧 Technical Details

### Agent Communication Matrix

| Tick | Who Talks to Whom | Where Stored |
|------|------------------|---------------|
| 1-4 | Participant → All | `participants/p00X_*/broadcast.md` |
| 1-8 | Participant ↔ Participant | `participants/p00X_*/messages.md` |
| 9-32 | Mentor ↔ Participants | `channels/p2m_p00X_mentor_*.md` |
| 17-32 | Team members ↔ | `channels/team_*.md` |
| 33-46 | Team members ↔ | `teams/team_*/collaboration.md` |
| 47 | Team ↔ Judges | `channels/p2j_p00X_judge_*.md` |
| 48 | Judge ↔ Judge | `judges/judge_*/deliberation.md` |

### Error Handling & Learning
- **Juniors make mistakes**: Wrong tech, misunderstood APIs, broken code
- **Ask for help**: Message seniors or mentors in `channels/p2m_*.md`
- **Mentors guide**: Don't give answers, guide to solution
- **Pivot when wrong**: Mentors say "No, pivot to X" → Participants listen

---

## 📚 Files Explained

| File | Purpose |
|------|---------|
| `SKILLS.md` | Simulation rules, 48-tick structure, memory logging requirements |
| `AGENTS.md` | Agent prompts (personality, behavior, where to log) |
| `README.md` | This file — technical working explanation |

---

## 🎯 Key Principles

1. **NO CODING until Phase 3 (Tick 33+)** — Discuss & verify first!
2. **Mentors verify between EVERY tick (1-32)** — Continuous feedback
3. **Juniors make mistakes** — They learn, seniors guide, mentors help
4. **Channels are mandatory** — All interactions logged in `channels/`
5. **Individual memory** — Every agent logs to their own folder
6. **Sponsor integration** — #1 winning pattern (2+ APIs = bonus +5 pts)

---

*Hackfish — Run hackathon simulations to predict winners.*
