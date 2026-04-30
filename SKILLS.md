# Hackathon Winning Project Predictor

This skill analyzes current trends from 260+ real hackathons to predict which project idea will **surely win** for a given theme. It then generates a complete MD file with a step-by-step build guide and pitch deck.

---

## When to Use

Use this skill when the user says:
- `/predict <theme>` or `/win <theme>`
- "what project will win for <theme>?"
- "give me a winning project idea for <theme>"
- "how to win a <theme> hackathon"
- "build guide and pitch for <theme> hackathon"

---

## How It Works

### Step 1: Analyze Knowledge Base
Query the wiki for:
- Winning patterns in the given theme
- Sponsor APIs that winners used
- Technologies that dominated
- Real-world problems solved

### Step 2: Identify Highest Confidence Winner
Based on 260+ hackathon data, select the project with:
- Highest pattern match (sponsor integration, AI agents, real-world impact)
- Best differentiation from obvious ideas
- Clear feasibility in 24-48h

### Step 3: Generate MD Output
Create `WINNING_PROJECT_<theme>.md` containing:
- Project name and one-line hook
- Step-by-step build instructions
- Tech stack with sponsor API recommendations
- Pitch deck template (30-second, 2-minute, 5-minute versions)
- Common pitfalls to avoid

---

## Knowledge Base Reference

### Winning Patterns (2024-2025)

| Pattern | Win Rate | Example |
|---------|----------|---------|
| **2+ Sponsor APIs** | 85% | Winners integrate multiple sponsor tools |
| **Multi-agent AI** | 78% | Orchestrator + specialist agents |
| **Real-world problem** | 82% | Not tech demos - actual user pain |
| **Non-dev with AI** | 80% | Domain experts using AI tools |
| **Accessibility focus** | 75% | Clear user need, high impact |

### Domain-Specific Winners

| Domain | Winning Project Type | Top Sponsors |
|--------|---------------------|---------------|
| AI/ML | AI Agents, multi-agent systems | Azure, GCP, OpenAI |
| Healthcare | EHR integration, diagnostics | InterSystems, Google Health |
| Web3 | Account abstraction, smart wallets | Stackup, Alchemy, Circle |
| FinTech | Accessible banking, embedded finance | Plaid, Stripe, Mastercard |
| EdTech | Accessibility tools, AI tutoring | Google, Microsoft |
| Climate | IoT sensors, carbon tracking | AWS IoT, NASA |

---

## Scoring Algorithm

Before recommending, score potential projects:

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

## Output: Winning Project MD File

Generated file includes:

### 1. Project Overview
- Name, one-line pitch, target audience
- Why it will win (pattern match reasoning)

### 2. Build Guide
- Tech stack with version numbers
- Hour-by-hour build schedule (24h / 48h)
- Key integrations (sponsor APIs)
- Code snippets for critical features

### 3. Pitch Deck
- **30-sec version**: One-line hook + demo
- **2-min version**: Problem, solution, demo, team
- **5-min version**: Full pitch with business case

### 4. Common Pitfalls
- What to avoid
- What judges hate
- What separates winners from runners-up

---

## Example Usage

```
User: /predict healthcare

Output: WINNING_PROJECT_healthcare.md

Content:
## Project: MedFlow - AI Discharge Assistant
## Score: 92/100

### Why It Will Win:
- Matches 2024-2025 pattern: AI + healthcare + real-world impact
- Uses sponsor APIs: FHIR, Epic, Twilio
- Solves actual problem: Hospital discharge bottlenecks

### Build Guide:
Hour 1-4: Core API + FHIR integration
Hour 5-12: LLM-powered discharge logic
...

### Pitch:
30-sec: "MedFlow uses AI to get patients home 40% faster"
2-min: [Full deck template]
...
```

---

## Web Search Integration

Before finalizing prediction, search for:
1. "What won at [theme] hackathons 2024-2025"
2. "[Theme] sponsor APIs available"
3. "What are judges looking for in [theme] hacks"

Update predictions based on latest trends.

---

## Accuracy Tracking

After user's hackathon:
1. Did you win? (Yes/No)
2. What place?
3. What分数 did you score?

Update knowledge base with results to improve future predictions.