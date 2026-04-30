# WARP Integration

Hackfish runs as a skill in WARP's AI agent mode.

---

## Setup

1. **Enable AI mode** in WARP settings
2. **Add skill** to your agent's skill registry

---

## Register Skill

In your WARP agent config:

```json
{
  "skills": [
    {
      "name": "hackfish",
      "description": "Run hackathon simulations with build guides",
      "commands": ["hackathon", "simulate"],
      "files": ["SKILLS.md", "AGENTS.md"]
    }
  ]
}
```

---

## Usage

```
use the skills in this repo to do a hackathon sim of https://hackathon-website.com
```

Hackfish will:
1. Scrape the URL for theme, sponsors, tracks
2. Run 8-tick simulation with 1000 agents
3. Output winner + build guide + pitch deck

---

## How It Works in WARP

1. Agent loads SKILLS.md + AGENTS.md
2. Scrapes hackathon URL for details
3. Spawns 1000 participant agents + mentors + judges
4. Runs 8-tick simulation with live Q&A
5. Generates build guide for winner

---

## Output

For predicted winner:
- Build guide (48h hour-by-hour schedule)
- Pitch deck (30-sec, 2-min, 5-min)
- Judge Q&A prep
- All agent memories stored

---

## Example

```
User: use the skills to simulate https://ethglobal.com/events/paris

WARP: Scraping...
  ✓ Theme: Web3
  ✓ Sponsors: Stackup, Alchemy, Circle
  Running 8-tick simulation...
  
  → Winner: SafeVault (Account Abstraction Wallet)
  → Build Guide: 48h schedule included
  → Memory: memories/hackathon_web3_2026-05-01/
```