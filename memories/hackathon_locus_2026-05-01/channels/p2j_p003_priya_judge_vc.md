# p2j_p003_priya_judge_vc.md#

## Participant: p003_priya_sharma (Team Gamma - CharityVault)
## Judge: judge_vc (VC/Investor)

---

### Tick 47: Live Pitch + Q&A.

**Tick 47, 10:10:00 - Pitch:**
"GoFundMe takes 3-5 DAYS to deliver funds. CharityVault does it in 4 HOURS. Donor gives → Locus payment link → Charity receives in 4 hours. 100% transparent: donors see exact timeline via Locus webhooks. Built by 2 juniors in 48 hours."

---

### Judge Question (Tick 47, 10:12:00).

**Judge_vc asks:**
"How do you handle payment failures? What if the charity never receives the funds?"

---

### Participant Answer (Tick 47, 10:12:15).

**Priya (p003) answers:**
"Locus webhook sends 'payment.failed' event. We show it in the timeline with a RED indicator. Donor can immediately 'Resend Link' button. Mentor_tech helped us implement this webhook verification! Also, Locus has 99.9% uptime, failures are rare."

---

### Judge Follow-up (Tick 47, 10:12:30).

**Judge_vc asks:**
"Your timeline shows 'Received in 4 hours'. How do you GUARANTEE this? What if Locus is slow?"

---

### Participant Answer (Tick 47, 10:12:45).

**Priya (p003) answers:**
"We... um... we can't guarantee 4 hours. It's based on Locus's typical processing time. But we DO show real-time status: Created (0min) → Sent (2min) → Received (4min). If it takes longer, donors see it in real-time. Mentor_design suggested adding 'Typical time: 4 hours' to manage expectations."

---

### Judge Scoring (Tick 48).

**Judge_vc scores:**
- Novelty: 4/5 (Same-day vs 3-5 days is novel)
- Feasibility: 5/5 (Built MVP in 48h, 2 juniors!)
- Defensibility: 4/5 (Locus dependency is risk, but webhooks = moat)
- Sponsor Integration: 4/5 (Locus Payment Links + Webhooks, need 2+ APIs for bonus but only using 1 suite)
- **Subtotal: 17/20 (+4 bonus = 21/25)**

**Comments:**
"Good emotional pitch. 2 juniors building in 48h is impressive. Only 1 Locus API (links + webhooks count as 1). No bonus points. Impact is HIGH (charity = good)."

---

*End of p2j_p003_priya_judge_vc.md*
