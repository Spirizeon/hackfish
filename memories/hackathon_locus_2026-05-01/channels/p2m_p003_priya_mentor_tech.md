# p2m_p003_priya_mentor_tech.md#

## Participant: p003_priya_sharma (Junior, Technical)
## Mentor: mentor_tech (Senior, Technical Lead)

---

### Tick 1-4: Watch Ideas Form.

**Tick 1, 10:00:03 - Participant broadcasts:**
"Building **DonateLocal** - Donation platform for local charitable causes. Give to neighbors, not big charities. 100% transparent where money goes."

**Mentor observes (Tick 2):**
"Priya's idea is good but 'transparency' is vague. Also, she's at a LOCUS hackathon - should use Locus API!"

**Message sent (Tick 4, 10:04:00):**
"Priya, you're at a LOCUS hackathon. Use Locus API for payments, not blockchain! Read: https://docs.locus.sh"

---

### Tick 5-8: Peer Discussion.

**Tick 6, 10:06:00 - Mentor observes:**
"Priya + James merging ideas (DonateLocal + CharityVault) = good! But Priya is JUNIOR - needs help."

**Message sent (Tick 8, 10:08:00):**
"Priya, you + Elena (both non-senior) = risky. Recruit James or Sarah for technical guidance!"

---

### Tick 9-12: Mentor Verification #1.

**Tick 10, 10:10:00 - Mentor feedback:**
"Priya, 'DonateLocal' is too similar to James's 'CharityVault'. MERGE or differentiate CLEARLY! Also, I see you're struggling - ASK FOR HELP!"

**Tick 11, 10:11:00 - Participant responds:**
"I don't know how to do webhooks... can someone help?"

**Mentor reply (Tick 11, 10:11:30):**
"Read: https://docs.locus.sh/webhooks. Set endpoint, verify signature, parse event. Here's code sample:
```javascript
app.post('/webhook', (req, res) => {
  const sig = req.headers['x-locus-signature'];
  // verify + parse event
});
```"

---

### Tick 13-16: Idea Shaping.

**Tick 14, 10:14:00 - Mentor feedback:**
"Better pivot to 'same-day donations'. But HOW? Explain your tech."

**Tick 15, 10:15:00 - Participant struggles:**
"I don't know what's the 10x... can someone help?"

**Mentor redirects (Tick 15, 10:15:30):**
"Message p001_sarah: 'Can you help? What's the 10x for charity donations?' She's senior, she'll help."

**Tick 16, 10:16:00 - Participant reshapes:**
"CharityVault - Same-day local donations. Donors see EXACTLY when charity receives Locus payment. 100% transparency via webhooks."

---

### Tick 17-20: Team Formation.

**Tick 18, 10:18:00 - Mentor observes:**
"Team Gamma: Priya (junior) + Elena (mid) = WEAK, no senior. Should recruit James..."

**Tick 19, 10:19:00 - Participant messages:**
"Can we recruit James as senior dev?"

**Mentor reply:**
"James joined Sarah's team. But don't worry! 2 people can win. ASK FOR HELP when stuck. I'm here!"

---

### Tick 21-24: Mentor Verification #2.

**Tick 22, 10:22:00 - Mentor feedback:**
"Team Gamma, you're only 2 people. That's risky for 48h build. Also, 'same-day' is good but HOW? Explain your tech."

**Tick 23, 10:23:00 - Participant panics:**
"We don't know how to do webhooks! I've never done them..."

**Mentor reply:**
"Read docs! Set endpoint, verify X-Locus-Signature header. Here's the code again..."

**Tick 24, 10:24:00 - Participant new plan:**
"Team Gamma Tech Stack: React (Priya), Node.js (Priya + mentor help), Locus Payment Links + Webhooks (Elena designs flow)."

---

### Tick 25-28: Final Tech Stack.

**Tick 26, 10:26:00 - Participant struggles:**
"React hooks confusing... useState not updating properly."

**Mentor redirects:**
"Message p005_aisha: 'Can you help with React hooks?' She's mid-level, she'll help!"

**Tick 27, 10:27:00 - Participant asks:**
"We have: React, Node.js, Locus Payment Links + Webhooks. Is this feasible in 48h?"

**Mentor reply:**
"YES! But simplify: Only do ONE-TIME donations (not recurring). Focus on webhook dashboard. Drop anything else."

---

### Tick 29-32: Mentor Sign-off.

**Tick 30, 10:30:00 - Mentor sign-off:**
"Team Gamma APPROVED. React + Node.js + Locus Payment Links + Polling (not websockets). MVP focused. You may start building."

**Tick 31, 10:31:00 - Participant confirms:**
"MENTOR APPROVAL RECEIVED ✓ Ready to build!"

---

### Tick 33-36: Sprint 1 - Help When Stuck.

**Tick 34, 10:34:00 - Participant asks:**
"Sarah, can you help? My React state is broken."

**Mentor observes:**
"I redirect to Sarah, who helps Priya with useState."

**Tick 36, 10:36:00 - Progress update:**
"React frontend 50% done! Donation form working. But Locus payment link created, don't know when charity clicks it..."

**Mentor reply:**
"You can't know when clicked. But you CAN poll: 'GET /payment-link-status'. Or wait for webhook event 'payment_link.visited'. Use polling, it's simpler."

---

### Tick 37-40: Sprint 2 - API Integration.

**Tick 38, 10:38:00 - Participant confused:**
"I don't understand Locus webhook verification... what's this 'signature' thing?"

**Mentor reply:**
"Locus sends X-Locus-Signature header. You verify it using your webhook secret. Here's the code:
```javascript
const signature = req.headers['x-locus-signature'];
const expected = crypto.createHmac('sha256', WEBHOOK_SECRET)
  .update(JSON.stringify(req.body)).digest('hex');
if (signature !== expected) return res.status(401).send('Invalid');
```"

**Tick 40, 10:40:00 - Success:**
"Locus Integration Done! Payment Links + Webhook Verification + Polling Status Check. Team Gamma is ready!"

---

### Tick 41-44: Sprint 3 - Polish.

**Tick 43, 10:43:00 - Participant struggles:**
"Polling every 5 seconds is TOO MANY REQUESTS! Server crashing..."

**Mentor reply:**
"Increase poll interval to 30 seconds. Or implement lazy polling: only poll when user is on 'Timeline' page. Here's how..."

**Tick 44, 10:44:00 - Demo ready:**
"CharityVault Demo Ready! Features: Donation form → Locus payment link → Polling checks status → Timeline shows: Created (0min) → Sent (2min) → Received (4min). All in 48h!"

---

### Tick 45-46: Pitch Prep.

**Tick 45, 10:45:00 - Participant drafts pitch:**
"CharityVault - Same-day local donations. Donors give, charity receives in HOURS via Locus. 100% transparent timeline."

**Mentor reviews (Tick 46):**
"Add NUMBERS! 'GoFundMe takes 3-5 DAYS. We do it in 4 HOURS.' Also mention LOCUS WEBHOOKS for transparency!"

**Tick 46, 10:46:00 - Final pitch:**
"CharityVault saves 2 days per donation. GoFundMe: 3-5 days. Us: 4 HOURS via Locus API. Donor gives → Payment link → Charity receives in 4 hours. 100% transparent timeline via Locus webhooks. Built by 2 juniors in 48h!"

---

### Tick 47: Live Pitch + Q&A.

**Tick 47, 10:47:00 - Pitch:**
"GoFundMe takes 3-5 DAYS to deliver funds. CharityVault does it in 4 HOURS. Donor gives → Locus payment link → Charity receives in 4 hours. 100% transparent: donors see exact timeline via Locus webhooks. Built by 2 juniors in 48 hours."

**Judge_vc asks:**
"How do you handle payment failures?"

**Participant answers:**
"Locus webhook sends 'payment.failed' event. We show it in timeline, donor can resend link. Mentor_tech helped us implement this!"

**Score: 21/25** (Tied for 1st!)

---

### Tick 48: Results.

**Final Score: 21/25**

**Judge Deliberation:**
"Team Gamma wins tie-breaker with Team Alpha. Why? HIGHER IMPACT (5 vs 4). Charity donations help people in need. Freelancer invoicing is convenience, not necessity. Also, built by 2 JUNIORS - impressive!"

**RESULT: 1st Place (tied with Team Alpha, won on impact)**

---

*End of p2m_p003_priya_mentor_tech.md*
