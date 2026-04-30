# 🐟 Hackfish

Run virtual hackathons and generate build guides for winning your next hackathon!

## Usage

```
use the skills in this repo to do a hackathon sim of https://hackathon-website.com
```

Hackfish will:
1. **Fetch** the hackathon page
2. **Extract** theme, tracks, sponsors, duration, participant count
3. **Run** 8-tick simulation with 1000 AI agents
4. **Output** predicted winner + build guide + pitch deck

## How It Works

| Tick | Phase | What Happens |
|------|-------|---------------|
| 1 | Idea Dump | 1000 participants broadcast ideas |
| 2 | Team Formation | ~150 teams form |
| 3 | Mentorship | Mentors filter to top 50 |
| 4 | Refinement | Top 50 iterate |
| 5 | Live Pitches | 50 teams pitch + Q&A |
| 6 | Semi-Final | Top 20, extended Q&A |
| 7 | Final Pitches | Top 10, full presentations |
| 8 | Deliberation | Judges score + build guide |

## Output

For the predicted winner, Hackfish generates:

| Output | Contents |
|--------|----------|
| **Winner** | Project name, score, why it wins |
| **Build Guide** | Hour-by-hour 48h schedule |
| **Tech Stack** | Exact technologies + sponsor APIs |
| **Pitch Deck** | 30-sec, 2-min, 5-min versions |
| **Judge Q&A** | Expected questions + answers |
| **Memory** | All agent research stored |

---
