# p002_marcus_johnson - Participant

## Profile
- **Type**: Business
- **Seniority**: Mid
- **Specialty**: FinTech, Business Development
- **Personality**: Persuasive, optimistic, networked

## Tick 1-4: Idea Generation

### Idea (Tick 1)
**Broadcast** (10:00:02):
"Building **GigSplit** - Automatic tip splitting for gig workers across platforms. Worker earns $100, it auto-splits to gas, phone bill, savings. Set it once, done forever."

### Received Ideas (Tick 1-4)
- p001_sarah: "PayFlow - Invoice automation"
- p003_priya: "DonateLocal - Local charity donations"
- p005_aisha: "InvoiceAI - AI-generated invoices"
- p006_david: "SubSync - SaaS subscription management"

### Updated Idea (Tick 4)
"GigSplit - Auto-split tips for gig workers. Integrated with Locus API for instant payout to multiple recipients. 60M gig workers need this!"

## Tick 5-8: Peer Discussion

### Messages (Tick 5)
Sent to p006_david: "Your SubSync + GigSplit = complete gig worker finance suite. Team up?"

Received p006_david: "Yes! I have the business model expertise."

### Messages (Tick 7)
Sent to p009_fatima: "MarketPay + GigSplit = freelancer + marketplace integration?"

Received p009_fatima: "I'm in! Let's build together."

## Tick 9-12: Mentor Verification #1

### Mentor Feedback Received (Tick 10)
From mentor_tech: "Marcus, your idea is too broad. Gig workers + marketplace? Pick ONE. Also, how does Locus API auto-split? Research the API docs."

### Response (Tick 11)
**Mistake made**: "I think Locus can auto-split to multiple recipients automatically..."

Sent to mentor_tech: "Can Locus auto-split payments?"

Received mentor_tech: "NO! You need to manually create multiple payment links. Read the docs: https://docs.locus.sh"

### Pivot (Tick 12)
"GigSplit - Tip splitting SPECIFICALLY for food delivery drivers. Locus API creates separate payment links for each split. Simpler, focused."

## Tick 13-16: Idea Shaping

### Mentor Feedback (Tick 14)
From mentor_design: "Marcus, food delivery is saturated. What about ride-share drivers? Or make it for ANY service worker receiving tips?"

### Final Shaped Idea (Tick 16)
"GigSplit - Tip splitting for ALL service workers (rides, food, cleaning). Worker scans QR, selects split %, Locus generates multiple payment links. Simple, universal."

## Tick 17-20: Team Formation

### Messages (Tick 17)
Sent to p006_david: "I've refined GigSplit. Want to team up?"

Received p006_david: "Yes! I'll handle the business model + SaaS integration."

Sent to p009_fatima: "Need a business expert for marketplace integration?"

Received p009_fatima: "I'm in! Team Beta it is."

**Team Formed**: Marcus Johnson, David Kim, Fatima Al-Hassan → **Team Beta**

## Tick 21-24: Mentor Verification #2

### Mentor Feedback (Tick 22)
From mentor_domain: "Team Beta, your idea is still fuzzy. GigSplit vs SubSync vs MarketPay - what's the UNIFYING theme? Also, 3 people, 3 different ideas?"

### Team Discussion (Tick 23)
**Team Beta Discussion Log:**
- Marcus: "I think we should focus on gig workers only."
- David: "But SubSync is for SaaS users, not gig workers."
- Fatima: "MarketPay is for vendors. We're too scattered."

Received mentor_tech: "Pivot to ONE theme: 'Financial tools for gig workers' - all your ideas fit!"

### Pivot (Tick 24)
**Team Beta New Focus**: "GigWorker Suite - Financial tools for gig workers: tip splitting (GigSplit) + subscription management (SubSync) + marketplace payouts (MarketPay). All powered by Locus API."

## Tick 25-28: Final Idea Shaping

### Tech Stack Decision (Tick 26)
**Team Beta Discussion:**
- Marcus: "Let's use React for frontend."
- David: "And Node.js for backend."
- Fatima: "I'm junior, not sure how to integrate Locus API..."

Sent to mentor_tech: "How do we integrate Locus for multiple use cases?"

Received mentor_tech: "Read the API docs. You'll need: payment links for tips, subscriptions API for SaaS, and webhooks for marketplace payouts."

### Project Spec (Tick 28)
**GigWorker Suite Spec:**
- MVP: Tip splitting with QR code + Locus payment links
- Phase 2: Add subscription tracker for gig workers' software expenses
- Phase 3: Marketplace vendor payout integration
- Tech: React, Node.js, Locus API (payment links + subscriptions)

## Tick 29-32: Mentor Sign-off

### Mentor Feedback (Tick 30)
From mentor_tech: "Team Beta, your spec is too ambitious for 48h. Focus on MVP ONLY: Tip splitting with QR. Drop the rest."

From mentor_design: "QR code experience needs to be seamless. Test it on mobile!"

### Final Sign-off (Tick 32)
From mentor_domain: "I approve THIS version: GigSplit MVP - QR-based tip splitting for gig workers using Locus payment links. Build only this. You may start building."

**MENTOR APPROVAL RECEIVED** ✓

## Tick 33-36: Sprint 1 - Core Features

### Development Log (Tick 33)
**Team Beta Collaboration:**
- Marcus: "I'll set up the React frontend."
- David: "I'll handle Node.js backend + Locus API integration."
- Fatima: "I'm stuck on React components... can someone help?"

Sent to p001_sarah: "Sarah, can you help Fatima with React? She's struggling."

Received p001_sarah: "Sure! Fatima, use functional components + hooks. Here's a code snippet..."

### Progress (Tick 35)
- Marcus: "Frontend is 60% done. QR code generator working!"
- David: "Locus API integration... having issues. Getting 401 errors."

Sent to mentor_tech: "We're getting 401 errors from Locus API. Help!"

Received mentor_tech: "Check your API key. Make sure it's in headers, not query params. Read docs: https://docs.locus.sh/auth"

### End of Sprint 1 (Tick 36)
**Status**: 
- Frontend: 80% (Marcus + Fatima with Sarah's help)
- Backend: 50% (David stuck on auth)
- Locus Integration: 40% (struggling with auth)

## Tick 37-40: Sprint 2 - Sponsor API Integration

### Development Log (Tick 37)
**Team Beta Discussion:**
- David: "Auth fixed! Now creating payment links..."
- Marcus: "QR code scanning working. Testing with real phones."
- Fatima: "I'm learning fast! Built the split percentage UI."

### Locus API Integration (Tick 39)
**Success!** 
- David: "Payment links being created successfully!"
- Marcus: "Scanning QR → auto-fills tip amount → generates 3 payment links (worker, gas, savings)."

Sent to mentor_tech: "Locus integration complete! Tips split to 3 recipients."

Received mentor_tech: "Good job. Now test the ACTUAL payment flow. Do real test payments."

## Tick 41-44: Sprint 3 - Polish + Demo

### Development Log (Tick 41)
**Team Beta Discussion:**
- Marcus: "UI looking good. Need to add 'split history' page."
- David: "Webhook handler for payment status updates - done!"
- Fatima: "I built the dashboard! Shows all past splits."

### Bug Appears (Tick 43)
**Problem**: "Payment links expire after 24h. Tips sometimes not claimed in time!"

Sent to mentor_tech: "Payment links expiring. How to extend expiry?"

Received mentor_tech: "Set `expiry_hours: 168` in API call. That's 7 days. Also, add 'resend link' feature."

### Final Polish (Tick 44)
**Status**:
- MVP Complete: QR → Split % → 3 Payment Links → Auto-expire in 7 days
- Demo Ready: Can scan QR, split $50 tip (70% worker, 20% gas, 10% savings)
- Bug Fixed: Expiry extended, resend link added

## Tick 45-46: Pitch Prep

### Draft Pitch (Tick 45)
**Team Beta Pitch Draft:**
"GigSplit - Tip splitting for gig workers. Scan QR, select split %, get paid instantly via Locus. No more manual splits, no more IOUs."

### Mentor Review (Tick 46)
Sent to mentor_design: "Can you review our pitch? It's: 'GigSplit - Tip splitting for gig workers...'"

Received mentor_design: "Too generic! Add: '60M gig workers waste 2hrs/week splitting tips manually. We save them time.' Also mention LOCUS API INTEGRATION!"

### Final Pitch (Tick 46)
"GigSplit saves 60M gig workers 2hrs/week on manual tip splitting. Scan QR, auto-split to gas/savings/phone bill via Locus API. Built in 48h."

## Tick 47: Live Pitch + Q&A

### Pitch (Tick 47, 10:00:00)
**Team Beta - GigSplit**
"60M gig workers waste 2 hours every week manually splitting tips. GigSplit solves this: Scan QR code → Select split % → Locus API generates 3 payment links → Workers get paid in minutes. Built in 48 hours."

### Judge Q&A (Tick 47, 10:02:00)
**Judge_vc asks**: "What's your monetization model?"

**Answer**: "We take 1% transaction fee on each split. 60M workers × average $500 tips/month = $30B processed. 1% = $300M revenue."

**Judge_product asks**: "Why would gig workers use this over Venmo?"

**Answer**: "Venmo doesn't auto-split. Workers manually send to multiple people. We automate the entire flow with ONE scan."

**Judge_academic asks**: "How do you handle payment link expiry?"

**Answer**: "We set expiry to 7 days via Locus API. Also added 'resend link' feature if expired. Mentor_tech helped us fix this!"

**Score**: 19/25
- Novelty: 3
- Feasibility: 5
- Impact: 4
- Differentiation: 3
- Sponsor Integration: 4 (Locus payment links only, need 2+ APIs for bonus)

## Tick 48: Deliberation

### Final Score
**Team Beta - GigSplit**: 19/25

**Judge Deliberation Notes** (from judges/judge_vc/deliberation.md):
"Team Beta had a clear problem (tip splitting), but only used 1 sponsor API (Locus payment links). Needed 2+ for bonus points. Good execution, but not winner material."

**Result**: 3rd place (behind Team Alpha - PayFlow 21/25 and Team Gamma - CharityVault 21/25)
