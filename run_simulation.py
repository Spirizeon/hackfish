#!/usr/bin/env python3
"""
Hackathon Simulation Runner
Meta PyTorch OpenEnv Hackathon - 800 participants
"""

import os
import json
import random
from datetime import datetime
from pathlib import Path

random.seed(42)

# Config
THEME = "AI/RL Environments"
PARTICIPANTS = 800
TEAM_SIZE = 3
TOTAL_TEAMS = PARTICIPANTS // TEAM_SIZE
SPONSORS = ["Meta", "PyTorch", "Hugging Face"]
DURATION = "48h"

BASE_DIR = Path("/home/berzi/Documents/hackfish/memories/hackathon_ai_rl_env_2026-05-04")

# Winning patterns for idea generation
IDEA_PATTERNS = [
    "AI Agents with OpenEnv",
    "Multi-agent RL Environment",
    "Sponsor API Integration (Meta/PyTorch/HuggingFace)",
    "Real-world Impact (Healthcare/Climate/EdTech)",
    "Accessibility Focus",
    "Non-developer with AI Tools",
    "Edge AI / Local Inference",
    "Customer Service Agents",
    "Email Triage System",
    "Autonomous Traffic Control",
    "Gaming Multi-Agent Strategy",
    "EHR Integration Environment",
    "Mental Health AI Agents",
    "Cross-border Payment Agents",
    "IoT Sensor Environment",
    "Carbon Tracking Agents",
    "AI Tutoring Environment",
    "Wearables Data Environment",
    "DeFi Agent Environment",
    "ZK Privacy Environment",
]

# Participant archetypes
SENIORITY = ["junior", "mid", "senior"]
TYPES = ["technical", "design", "business"]
PERSONALITIES = [
    ["competitive", "creative", "stubborn"],
    ["analytical", "methodical", "curious"],
    ["bold", "visionary", "risk-taker"],
    ["collaborative", "empathetic", "user-focused"],
    ["technical", "detail-oriented", "systematic"],
]

EXPERTISE_MAP = {
    "technical": ["Python", "PyTorch", "RL", "Docker", "Gymnasium API"],
    "design": ["UX Research", "Product Design", "User Testing", "Figma"],
    "business": ["Product Strategy", "Market Research", "Pitch Deck", "Business Model"],
}

class HackathonSimulation:
    def __init__(self):
        self.participants = []
        self.teams = []
        self.mentors = []
        self.judges = []
        self.tick = 0
        
    def generate_participants(self):
        """Generate 800 participants with diverse backgrounds"""
        print(f"Generating {PARTICIPANTS} participants...")
        
        for i in range(1, PARTICIPANTS + 1):
            seniority = random.choice(SENIORITY)
            ptype = random.choice(TYPES)
            personality = random.choice(PERSONALITIES)
            expertise = EXPERTISE_MAP[ptype].copy()
            expertise.append(random.choice(["OpenEnv", "Hugging Face", "Meta APIs"]))
            
            participant = {
                "id": f"p{str(i).zfill(3)}",
                "name": f"participant_{i}",
                "seniority": seniority,
                "type": ptype,
                "personality": personality,
                "expertise": expertise,
                "idea": random.choice(IDEA_PATTERNS),
                "team": None,
                "broadcast": "",
                "messages": [],
                "research": [],
                "pitch": "",
                "score": 0,
            }
            self.participants.append(participant)
            
        print(f"  ✓ Generated {len(self.participants)} participants")
        
    def tick_1_idea_dump(self):
        """Tick 1: All participants broadcast ideas"""
        self.tick = 1
        print(f"\n=== TICK {self.tick}: IDEA DUMP ===")
        print(f"All {PARTICIPANTS} participants broadcasting ideas...")
        
        for p in self.participants:
            idea = p["idea"]
            broadcast = f'I\'m building "{idea}" using Meta OpenEnv and PyTorch. This solves real problems with AI agents.'
            p["broadcast"] = broadcast
            
            # Write to memory file
            mem_dir = BASE_DIR / "participants" / f"{p['id']}_{p['name']}"
            mem_dir.mkdir(parents=True, exist_ok=True)
            
            with open(mem_dir / "idea.md", "w") as f:
                f.write(f"# {p['name']} - Idea\n\n")
                f.write(f"## Original Idea (Tick 1)\n")
                f.write(f"**Project:** {idea}\n")
                f.write(f"**Description:** {broadcast}\n")
                f.write(f"**Seniority:** {p['seniority']}\n")
                f.write(f"**Type:** {p['type']}\n")
                f.write(f"**Expertise:** {', '.join(p['expertise'])}\n")
                
            with open(mem_dir / "broadcast.md", "w") as f:
                f.write(f"# {p['name']} - Broadcast\n\n")
                f.write(f"## Tick 1: Broadcast to All\n")
                f.write(f"{broadcast}\n")
                
        print(f"  ✓ All participants broadcasted ideas")
        print(f"  ✓ Individual memories written to participants/*/idea.md and broadcast.md")
        
    def tick_2_team_formation(self):
        """Tick 2: Form teams around idea clusters"""
        self.tick = 2
        print(f"\n=== TICK {self.tick}: TEAM FORMATION ===")
        print(f"Forming {TOTAL_TEAMS} teams of {TEAM_SIZE}...")
        
        # Shuffle and form teams
        random.shuffle(self.participants)
        
        for i in range(0, PARTICIPANTS - (PARTICIPANTS % TEAM_SIZE), TEAM_SIZE):
            team_id = f"team_{str(i//TEAM_SIZE + 1).zfill(3)}"
            members = self.participants[i:i+TEAM_SIZE]
            
            team = {
                "id": team_id,
                "members": [m["id"] for m in members],
                "idea": members[0]["idea"],  # Lead's idea
                "score": random.randint(60, 95),
                "sponsor_apis": random.randint(0, 3),
                "discussion": [],
                "decisions": [],
            }
            self.teams.append(team)
            
            # Update participant team assignment
            for m in members:
                m["team"] = team_id
                
            # Write team memory
            team_dir = BASE_DIR / "teams" / team_id
            team_dir.mkdir(parents=True, exist_ok=True)
            
            with open(team_dir / "discussion.md", "w") as f:
                f.write(f"# {team_id} - Team Discussion\n\n")
                f.write(f"## Members\n")
                for m in members:
                    f.write(f"- {m['id']} ({m['type']}, {m['seniority']})\n")
                f.write(f"\n## Idea\n{team['idea']}\n")
                f.write(f"\n## Tick 2: Formation\n")
                f.write(f"Team formed around: {team['idea']}\n")
                
            # Write participant team.md
            for m in members:
                mem_dir = BASE_DIR / "participants" / f"{m['id']}_{m['name']}"
                with open(mem_dir / "team.md", "w") as f:
                    f.write(f"# {m['name']} - Team\n\n")
                    f.write(f"**Team:** {team_id}\n")
                    f.write(f"**Members:** {', '.join([mm['id'] for mm in members])}\n")
                    f.write(f"**Role:** {m['type']}\n")
                    
        print(f"  ✓ Formed {len(self.teams)} teams")
        print(f"  ✓ Team memories written to teams/*/discussion.md")
        
    def tick_3_mentorship(self):
        """Tick 3: Mentors give feedback to top teams"""
        self.tick = 3
        print(f"\n=== TICK {self.tick}: MENTORSHIP ===")
        
        # Sort teams by score and take top 50
        top_teams = sorted(self.teams, key=lambda t: t["score"], reverse=True)[:50]
        
        mentors = [
            {"id": "mentor_tech", "type": "lead", "name": "Alex Tech"},
            {"id": "mentor_design", "type": "design", "name": "Sam Design"},
            {"id": "mentor_domain", "type": "domain", "name": "Jordan Domain"},
        ]
        
        print(f"3 mentors giving feedback to top 50 teams...")
        
        for mentor in mentors:
            mentor_dir = BASE_DIR / "mentors" / mentor["id"]
            mentor_dir.mkdir(parents=True, exist_ok=True)
            
            with open(mentor_dir / "feedback.md", "w") as f:
                f.write(f"# {mentor['name']} - Mentor Feedback\n\n")
                f.write(f"## Tick 3: Feedback to Top 50 Teams\n\n")
                
                for team in top_teams:
                    feedback = self._generate_feedback(mentor, team)
                    f.write(f"### {team['id']}\n")
                    f.write(f"{feedback}\n\n")
                    
                    # Write to team's mentor channel
                    team_dir = BASE_DIR / "teams" / team["id"]
                    channel_file = team_dir / f"p2m_{team['id']}_{mentor['id']}.md"
                    with open(channel_file, "w") as tf:
                        tf.write(f"# {team['id']} ↔ {mentor['name']}\n\n")
                        tf.write(f"**Mentor Feedback:**\n{feedback}\n")
                        
        print(f"  ✓ Mentors gave feedback to top 50 teams")
        print(f"  ✓ Mentor memories written to mentors/*/feedback.md")
        
    def _generate_feedback(self, mentor, team):
        """Generate realistic mentor feedback"""
        if mentor["type"] == "lead":
            return f"Tech review: Your {team['idea']} needs stronger OpenEnv integration. Use PyTorch 2.0+ features. Score: {team['score']}/100. Push for 2+ sponsor APIs."
        elif mentor["type"] == "design":
            return f"UX review: {team['idea']} has potential but clarify user flow. How does this solve real user problems? Consider accessibility."
        else:
            return f"Domain review: {team['idea']} - good domain fit. Ensure real-world impact. Validate with actual use cases. Sponsor API integration?"
            
    def tick_4_refinement(self):
        """Tick 4: Top 50 teams refine based on feedback"""
        self.tick = 4
        print(f"\n=== TICK {self.tick}: REFINEMENT ===")
        
        top_teams = sorted(self.teams, key=lambda t: t["score"], reverse=True)[:50]
        
        for team in top_teams:
            team_dir = BASE_DIR / "teams" / team["id"]
            with open(team_dir / "decisions.md", "w") as f:
                f.write(f"# {team['id']} - Key Decisions\n\n")
                f.write(f"## Tick 4: Refinement Based on Mentor Feedback\n\n")
                f.write(f"**Original Idea:** {team['idea']}\n")
                f.write(f"**Refined Approach:** Added sponsor API integration (Meta + Hugging Face)\n")
                f.write(f"**Tech Stack:** PyTorch 2.0, OpenEnv, Hugging Face Transformers\n")
                f.write(f"**Sponsor APIs:** {team['sponsor_apis'] + 1} integrated\n")
                
        print(f"  ✓ Top 50 teams refined their ideas")
        print(f"  ✓ Refinement logged to teams/*/decisions.md")
        
    def tick_5_live_pitches(self):
        """Tick 5: Live pitches - Top 50 pitch + Q&A"""
        self.tick = 5
        print(f"\n=== TICK {self.tick}: LIVE PITCHES (Top 50) ===")
        
        top_50 = sorted(self.teams, key=lambda t: t["score"], reverse=True)[:50]
        
        for rank, team in enumerate(top_50, 1):
            pitch = f"Team {team['id']} presents: {team['idea']}. We use Meta OpenEnv + PyTorch + Hugging Face APIs to solve real-world problems. Built in 48h by {len(team['members'])} people."
            team["pitch"] = pitch
            
            team_dir = BASE_DIR / "teams" / team["id"]
            with open(team_dir / "pitch.md", "w") as f:
                f.write(f"# {team['id']} - Pitch\n\n")
                f.write(f"## Tick 5: Live Pitch (Rank {rank}/50)\n\n")
                f.write(f"{pitch}\n\n")
                f.write(f"**Q&A:**\n")
                f.write(f"Judge: What's your differentiation?\n")
                f.write(f"A: We integrate 2+ sponsor APIs uniquely.\n")
                f.write(f"\n**Score after pitch:** {team['score']}/100\n")
                
        print(f"  ✓ Top 50 teams pitched")
        print(f"  ✓ Pitches stored in teams/*/pitch.md")
        
    def tick_6_semi_final(self):
        """Tick 6: Semi-final - Top 20 extended Q&A"""
        self.tick = 6
        print(f"\n=== TICK {self.tick}: SEMI-FINAL (Top 20) ===")
        
        top_20 = sorted(self.teams, key=lambda t: t["score"], reverse=True)[:20]
        
        for team in top_20:
            team_dir = BASE_DIR / "teams" / team["id"]
            with open(team_dir / "pitch.md", "a") as f:
                f.write(f"\n## Tick 6: Semi-Final Q&A\n")
                f.write(f"Extended 5-minute Q&A with judges.\n")
                f.write(f"Judge VC: Is this 48h buildable?\n")
                f.write(f"A: Yes, we have MVP working with OpenEnv.\n")
                f.write(f"Judge Product: What's the user impact?\n")
                f.write(f"A: Solves real problems for 1000+ users.\n")
                
        print(f"  ✓ Top 20 teams advanced to semi-final")
        
    def tick_7_final_pitches(self):
        """Tick 7: Final pitches - Top 10 with demos"""
        self.tick = 7
        print(f"\n=== TICK {self.tick}: FINAL PITCHES (Top 10) ===")
        
        top_10 = sorted(self.teams, key=lambda t: t["score"], reverse=True)[:10]
        
        for team in top_10:
            team_dir = BASE_DIR / "teams" / team["id"]
            with open(team_dir / "pitch.md", "a") as f:
                f.write(f"\n## Tick 7: Final Pitch with Demo\n")
                f.write(f"Full 5-minute presentation with demo.\n")
                f.write(f"**Demo:** Live OpenEnv environment running.\n")
                f.write(f"**Final Score:** {team['score']}/100\n")
                
        print(f"  ✓ Top 10 teams presented final pitches with demos")
        
    def tick_8_deliberation(self):
        """Tick 8: Judges deliberate and select winners"""
        self.tick = 8
        print(f"\n=== TICK {self.tick}: DELIBERATION ===")
        
        judges = [
            {"id": "judge_vc", "type": "vc", "name": "Taylor VC"},
            {"id": "judge_product", "type": "product", "name": "Morgan Product"},
            {"id": "judge_academic", "type": "academic", "name": "Casey Academic"},
        ]
        
        # Sort all teams by score
        all_teams_sorted = sorted(self.teams, key=lambda t: t["score"], reverse=True)
        top_3 = all_teams_sorted[:3]
        
        print(f"3 judges deliberating...")
        
        for judge in judges:
            judge_dir = BASE_DIR / "judges" / judge["id"]
            judge_dir.mkdir(parents=True, exist_ok=True)
            
            with open(judge_dir / "scores.md", "w") as f:
                f.write(f"# {judge['name']} - Scores\n\n")
                f.write(f"## Tick 8: Final Scoring\n\n")
                
                for rank, team in enumerate(all_teams_sorted[:10], 1):
                    score = team["score"]
                    f.write(f"### {rank}. {team['id']} - {team['idea']}\n")
                    f.write(f"**Score:** {score}/100\n")
                    f.write(f"**Sponsor APIs:** {team['sponsor_apis']}\n")
                    f.write(f"**Novelty:** {random.randint(20, 25)}/25\n")
                    f.write(f"**Feasibility:** {random.randint(20, 25)}/25\n")
                    f.write(f"**Impact:** {random.randint(20, 25)}/25\n")
                    f.write(f"**Differentiation:** {random.randint(15, 20)}/20\n")
                    f.write(f"**Sponsor Bonus:** +{team['sponsor_apis'] if team['sponsor_apis'] >= 2 else 0}\n\n")
                    
            with open(judge_dir / "deliberation.md", "w") as f:
                f.write(f"# {judge['name']} - Deliberation\n\n")
                f.write(f"## Final Decision\n\n")
                f.write(f"**Winner:** {top_3[0]['id']} - {top_3[0]['idea']}\n")
                f.write(f"**Score:** {top_3[0]['score']}/100\n")
                f.write(f"**Reasoning:** Best sponsor API integration, real-world impact, 48h buildable.\n")
                
        # Write top 3 to summary
        with open(BASE_DIR / "winner_summary.md", "w") as f:
            f.write(f"# Hackathon Results: {THEME}\n\n")
            f.write(f"**Participants:** {PARTICIPANTS}\n")
            f.write(f"**Teams Formed:** {len(self.teams)}\n")
            f.write(f"**Duration:** {DURATION}\n")
            f.write(f"**Sponsors:** {', '.join(SPONSORS)}\n\n")
            f.write(f"## Predicted Winner\n\n")
            f.write(f"**{top_3[0]['id']}** — {top_3[0]['idea']}\n")
            f.write(f"- Score: {top_3[0]['score']}/100\n")
            f.write(f"- Why it wins: Matches 'AI Agents' + 'Sponsor Integration' winning patterns\n\n")
            f.write(f"## Top 3\n\n")
            for i, team in enumerate(top_3, 1):
                f.write(f"{i}. {team['id']} - {team['idea']} ({team['score']}/100)\n")
            f.write(f"\n## Simulation Details\n\n")
            f.write(f"- 800 participants → {len(self.teams)} teams\n")
            f.write(f"- Top 50 → Live pitches + Q&A\n")
            f.write(f"- Top 20 → Semi-final Q&A\n")
            f.write(f"- Top 10 → Final pitches with demos\n")
            f.write(f"- All memories stored in: memories/hackathon_ai_rl_env_2026-05-04/\n")
            
        print(f"  ✓ Judges deliberated and selected winners")
        print(f"  ✓ Results written to winner_summary.md")
        print(f"  ✓ Judge memories written to judges/*/")
        
    def generate_build_guide(self):
        """Generate build guide for winner"""
        print(f"\n=== GENERATING BUILD GUIDE ===")
        
        winner = sorted(self.teams, key=lambda t: t["score"], reverse=True)[0]
        
        build_guide_dir = Path("/home/berzi/Documents/hackfish/build_guides/hackathon_ai_rl_env_2026-05-04")
        build_guide_dir.mkdir(parents=True, exist_ok=True)
        
        with open(build_guide_dir / "winner_build_guide.md", "w") as f:
            f.write(f"# Build Guide: How to Build the Winner\n\n")
            f.write(f"**Project:** {winner['idea']}\n")
            f.write(f"**Team:** {winner['id']}\n")
            f.write(f"**Score:** {winner['score']}/100\n\n")
            f.write(f"## Tech Stack\n\n")
            f.write(f"- **Framework:** Meta OpenEnv\n")
            f.write(f"- **ML Library:** PyTorch 2.0+\n")
            f.write(f"- **Models:** Hugging Face Transformers\n")
            f.write(f"- **Environment:** Gymnasium-style API\n")
            f.write(f"- **Containerization:** Docker\n")
            f.write(f"- **Language:** Python 3.10+\n\n")
            f.write(f"## Sponsor APIs to Integrate\n\n")
            f.write(f"1. **Meta OpenEnv API** - Core environment framework\n")
            f.write(f"2. **PyTorch** - Model training & inference\n")
            f.write(f"3. **Hugging Face Hub** - Model sharing & deployment\n\n")
            f.write(f"## 48h Schedule\n\n")
            f.write(f"- **Hour 1-4:** Project setup, OpenEnv init, repo structure\n")
            f.write(f"- **Hour 5-12:** Core RL environment implementation\n")
            f.write(f"- **Hour 13-20:** Sponsor API integrations (Meta + HF)\n")
            f.write(f"- **Hour 21-28:** Agent logic & reward functions\n")
            f.write(f"- **Hour 29-36:** Testing, demo preparation\n")
            f.write(f"- **Hour 37-44:** Polish, bug fixes, pitch deck\n")
            f.write(f"- **Hour 45-48:** Final pitch prep, submit\n\n")
            f.write(f"## Key Code Snippets\n\n")
            f.write(f"```python\n")
            f.write(f"import openenv\nfrom gymnasium import Env\n\n")
            f.write(f"class MyEnv(opencv.Env):\n")
            f.write(f"    def __init__(self):\n")
            f.write(f"        self.action_space = spaces.Discrete(4)\n")
            f.write(f"        self.observation_space = spaces.Box(low=0, high=1, shape=(8,))\n")
            f.write(f"```\n\n")
            f.write(f"## Pitch Deck\n\n")
            f.write(f"**30-sec:** {winner['idea']} - AI agents solving real problems with Meta OpenEnv.\n")
            f.write(f"**2-min:** Problem → Solution → Demo with OpenEnv + PyTorch.\n")
            f.write(f"**5-min:** Full pitch with business case and sponsor integration.\n")
            
        print(f"  ✓ Build guide generated at build_guides/hackathon_ai_rl_env_2026-05-04/winner_build_guide.md")
        
    def run_all(self):
        """Run complete simulation"""
        print(f"\n{'='*60}")
        print(f"HACKATHON SIMULATION: {THEME}")
        print(f"Participants: {PARTICIPANTS}")
        print(f"Teams: ~{TOTAL_TEAMS}")
        print(f"Sponsors: {', '.join(SPONSORS)}")
        print(f"{'='*60}\n")
        
        self.generate_participants()
        self.tick_1_idea_dump()
        self.tick_2_team_formation()
        self.tick_3_mentorship()
        self.tick_4_refinement()
        self.tick_5_live_pitches()
        self.tick_6_semi_final()
        self.tick_7_final_pitches()
        self.tick_8_deliberation()
        self.generate_build_guide()
        
        print(f"\n{'='*60}")
        print(f"SIMULATION COMPLETE")
        print(f"{'='*60}")
        print(f"\nAll agentic memories stored in:")
        print(f"  memories/hackathon_ai_rl_env_2026-05-04/")
        print(f"\n  - participants/*/ (idea.md, broadcast.md, team.md)")
        print(f"  - teams/*/ (discussion.md, decisions.md, pitch.md)")
        print(f"  - mentors/*/ (feedback.md)")
        print(f"  - judges/*/ (scores.md, deliberation.md)")
        print(f"\nWinner summary: memories/hackathon_ai_rl_env_2026-05-04/winner_summary.md")
        print(f"Build guide: build_guides/hackathon_ai_rl_env_2026-05-04/winner_build_guide.md")

if __name__ == "__main__":
    sim = HackathonSimulation()
    sim.run_all()
