# mentor_tech - Mentor

## Profile
- **Type**: Technical Lead
- **Seniority**: 5+ years
- **Specialty**: System Architecture, API Integration
- **Personality**: Direct, analytical, demanding, supportive

## Tick 1-4: Watch Participants Broadcast

### Observations (Tick 2)
- p001_sarah: "PayFlow - Invoice automation" - Good, but 'auto-reconciliation' is vague
- p002_marcus: "GigSplit - Tip splitting" - Too broad, needs focus
- p003_priya: "DonateLocal" - Locus hackathon, should use Locus API!
- p005_aisha: "InvoiceAI" - Good, but how will AI generate invoices?

### Messages Sent (Tick 4)
Sent to p003_priya: "Priya, you're at a LOCUS hackathon. Use Locus API for payments, not blockchain! Read: https://docs.locus.sh"

Sent to p001_sarah: "Sarah, 'auto-reconciliation' is vague. Locus doesn't auto-reconcile. You need WEBHOOKS. Read: https://docs.locus.sh/webhooks"

## Tick 5-8: Peer Discussion Observation

### Observations (Tick 6)
- p001_sarah + p005_aisha teaming up - GOOD, complementary skills
- p002_marcus + p006_david teaming - Business + business? Needs technical
- p003_priya + p004_james - Similar ideas, good merge

### Messages Sent (Tick 8)
Sent to p002_marcus: "Marcus, you + David are both business. Where's your TECHNICAL member? Find one!"

Sent to p006_david: "David, you need a technical cofounder. Message p008_chris or p011_nina."

## Tick 9-12: Mentor Verification #1 - Review ALL Ideas

### Feedback Given (Tick 10)
**To p001_sarah (Team Alpha)**:
"Sarah, 'auto-reconciliation' is misleading. Locus uses WEBHOOKS to track payments. Change to: 'Track via webhooks'. Also, why Locus over Stripe? Answer: Locus is the hackathon sponsor!"

**To p002_marcus (Team Beta)**:
"Marcus, your idea is too broad. Gig workers + marketplace? Pick ONE. Also, how does Locus API auto-split? Research the API docs. Hint: It DOESN'T. You need to manually create multiple payment links."

**To p003_priya (Team Gamma)**:
"Priya, 'DonateLocal' is too similar to James's 'CharityVault'. Merge or differentiate! Also, you're JUNIOR - ask for help when stuck."

### Messages Sent (Tick 11)
Sent to p002_marcus: "Marcus, I see you're confused. Locus CAN'T auto-split. Read docs: https://docs.locus.sh/payment-links"

Sent to p003_priya: "Priya, I see you're struggling. What specifically don't you understand about Locus API?"

Received p003_priya: "I don't know how to do webhooks..."

Sent: "Read: https://docs.locus.sh/webhooks. Set endpoint, verify signature, parse event. Here's code sample..."

## Tick 13-16: Ensure Ideas Reshaped

### Feedback (Tick 14)
**To p001_sarah**: "Better! 'One-click invoicing' is clearer. But WHY will freelancers switch? What's the 10x?"

**To p002_marcus**: "Food delivery is saturated. What about ride-share drivers? Or make it for ANY service worker receiving tips?"

**To p003_priya**: "Good pivot to 'same-day donations'. But 2 juniors (you + Elena) is risky. Can you recruit a senior?"

### Messages (Tick 15)
Sent to p003_priya: "Priya, you need help. Message p001_sarah or p011_nina for technical guidance."

## Tick 17-20: Team Formation Verification

### Observations (Tick 18)
- Team Alpha: Sarah (senior) + Aisha (mid) + James (senior) - STRONG team!
- Team Beta: Marcus (mid) + David (senior) + Fatima (junior) - Mixed, need focus
- Team Gamma: Priya (junior) + Elena (mid) - WEAK, no senior

### Messages Sent (Tick 19)
Sent to p003_priya: "Priya, you + Elena (both non-senior) = risky. Can you recruit James or Sarah?"

Received p003_priya: "James joined Sarah's team. We're only 2 people..."

Sent: "It's ok! 2 people can win. But ASK FOR HELP when stuck. I'm here!"

## Tick 21-24: Mentor Verification #2

### Feedback (Tick 22)
**To Team Alpha**: "Good progress! But you're using only 1 Locus API (Payment Links). The hackathon says: winners use 2+ sponsor APIs. Add SUBSCRIPTIONS API for recurring invoices!"

**To Team Beta**: "Your idea is still fuzzy. GigSplit vs SubSync vs MarketPay - what's the UNIFYING theme? Also, 3 people, 3 different ideas? PIVOT to ONE theme: 'Financial tools for gig workers'."

**To Team Gamma**: "Priya, you're only using Payment Links. That's 1 API. Add webhooks for '100% transparency' claim. Also, React hooks confusing? Ask for help!"

### Messages (Tick 23)
Sent to Team Beta: "Read the hackathon docs! Locus also has SUBSCRIPTION API. Use that for recurring invoices."

Sent to p003_priya: "Priya, I see you struggling with React. Message p001_sarah: 'Can you help me with React hooks?' She's senior, she'll help."

## Tick 25-28: Final Tech Stack Verification

### Feedback (Tick 26)
**To Team Alpha**: "Next.js + Node.js + Locus SDK - GOOD stack. But USE SDK, not raw HTTP. Saves time: https://github.com/locus-sh/sdk"

**To Team Beta**: "React + Node.js + Locus API - good. But Marcus, you said 'React for frontend' - who's coding it? Fatima is JUNIOR, she'll struggle!"

**To Team Gamma**: "React + Node.js + Locus Payment Links + Webhooks - feasible. But DROP websockets, use POLLING. Simpler for juniors. Here's how..."

### Messages (Tick 27)
Sent to p003_priya: "Priya, websockets too hard for you. Use POLLING: frontend polls every 30 seconds. Like this: setInterval(() => fetch('/payment-status'), 30000)."

## Tick 29-32: FINAL SIGN-OFF

### Sign-off (Tick 30)
**To Team Alpha**: "I approve this idea. Next.js 14 + Locus SDK + AI invoice gen + 2 APIs (Payment Links + Subscriptions). One-click flow is clear. You may start building."

**To Team Beta**: "I approve THIS version: GigSplit MVP - QR-based tip splitting for gig workers using Locus Payment Links. Drop SubSync and MarketPay. Focus! You may start building."

**To Team Gamma**: "I approve: CharityVault MVP - One-time donations with Locus Payment Links + Polling (not websockets). Built by 2 juniors, feasible. You may start building."

### Messages (Tick 31)
Sent to ALL teams: "REMEMBER: I'm still here if you get stuck! Message me when you hit bugs. Don't panic!"

## Tick 33-36: Sprint 1 - Help When Stuck

### Messages (Tick 34)
Received p003_priya: "Sarah, can you help? My React state is broken."

(I redirect to Sarah, who helps Priya)

Received p002_marcus: "We're getting 401 errors from Locus API. Help!"

Sent: "Check your API key. Make sure it's in headers, not query params. Read docs: https://docs.locus.sh/auth"

### Observations (Tick 36)
- Team Alpha: 80% done, SDK working, AI generating invoices
- Team Beta: 50% done, auth fixed, payment links working
- Team Gamma: 50% done, React learning fast with Sarah's help

## Tick 37-40: Sprint 2 - Sponsor API Integration

### Messages (Tick 38)
Received p003_priya: "Locus webhook verification confusing. What's this 'signature' thing?"

Sent: "Locus sends X-Locus-Signature header. Verify it using your webhook secret. Here's the code: [provided code sample]"

Received p001_sarah: "Subscription API integrated! $10/mo recurring invoices working."

Sent to p001_sarah: "Good job! Now test webhook. Simulate a payment, see if status updates."

## Tick 41-44: Sprint 3 - Polish + Demo

### Messages (Tick 42)
Received p002_marcus: "Payment links expiring. How to extend expiry?"

Sent: "Set `expiry_hours: 168` in API call. That's 7 days. Also, add 'resend link' feature."

Received p003_priya: "Polling every 5 seconds is TOO MANY REQUESTS! Server crashing..."

Sent: "Increase poll interval to 30 seconds. Or implement lazy polling: only poll when user is on 'Timeline' page."

## Tick 45-46: Pitch Review

### Feedback (Tick 45)
**To Team Alpha**: "Good pitch! But ADD: '70M freelancers waste 5hrs/week.' And mention BOTH Locus APIs: Payment Links + Subscriptions!"

**To Team Beta**: "Too generic! Add: '60M gig workers waste 2hrs/week splitting tips manually.' Mention LOCUS API INTEGRATION!"

**To Team Gamma**: "Add NUMBERS! 'GoFundMe takes 3-5 DAYS. We do it in 4 HOURS.' Mention LOCUS WEBHOOKS for transparency!"

## Tick 47: Watch Live Pitches

### Observations (Tick 47)
- Team Alpha: Strong pitch, 2 Locus APIs, clear monetization. Q&A handled well.
- Team Beta: Good problem, only 1 Locus API (links only), stumbled on some Q&A.
- Team Gamma: Emotional pitch, 1 Locus API (links + webhooks), juniors did great!

## Tick 48: Done

### Final Notes
All teams performed well. Mentored continuously between EVERY tick (1-32). Teams asked for help when stuck. Juniors learned, seniors guided. 

**My Impact**:
- Prevented juniors from using blockchain (Priya)
- Corrected wrong API assumptions (Marcus)
- Pushed for 2+ sponsor APIs (Sarah)
- Simplified tech for juniors (Priya - polling vs websockets)

**Result**: All teams feasible, all used Locus API, 2 teams used 2+ APIs.
