# p003_priya_sharma - Participant

## Profile
- **Type**: Technical
- **Seniority**: Junior
- **Specialty**: Frontend, React
- **Personality**: Eager, anxious, hardworking

## Tick 1-4: Idea Generation

### Idea (Tick 1)
**Broadcast** (10:00:03):
"Building **DonateLocal** - Donation platform for local charitable causes. Give to neighbors, not big charities. 100% transparent where money goes."

### Mistake (Tick 3)
**Confusion**: "I'm not sure how to make donations transparent. Maybe use blockchain?"

Sent to mentor_tech: "Should I use blockchain for donation tracking?"

Received mentor_tech: "NO! You're at a LOCUS hackathon. Use Locus API for payment tracking. Blockchain is overkill and won't work in 48h."

### Pivot (Tick 4)
"DonateLocal - Local donations via Locus payment links. Donors see exactly when local charity receives funds. Simple, transparent."

## Tick 5-8: Peer Discussion

### Messages (Tick 5)
Received p004_james: "I have CharityVault idea. Similar to yours?"

Sent to p004_james: "Yes! Let's discuss."

### Messages (Tick 7)
Received p007_elena: "I have TipJar Pro. What if we combine charity + tips?"

Accepted: "Yes! Charity + tips = good combo."

## Tick 9-12: Mentor Verification #1

### Mentor Feedback (Tick 10)
From mentor_design: "Priya, 'DonateLocal' is too similar to James's 'CharityVault'. Merge or differentiate!"

### Confusion (Tick 11)
"I don't understand... how are we different? James, what's your UVP?"

Received p004_james: "Mine is 'transparent tracking'. Yours is 'local focus'. Let's merge!"

Sent to mentor_design: "We merged! Team Gamma = CharityVault + DonateLocal = 'Transparent local giving'."

Received mentor_design: "Better! Now focus on the 'transparency' part. How?"

### Pivot (Tick 12)
"Team Gamma Idea: **CharityVault** - Transparent local donations. Donors see EXACTLY when charity receives Locus payment. 100% transparency via webhooks."

## Tick 13-16: Idea Shaping

### Mentor Feedback (Tick 14)
From mentor_domain: "Priya, 'local' is still vague. What's the 10x over GoFundMe?"

### Struggle (Tick 15)
"I don't know what's the 10x... can someone help?"

Sent to p001_sarah: "Sarah, can you help? What's the 10x for charity donations?"

Received p001_sarah: "Focus on SPEED. GoFundMe takes 3-5 days. You can do SAME DAY via Locus."

### Reshaped Idea (Tick 16)
"CharityVault - Same-day local donations. Donor gives → Locus payment link → charity receives in HOURS (not days). 100% transparent via webhooks. Speed + transparency."

## Tick 17-20: Team Formation

**Team Formed**: Priya Sharma, Elena Rodriguez → **Team Gamma**

### Messages (Tick 18)
"Team Gamma is me (frontend) + Elena (design). We need a senior... can we recruit James?"

Sent to p004_james: "Join Team Gamma as senior dev?"

Received p004_james: "I'm already with Sarah's team. Can't join. Good luck!"

### Team Discussion (Tick 19)
**Team Gamma Discussion Log:**
- Priya: "I'm junior, worried I can't build this alone with just Elena..."
- Elena: "Don't worry! I'll handle design, you code. We can ask mentors for help."

## Tick 21-24: Mentor Verification #2

### Mentor Feedback (Tick 22)
From mentor_tech: "Team Gamma, you're only 2 people. That's risky for 48h build. Also, 'same-day' is good but HOW? Explain your tech."

### Panic (Tick 23)
"We don't know how to do webhooks! I've never done them..."

Sent to mentor_tech: "How do Locus webhooks work? We're stuck!"

Received mentor_tech: "Read: https://docs.locus.sh/webhooks. Set endpoint, verify signature, parse event. Here's code sample..."

### New Plan (Tick 24)
"Team Gamma Tech Stack: React frontend (Priya), Node.js backend (Priya + mentor help), Locus Payment Links + Webhooks (Elena designs flow)."

## Tick 25-28: Final Idea Shaping

### Tech Struggle (Tick 26)
**Problem**: "React hooks confusing... useState not updating properly."

Sent to p005_aisha: "Aisha, can you help? My React state is broken."

Received p005_aisha: "Sure! You're mutating state directly. Use setState. Here's the fix..."

### Mentor Check (Tick 27)
Sent to mentor_tech: "We have: React, Node.js, Locus Payment Links + Webhooks. Is this feasible in 48h?"

Received mentor_tech: "YES! But simplify: Only do ONE-TIME donations (not recurring). Focus on webhook dashboard. Drop anything else."

### Final Spec (Tick 28)
"CharityVault MVP: React frontend, Node.js backend, Locus ONE-TIME payment links, webhook dashboard showing real-time payment status. Donors see exact timeline: Created → Sent → Received."

## Tick 29-32: Mentor Sign-off

### Mentor Feedback (Tick 30)
From mentor_design: "Elena's UI mockups look great! But 'real-time dashboard' needs polling or websockets. Can you do that?"

### Struggle (Tick 31)
"We don't know websockets... too hard for juniors."

Sent to mentor_tech: "Websockets too hard. What's simpler?"

Received mentor_tech: "Use POLLING. Frontend polls every 5 seconds: 'GET /payment-status'. Simple, works."

### Final Sign-off (Tick 32)
From mentor_tech: "Team Gamma APPROVED. React + Node.js + Locus Payment Links + Polling (not websockets). MVP focused. You may start building."

**MENTOR APPROVAL RECEIVED** ✓

## Tick 33-36: Sprint 1 - Core Features

### Development Log (Tick 33)
**Team Gamma Collaboration:**
- Priya: "Setting up React... confused with useEffect dependencies."
- Elena: "I'll create the donation form in Figma."

### Help Needed (Tick 34)
Sent to p001_sarah: "Sarah, useEffect with empty deps array... when does it run?"

Received p001_sarah: "Runs ONCE on mount. If you want it to run on state change, add state to deps array. Like this: useEffect(() => {...}, [state])"

### Progress (Tick 35)
- Priya: "React frontend 50% done! Donation form working."
- Elena: "Design implemented! Looks beautiful."

### Bug (Tick 36)
**Problem**: "Locus payment link created but don't know when charity clicks it..."

Sent to mentor_tech: "How to know when payment link is clicked?"

Received mentor_tech: "You can't. But you CAN poll: 'GET /payment-link-status'. Or wait for webhook event 'payment_link.visited'. Use polling, it's simpler."

## Tick 37-40: Sprint 2 - Sponsor API Integration

### Development Log (Tick 37)
- Priya: "Locus Payment Link API working! Can create link for $50 donation."
- Elena: "Adding 'Donation Timeline' UI component."

### Confusion (Tick 38)
"I don't understand Locus webhook verification... what's this 'signature' thing?"

Sent to mentor_tech: "Locus webhook signature confusing. Help!"

Received mentor_tech: "Locus sends X-Locus-Signature header. You verify it using your webhook secret. Here's the code:
```javascript
const signature = req.headers['x-locus-signature'];
const expected = crypto.createHmac('sha256', WEBHOOK_SECRET).update(JSON.stringify(req.body)).digest('hex');
if (signature !== expected) return res.status(401).send('Invalid');
```"

### Integration Complete (Tick 40)
"Locus Integration Done! Payment Links + Webhook Verification + Polling Status Check. Team Gamma is ready!"

## Tick 41-44: Sprint 3 - Polish + Demo

### Development Log (Tick 41)
- Priya: "Adding 'Donation Timeline' page. Shows: Created → Sent → Received."
- Elena: "Polishing UI. Making it mobile-responsive."

### Bug (Tick 43)
**Problem**: "Polling every 5 seconds is TOO MANY REQUESTS! Server crashing..."

Sent to mentor_tech: "Polling killing our server. Help!"

Received mentor_tech: "Increase poll interval to 30 seconds. Or implement lazy polling: only poll when user is on 'Timeline' page. Here's how..."

### Demo Ready (Tick 44)
"CharityVault Demo Ready! Features: Donation form → Locus payment link → Polling checks status → Timeline shows: Created (0min) → Sent (2min) → Received (4min). All in 48h!"

## Tick 45-46: Pitch Prep

### Draft Pitch (Tick 45)
"CharityVault - Same-day local donations. Donors give, charity receives in HOURS via Locus. 100% transparent timeline."

### Mentor Review (Tick 46)
Sent to mentor_design: "Can you review our pitch? 'CharityVault - Same-day donations...'"

Received mentor_design: "Add NUMBERS! 'GoFundMe takes 3-5 DAYS. We do it in 4 HOURS.' Also mention LOCUS WEBHOOKS for transparency!"

### Final Pitch (Tick 46)
"CharityVault saves 2 days per donation. GoFundMe: 3-5 days. Us: 4 HOURS via Locus API. Donor gives → Payment link → Charity receives in 4 hours. 100% transparent timeline via Locus webhooks. Built by 2 juniors in 48h!"

## Tick 47: Live Pitch + Q&A

### Pitch (Tick 47, 10:10:00)
**Team Gamma - CharityVault**
"GoFundMe takes 3-5 DAYS to deliver funds. CharityVault does it in 4 HOURS. Donor gives → Locus payment link → Charity receives in 4 hours. 100% transparent: donors see exact timeline via Locus webhooks. Built by 2 juniors in 48 hours."

### Judge Q&A (Tick 47, 10:12:00)
**Judge_vc asks**: "How do you handle payment failures?"

**Answer**: "Locus webhook sends 'payment.failed' event. We show it in timeline, donor can resend link. Mentor_tech helped us implement this!"

**Judge_product asks**: "Why would charities use this over GoFundMe?"

**Answer**: "Speed! Charities wait 3-5 days with GoFundMe. We deliver in 4 HOURS. Also, we're LOCAL only - community-focused, not global."

**Judge_academic asks**: "How do you verify charities are real?"

**Answer**: "We... um... we don't yet. It's an MVP. Future feature would be charity verification via government API."

**Score**: 21/25
- Novelty: 4
- Feasibility: 5
- Impact: 5
- Differentiation: 3
- Sponsor Integration: 4 (Locus Payment Links + Webhooks, need 2+ APIs for bonus but only using 1 suite)

## Tick 48: Results

**Final Score**: 21/25

**Judge Deliberation** (from judges/judge_product/deliberation.md):
"Team Gamma wins tie-breaker with Team Alpha. Why? HIGHER IMPACT (5 vs 4). Charity donations help people in need. Freelancer invoicing is convenience, not necessity. Also, built by 2 JUNIORS - impressive!"

**RESULT: 1st Place (tied with Team Alpha, won on impact)**
