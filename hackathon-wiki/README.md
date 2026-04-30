# Hackathon Simulation Knowledge Wiki

This wiki contains data on 100+ hackathons and their winning projects for simulation training and validation.

## Structure
```
hackathon-wiki/
├── README.md              # This file
├── hackathons/            # Individual hackathon records
│   ├── ethglobal/         # ETHGlobal events (26+ hackathons)
│   ├── devfolio/          # Devfolio events (55+ hackathons)
│   └── major-tech/        # Major tech hackathons (20 hackathons)
├── patterns/             # Pattern analysis
│   ├── winning-patterns.json
│   ├── tech-trends.json
│   └── judge-preferences.json
└── analysis/             # Simulation results
    ├── predictions/
    └── accuracy-reports/
```

## Quick Stats
| Category | Count | Exact Match Rate |
|----------|-------|----------------|
| ETHGlobal | 26+ | 83.3% |
| Devfolio | 55+ | 87.5% |
| Major Tech | 20 | 85% |
| **Total** | **100+** | **85.3%** |

## Key Winning Patterns
1. **AI Agents** - Dominant in 2024-2025 (DAOGenie, Industry AI, PlayBack Network)
2. **Account Abstraction** - Smart wallets (Yield.me, Solvify, Urbexium)
3. **ZK/Privacy** - Privacy-preserving tools (RageAgainst.eu, POLP)
4. **Consumer DeFi** - Simple payments (HabibiCross, JustETH)
5. **Domain-Specific** - Agriculture/Health (FRESHGUARD, HyGenie)

## Prediction Criteria (25 pts each)
- Novelty: Unexpected tech/domain combos
- Feasibility: Buildable in 24-48h
- Impact: Clear real-world problem
- Differentiation: Not the obvious approach

## Match Scoring
- exact_match: 3pts (same domain + tech)
- same_domain: 2pts (same category)
- partial_overlap: 1pt (related domain)
- miss: 0pt (no alignment)

## Sponsor Integration is #1 Predictor
Winners almost always integrate 2+ sponsor technologies.