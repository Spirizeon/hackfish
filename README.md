# 🐟 Hackfish

**An AI agent skill for running hackathon simulations and predicting winners.**

Built for opencode, Claude Code, and other AI agent frameworks.

---

## What Is Hackfish?

Hackfish is a **simulation agent** that mimics a complete hackathon — participants brainstorming, mentors advising, judges scoring — to predict which project will win.

It uses agent prompts trained on **260+ real hackathons** to generate realistic team dynamics, mentor feedback, and final predictions.

### Use Cases

| For | Use Hackfish To |
|-----|-----------------|
| **Hackathon Organizers** | Preview likely winners, adjust judging criteria |
| **Participants** | Test your idea before the event, get mentor-style feedback |
| **Educators** | Teach hackathon strategy through simulation |
| **Product Teams** | Generate winning project concepts for innovation challenges |

---

## How It Works

```
/hackathon ai        → Run AI/ML hackathon simulation
/hackathon healthcare → Run Healthcare hackathon simulation
/hackathon web3      → Run Web3 hackathon simulation
```

The agent runs through **6 simulation ticks**:

| Tick | Phase | What Happens |
|------|-------|-------------|
| 1 | **Idea Dump** | Participants broadcast project ideas |
| 2 | **Team Formation** | Participants form teams around ideas |
| 3 | **Mentorship** | Mentors give feedback, push for sponsor integration |
| 4 | **Refinement** | Teams iterate, judges ask probing questions |
| 5 | **Pitch Prep** | Teams finalize pitches with mentor polish |
| 6 | **Deliberation** | Judges score and select winners |

**Output:** Predicted winner with confidence score and reasoning.

---

## For Developers

### Integrate with Your Agent

```
1. Copy src/SKILLS.md into your agent's skill registry
2. Load AGENTS.md prompts into your agent framework
3. Run: /hackathon <theme>
```

### Skill Commands

```
/hackathon <theme>     → Run full simulation
/predict <theme>      → Quick prediction (deprecated)
/simulate <theme>     → Run simulation (deprecated)
```

### Output Format

```
## Hackathon: <theme>

### Predicted Winner
**Project Name** — <one-line hook>
- Score: X/100
- Why it wins: <reasoning>

### Top 3
1. ...
2. ...
3. ...

### Accuracy (if validated)
- Match type: exact/same_domain/partial/miss
- Score: X/3
```

---

## How It Was Built

The knowledge base (`data/`, `hackathon-wiki/`) was used to **develop the skill** — it's development data, not runtime input:

- Analyzed **260+ hackathons** and **1,000+ winning projects**
- Identified winning patterns: sponsor integration, multi-agent AI, real-world impact
- Built agent prompts that simulate participants, mentors, judges
- Validated predictions against real results (78-100% accuracy)

**The knowledge base stays in dev. End users just run the skill.**

---

## Project Structure

```
hackfish/
├── README.md                  # This file
├── src/                       # Skill source (for agents)
│   ├── SKILLS.md             # Skill definition
│   ├── AGENTS.md             # Agent prompt templates
│   ├── TEAMS.md              # Team role definitions
│   └── WIKI-README.md        # Dev background
├── data/                     # Dev: research data (260+ hackathons)
├── examples/                 # Dev: generated outputs
└── hackathon-wiki/           # Dev: full knowledge base
```

---

## Supported Themes

```
/hackathon ai           → AI/ML
/hackathon healthcare  → Healthcare/Biotech
/hackathon web3        → Web3/Blockchain
/hackathon fintech     → FinTech/Payments
/hackathon edtech      → EdTech/Education
/hackathon climate     → Climate/Sustainability
/hackathon civic       → Civic/Government
```

---

## Scoring Model

Each project scored on:

| Criterion | Points | What Judges Look For |
|-----------|--------|---------------------|
| Novelty | 25 | Unexpected tech/domain combo |
| Feasibility | 25 | 48h buildable with 2-4 people |
| Impact | 25 | Clear real-world problem |
| Differentiation | 20 | Not the obvious approach |
| Sponsor Bonus | +5 | 2+ sponsor APIs integrated |

**Target: 85+/100 to win**

---

## Example Output

```
## Hackathon: AI/ML

### Predicted Winner
**AgentFlow** — Multi-agent AI orchestrator for enterprise workflows
- Score: 22/100
- Why it wins: Matches 2025 pattern (multi-agent), 2+ sponsor APIs, real-world problem

### Top 3
1. AgentFlow - Multi-agent orchestrator (22)
2. AccessiBot - Accessibility auto-fixer (20)
3. CodeReview AI - Security co-pilot (19)

### Accuracy
- Match type: same_domain
- Score: 2/3
```

---

## Contribute

Add more hackathon data to improve the skill:

```
1. Add event to data/<domain>_hackathons.json
2. Include: winners, tech stack, sponsor APIs
3. Update WIKI-META.json
```

---

*Hackfish — An AI agent skill that runs hackathon simulations to predict winners.*