# 🐟 Hackfish

An AI agent skill that runs hackathon simulations to predict winners — and tells you exactly how to build them.

---

## Usage

```
use the skills in this repo to do a hackathon sim of https://hackathon-website.com
```

Hackfish will:
1. **Fetch** the hackathon page
2. **Extract** theme, tracks, sponsors, duration, participant count
3. **Run** 8-tick simulation with 1000 AI agents
4. **Output** predicted winner + build guide + pitch deck

---

## Why Hackfish Works

### Traditional Approaches (Fail)

| Method | Why It Fails |
|--------|--------------|
| Static analysis | Can't predict team dynamics |
| Manual survey | Can't scale to 1000 participants |
| Simple scoring | No mentor/judge feedback loop |
| Guesswork | No data-driven predictions |

### Hackfish Architecture (Wins)

```
User Input (URL)
       ↓
┌──────────────────┐
│  Web Scraper     │ ← Extracts: theme, sponsors, tracks
└────────┬─────────┘
         ↓
┌──────────────────┐
│  1000 Agents     │ ← Each participant, mentor, judge
│  (8 ticks)      │ ← Idea → Team → Pitch → Q&A → Score
└────────┬─────────┘
         ↓
┌──────────────────┐
│  Memory System   │ ← Every agent stores research/pitch
└────────┬─────────┘
         ↓
┌──────────────────┐
│  Output          │ ← Winner + Build Guide + Pitch Deck
└──────────────────┘
```

**Key advantages:**
- **1000 agents** simulate real participant behavior
- **8-tick simulation** mirrors actual hackathon flow
- **Live Q&A rounds** test feasibility like real judges
- **Memory system** stores every agent's research
- **Build guide** tells winner exactly how to build

---

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

## Files

```
├── README.md    # This file
├── SKILLS.md    # Skill definition
├── AGENTS.md    # Agent prompts
└── WARP.md      # WARP integration
```

---

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

**Score:** Novelty(25) + Feasibility(25) + Impact(25) + Differentiation(20) + SponsorBonus(5)

Target: 85+/100