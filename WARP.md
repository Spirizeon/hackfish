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
      "name": "hackathon",
      "description": "Run hackathon simulations to predict winners",
      "commands": ["/hackathon"],
      "files": ["SKILLS.md", "AGENTS.md"]
    }
  ]
}
```

---

## Usage

```bash
/hackathon ai
/hackathon healthcare
/hackathon web3
```

---

## How It Works in WARP

1. Agent loads SKILLS.md to understand commands
2. Spawns participant, mentor, judge agents from AGENTS.md
3. Runs 6-tick simulation
4. Returns predicted winner

---

## Commands

| Command | Action |
|---------|--------|
| `/hackathon <theme>` | Run full simulation |
| `/hackathon list` | Show supported themes |

---

## Themes

- ai, healthcare, web3, fintech, edtech, climate, civic