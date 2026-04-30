# 🐟 Hackfish

Mimic a complete hackathon — participants brainstorming, mentors advising, judges scoring — to predict which project will win.

Built on insights from 260+ real hackathons. Runs a 6-tick simulation that generates realistic team dynamics, mentor feedback, and judge evaluations.

## Usage

```bash
/hackathon ai           → Run AI/ML hackathon simulation
/hackathon healthcare  → Run Healthcare hackathon
/hackathon web3        → Run Web3 hackathon
/hackathon fintech     → Run FinTech hackathon
/hackathon edtech      → Run EdTech hackathon
/hackathon climate     → Run Climate hackathon
```

**Output:** Predicted winner with score and reasoning.

## Integrate

```bash
# Clone
git clone https://github.com/yourusername/hackfish.git

# Use
- Copy src/SKILLS.md into your agent's skill registry
- Use src/AGENTS.md prompts for participant, mentor, judge agents
- Run: /hackathon <theme>
```

**Source files:**
```
src/
├── SKILLS.md    # Skill definition
├── AGENTS.md    # Agent prompts (18KB)
├── TEAMS.md     # Team roles
└── WIKI-README.md
```

---

## How It Works

| Tick | Phase |
|------|-------|
| 1 | Participants broadcast ideas |
| 2 | Teams form |
| 3 | Mentors give feedback |
| 4 | Teams refine, judges question |
| 5 | Pitch prep |
| 6 | Judges deliberate & score |

**Score:** Novelty(25) + Feasibility(25) + Impact(25) + Differentiation(20) + SponsorBonus(5)

Target: 85+/100 to win.
