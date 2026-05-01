# p2m_p001_sarah_mentor_tech.md

## Participant: p001_sarah_chen (Senior, Technical)
## Mentor: mentor_tech (Senior, Technical Lead)

---

### Tick 1-4: Watch Ideas Form

**Tick 1, 10:00:01 - Participant broadcasts:**
"I'm building PayFlow - Invoice automation for freelancers with Locus payment links."

**Mentor observes (Tick 2):**
"Sarah's idea is good but 'auto-reconciliation' is vague. Locus doesn't auto-reconcile, it uses WEBHOOKS."

**Message sent (Tick 4, 10:04:00):**
"Sarah, 'auto-reconciliation' is misleading. Locus uses WEBHOOKS to track payments. Change to: 'Track via webhooks'. Also, why Locus over Stripe? Answer: Locus is the hackathon sponsor!"

---

### Tick 5-8: Peer Discussion

**Tick 5, 10:05:00 - Participant messages:**
"Your InvoiceAI + my PayFlow = perfect match! Team up?"

**Mentor observes (Tick 6):**
"Good! Sarah (senior) + Aisha (mid) = complementary. James (senior design) joins = STRONG team."

---

### Tick 9-12: Mentor Verification #1

**Tick 10, 10:10:00 - Mentor feedback:**
"Sarah, 'auto-reconciliation' is misleading. Locus uses WEBHOOKS to track payments. Change to: 'Track via webhooks'. Also, why Locus over Stripe?"

**Tick 11, 10:11:00 - Participant response:**
"I think Locus auto-reconciles payments..."

**Mentor reply (Tick 11, 10:11:30):**
"LOL NO! You need webhooks. Read: https://docs.locus.sh/webhooks"

**Tick 12, 10:12:00 - Participant pivot:**
"PayFlow - Generate invoices, send Locus payment links, track via WEBHOOKS (not auto-reconciliation). Clearer, feasible."

---

### Tick 13-16: Idea Shaping

**Tick 14, 10:14:00 - Mentor feedback:**
"Sarah, 'one-click invoicing' is clearer. But WHY will freelancers switch? What's the 10x?"

**Tick 16, 10:16:00 - Participant reshapes:**
"PayFlow - ONE-CLICK invoicing. Describe work → AI generates invoice → Locus payment link sent → webhook tracks payment. From 'done' to 'paid' in 1 click."

---

### Tick 17-20: Team Formation

**Tick 17, 10:17:00 - Mentor observes:**
"Team Alpha formed: Sarah (senior) + Aisha (mid) + James (senior). STRONG team!"

**Tick 18, 10:18:00 - No issues, team is solid.**

---

### Tick 21-24: Mentor Verification #2

**Tick 22, 10:22:00 - Mentor feedback:**
"Team Alpha, 'one-click' is good but you're using only 1 Locus API (Payment Links). The hackathon says: winners use 2+ sponsor APIs. Add SUBSCRIPTIONS API for recurring invoices!"

**Tick 23, 10:23:00 - Participant asks:**
"We use Locus Payment Links. What's the 2nd API?"

**Mentor reply:**
"Read the hackathon docs! Locus also has SUBSCRIPTION API. Use that for recurring invoices."

**Tick 24, 10:24:00 - Participant pivot:**
"PayFlow - One-click invoicing with Locus PAYMENT LINKS (one-time) + SUBSCRIPTIONS API (recurring). Two APIs! Mentor_domain helped us."

---

### Tick 25-28: Final Tech Stack

**Tick 26, 10:26:00 - Team discussion:**
- Sarah: "Next.js 14 + Tailwind."
- Aisha: "Backend: Node.js + Express + GPT-4 + Locus SDK."
- James: "I'll use Figma, code in Tailwind."

**Tick 27, 10:27:00 - Participant asks:**
"Is Next.js + Node.js right for Locus API integration?"

**Mentor reply:**
"Yes, good stack. Use Locus SDK properly: `locus.paymentLinks.create()` not raw HTTP. Saves time: https://github.com/locus-sh/sdk"

---

### Tick 29-32: Mentor Sign-off

**Tick 30, 10:30:00 - Mentor sign-off:**
"Team Alpha, your spec is solid. Next.js + Locus SDK + AI invoice gen + 2 APIs (Payment Links + Subscriptions). One-click flow is clear. APPROVED."

**Tick 31, 10:31:00 - Participant confirms:**
"MENTOR APPROVAL RECEIVED ✓ Ready to build!"

---

### Tick 33-36: Sprint 1 - Help When Stuck

**Tick 35, 10:35:00 - Participant progress:**
"Locus SDK working! Payment links created in 1 line. AI generating invoices perfectly."

**Tick 36, 10:36:00 - No help needed, progress smooth.**

---

### Tick 37-40: Sprint 2 - API Integration

**Tick 39, 10:39:00 - Participant success:**
"Locus Subscription API integrated! $10/mo recurring invoices working. GPT-4 + 2 Locus APIs = winning combo!"

---

### Tick 41-44: Sprint 3 - Polish

**Tick 43, 10:43:00 - No issues, demo ready.**

---

### Tick 45-46: Pitch Prep

**Tick 46, 10:46:00 - Mentor reviews pitch:**
"Good pitch! But ADD: '70M freelancers waste 5hrs/week.' And mention BOTH Locus APIs: payment links + subscriptions!"

---

### Tick 47: Live Pitch

**Tick 47, 10:47:00 - Mentor watches:**
"Strong pitch, 2 Locus APIs mentioned, clear monetization. Q&A handled well. Ready to win!"

---

*End of p2m_p001_sarah_mentor_tech.md*
