# Search Intent Taxonomy

Reference document for the `keyword-cluster` skill. Defines the four intent types, their modifier signals, and how they map to content types and funnel stages.

## The Four Intent Types

### 1. Informational

The searcher wants to learn something. They have a question or need to understand a concept.

**Funnel stage**: Top of funnel (awareness)

**Modifier signals**:
- Question words: what, how, why, when, where, who, can, does, is
- Learning words: guide, tutorial, examples, tips, ideas, explained, definition, meaning
- Process words: steps, ways, methods, strategies, techniques, process
- Comparison-adjacent: difference between, vs (when comparing concepts, not products)

**Examples**:
- "what is keyword clustering"
- "how to do technical seo audit"
- "seo vs sem difference"
- "internal linking strategies"

**Content types**: How-to guides, tutorials, explainers, glossary pages, pillar content

**Conversion potential**: Low direct, high for building topical authority and email capture

---

### 2. Navigational

The searcher wants to find a specific page, brand, or resource. They already know what they're looking for.

**Funnel stage**: Any (depends on context)

**Modifier signals**:
- Brand names: "ahrefs", "semrush", "google search console"
- Product names: "screaming frog seo spider", "claude code"
- Platform-specific: login, dashboard, documentation, docs, api, pricing page
- Specific resource: "[brand] blog", "[tool] tutorial", "[person] twitter"

**Examples**:
- "google search console"
- "ahrefs site audit"
- "screaming frog documentation"
- "ccforseo.com skills"

**Content types**: Landing pages, product pages, branded content, documentation

**Conversion potential**: High if navigating to your brand. Low/zero if navigating to a competitor.

**Clustering note**: Navigational keywords for competitor brands rarely deserve their own content unless you're writing a comparison or alternative piece (which is commercial intent).

---

### 3. Commercial

The searcher is evaluating options before a purchase. They're comparing, reviewing, or researching products and services.

**Funnel stage**: Middle of funnel (consideration)

**Modifier signals**:
- Evaluation words: best, top, review, reviews, comparison, compare, vs (products)
- Alternative-seeking: alternative, alternatives to, similar to, like
- Quality signals: pros and cons, honest review, worth it, should I
- Category browsing: tools, software, platforms, services, agencies, companies
- Year modifiers: "best [x] 2026" (signals active comparison shopping)

**Examples**:
- "best seo tools for agencies"
- "ahrefs vs semrush 2026"
- "screaming frog alternatives"
- "is surfer seo worth it"

**Content types**: Comparison posts, "best of" roundups, detailed reviews, alternative pages, listicles

**Conversion potential**: High. These searchers are close to buying. Comparison and alternative content converts well with affiliate links or product positioning.

---

### 4. Transactional

The searcher is ready to take action: buy, sign up, download, or start a trial.

**Funnel stage**: Bottom of funnel (decision/action)

**Modifier signals**:
- Purchase words: buy, purchase, order, pricing, price, cost, plans, subscription
- Action words: sign up, register, download, free trial, get started, demo, book
- Deal-seeking: discount, coupon, deal, sale, promo code, free, cheap, affordable
- Urgency: near me, same day, fast, instant

**Examples**:
- "ahrefs pricing"
- "semrush free trial"
- "buy screaming frog license"
- "seo audit service pricing"

**Content types**: Product pages, pricing pages, landing pages, free trial pages, checkout flows

**Conversion potential**: Highest. Minimize friction. These pages need clear CTAs, trust signals, and fast load times.

---

## Mixed Intent Keywords

Some keywords carry signals from multiple intent types. Rules for handling:

1. **Primary intent wins**: Assign the dominant intent. Note the secondary in the cluster output.
2. **"Best" + informational topic**: Commercial, not informational. "Best ways to do keyword research" is commercial because "best" signals evaluation.
3. **Brand + question**: Navigational if seeking a specific brand page. Informational if asking about the brand conceptually. Context determines this.
4. **"How to buy"**: Transactional, not informational. The action verb "buy" overrides the question word.
5. **"Free"**: Commercial if comparing free options ("best free seo tools"). Transactional if seeking a free version ("ahrefs free trial").

## Intent-to-Funnel Mapping

| Intent | Funnel Stage | Primary KPI | Secondary KPI |
|---|---|---|---|
| Informational | Awareness | Organic traffic, time on page | Email signups, scroll depth |
| Navigational | Any | Direct visits, branded search volume | Bounce rate (should be low) |
| Commercial | Consideration | CTR to product page, comparison engagement | Affiliate clicks, demo requests |
| Transactional | Decision | Conversion rate, revenue | Cart abandonment rate, trial starts |

## Intent Signals by Language Pattern

### English modifiers (most common in SEO tools)

| Pattern | Intent | Confidence |
|---|---|---|
| "what is [x]" | Informational | High |
| "how to [x]" | Informational | High |
| "[x] guide" | Informational | High |
| "[x] tutorial" | Informational | High |
| "best [x]" | Commercial | High |
| "[x] vs [y]" | Commercial | High |
| "[x] alternatives" | Commercial | High |
| "[x] review" | Commercial | High |
| "[x] pricing" | Transactional | High |
| "buy [x]" | Transactional | High |
| "[x] free trial" | Transactional | High |
| "[x] login" | Navigational | High |
| "[brand] [feature]" | Navigational | Medium |
| "[x] for [use case]" | Commercial | Medium |
| "[x] examples" | Informational | Medium |
| "[x] template" | Transactional | Medium (wants a downloadable asset) |
| "[x] checklist" | Informational | Medium (but high conversion for lead magnets) |

### Ambiguous patterns (need context)

| Pattern | Possible Intents | Resolution |
|---|---|---|
| "[tool name]" (single word) | Navigational or Informational | Check SERP: if homepage ranks #1, navigational |
| "[x] tools" | Commercial or Informational | If plural "tools" with no "best/top", lean commercial |
| "[x] strategy" | Informational or Commercial | Informational unless paired with "best" or comparison |
| "[x] cost" | Transactional or Informational | Transactional if specific product, informational if general concept |
