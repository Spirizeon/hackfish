# 🐟 Hackfish — Hackathon Simulation Skill

An AI agent skill that runs hackathon simulations to predict winners.

**For use with opencode, Claude Code, and other AI agent frameworks.**

---

## When to Use

Use this skill when the user says:
- `/hackathon <theme>` or `/simulate <theme>`
- "run a hackathon simulation for <theme>"
- "predict who will win the <theme> hackathon"
- "simulate a <theme> hackathon"

---

## How It Works

Hackfish runs a **6-tick simulation** that mirrors a real hackathon:

| Tick | Phase | What Happens |
|------|-------|-------------|
| 1 | **Idea Dump** | Participants broadcast project ideas |
| 2 | **Team Formation** | Participants form teams around compatible ideas |
| 3 | **Mentorship** | Mentors give feedback, push for sponsor integration |
| 4 | **Refinement** | Teams iterate, judges ask probing questions |
| 5 | **Pitch Prep** | Teams finalize pitches with mentor polish |
| 6 | **Deliberation** | Judges score and select winners |

The simulation uses agent prompts (see `AGENTS.md`) to generate realistic:
- Participant behavior (idea generation, team formation)
- Mentor feedback (pushing for novelty, feasibility, sponsor integration)
- Judge evaluation (scoring, deliberation)

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

Each project scored during deliberation:

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
## Hackathon: <theme>

### Predicted Winner
**Project Name** — <one-line hook>
- Score: X/100
- Why it wins: <reasoning>

### Top 3
1. Project A - <hook> (score)
2. Project B - <hook> (score)
3. Project C - <hook> (score)

### Simulation Notes
- Teams formed: X
- Mentor feedback themes: <themes>
- Judge criteria emphasized: <criteria>
```

---

## Example Usage

```
User: /hackathon ai

Agent runs simulation:

Tick 1: 8 participants broadcast ideas
  - CodeReview AI, LocalAI, AccessiBot, NoCode AI, EdgeIoT...

Tick 2: Teams form
  - Team Alpha (4): CodeReview AI
  - Team Beta (3): NoCode AI
  - Team Gamma (2): AccessiBot

Tick 3: Mentors give feedback
  - Push sponsor API integration
  - NoCode AI: "Strong real-world impact pattern"
  - AccessiBot: "Clear user need, auto-fix differentiation"

Tick 4: Refinement + judge questions
  - All teams pivot toward production-ready
  - Judges probe sponsor integration

Tick 5: Pitch prep
  - NoCode AI: Non-developer focus, 2 sponsor APIs
  - AccessiBot: Auto-fix, accessibility
  - CodeReview AI: Security domain

Tick 6: Deliberation
  - NoCode AI: 25/100 (wins)
  - AccessiBot: 22/100
  - CodeReview AI: 21/100

Output:
## Hackathon: AI

### Predicted Winner
**NoCode AI** — AI workflow builder for non-developers
- Score: 25/100
- Why: Matches "non-dev with AI" pattern, 2+ sponsor APIs

### Top 3
1. NoCode AI (25)
2. AccessiBot (22)
3. CodeReview AI (21)
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
| `TEAMS.md` | Team role definitions |

---

*Hackfish — Run hackathon simulations to predict winners.*