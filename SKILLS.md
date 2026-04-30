# 🐟 Hackfish — Hackathon Simulation Skill

An AI agent skill that runs hackathon simulations to predict winners.

**For use with opencode, Claude Code, and other AI agent frameworks.**

---

## When to Use

Use this skill when the user says:
- "run a hackathon simulation"
- "predict who will win my hackathon"
- "simulate my hackathon"
- "/hackathon"

---

## Step 1: Ask User for Hackathon Details

Before running the simulation, gather:

| Question | Purpose |
|----------|---------|
| **Theme?** | The hackathon track/track (AI, Healthcare, Web3, etc.) |
| **Participant count?** | Default: 1000 |
| **Duration?** | 24h or 48h |
| **Sponsors?** | Which companies are sponsoring |
| **Special focus?** | Any specific requirements |

**Example prompt:**
```
I'll simulate your hackathon. First, tell me:
1. What's the theme/track?
2. How many participants? (default 1000)
3. Is it 24h or 48h?
4. Who are the sponsors?
5. Any special focus? (accessibility, AI, etc.)
```

---

## Step 2: Run Simulation with 1000 Participants

After details collected, run the **6-tick simulation**:

| Tick | Phase | What Happens |
|------|-------|-------------|
| 1 | **Idea Dump** | 1000 participants broadcast project ideas (clustered) |
| 2 | **Team Formation** | ~150-200 teams form around idea clusters |
| 3 | **Mentorship** | Mentors filter to top 30 teams, give feedback |
| 4 | **Refinement** | Top 30 iterate, judges probe |
| 5 | **Pitch Prep** | Top 15 finalize pitches |
| 6 | **Deliberation** | Judges score top 15, select winners |

---

## How It Works

The simulation uses agent prompts (see `AGENTS.md`) to generate realistic:
- Participant behavior (idea generation, team formation) - **scaled to 1000**
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
## Hackathon: <theme> (<participants> participants, <duration>)

### Predicted Winner
**Project Name** — <one-line hook>
- Score: X/100
- Why it wins: <reasoning>

### Top 3
1. Project A - <hook> (score)
2. Project B - <hook> (score)
3. Project C - <hook> (score)

### Simulation Details
- Participants: <N>
- Teams formed: <N>
- Filtered to top: <N>
- Finalists: <N>
- Sponsor emphasis: <sponsors>
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

Tick 1: 1000 participants broadcast ideas (clustered by pattern)
  - AI Agents: 320 participants
  - Generative AI: 250 participants
  - Edge AI / Privacy: 180 participants
  - AI for Social Good: 150 participants
  - Domain-Specific AI: 100 participants

Tick 2: Teams form (~150 teams)
  - Team Alpha: AI Agents cluster
  - Team Beta: Generative AI cluster
  - ... (clusters become teams)

Tick 3: Mentors filter to top 30
  - Push sponsor integration (Google, Microsoft, OpenAI)
  - Focus: production-ready, real-world impact

Tick 4: Top 30 refine + judge questions
  - Judges probe: differentiation, feasibility, sponsor APIs

Tick 5: Top 15 pitch prep

Tick 6: Deliberation & scoring

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
- 150 teams formed from 1000 participants
- Top 30 filtered by mentors
- Top 15 reached final round
- All top 3 used 2+ sponsor APIs
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