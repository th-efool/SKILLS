# SEO/GEO Playbook

Rules and processes for creating content that ranks in traditional search and AI overviews. Read by the `/seo-blog` skill on every invocation.

---

## A. What to Research (Before Writing Anything)

### Keyword Research (MCP tools)
1. **Google Trends** — `compare_keywords` (3-5 core terms), `get_related_queries` (actual search language), `get_trending_searches` (is topic trending now?)
2. **Keyword Planner** — `generate_keyword_ideas` (seed with core keywords), `get_historical_metrics` (monthly search volumes)
3. Output: primary keyword, 3-5 secondary keywords, 5-8 long-tail questions

### Forum/Community Mining
- WebSearch for Reddit threads, StackOverflow, Quora, niche forums
- Extract actual questions people ask (exact phrasing) → these become H2 headings and FAQ candidates
- Note common pain points, misconceptions, and language patterns
- Search queries: `"[topic] site:reddit.com"`, `"[topic] site:stackoverflow.com"`

### Competitor Content Audit
- Find top 3-5 ranking articles for target keyword
- Analyze: structure, word count, headings, data, what they MISS
- Identify the gap your content fills (unique angle)

### Data & Numbers Sourcing
- Research papers, industry reports, benchmarks
- Google Scholar: `"[topic]" filetype:pdf` or site:arxiv.org
- Gartner, Forrester, McKinsey reports for enterprise topics
- **Must find 3+ citable data points with specific numbers** — GEO loves data
- When citing: include source name, year, and exact figure

### Semantic Mapping
- Ask ChatGPT/Claude: "What are the top resources for [topic]?"
- Note which sources AI engines currently cite → your content should be better than those
- Identify the query patterns AI engines respond to

### Funnel Classification
| Position | Content Types | Effort | Keywords |
|----------|--------------|--------|----------|
| Top of funnel | Listicles, glossary, broad educational | Light | High volume, low intent |
| Middle of funnel | How-to, guides, use cases | Moderate | Specific, problem-focused |
| Bottom of funnel | Comparisons, alternatives, case studies | Deep research | High intent, low volume |

---

## B. How to Structure Content

### Mandatory Structure (every content piece)

1. **TL;DR on top** — 3-5 bullets, under 100 words, BEFORE the intro
2. **Short intro** — 2-3 sentences establishing tension/hook. Not a preamble.
3. **Question-based H2 headings** — real questions people search for (from forum mining)
4. **Self-contained sections** — each section answers its heading question completely
   - First sentence = direct answer to the heading question
   - No "as mentioned above" or "we'll cover this later"
   - If someone extracted just this section, it would make complete sense
5. **Tables** — use wherever structured data exists (comparisons, pricing, pros/cons, feature matrices)
6. **FAQs at bottom** — 5-7 questions from forum research (not assumed), 40-60 words each, FAQ schema
7. **At least 1 image** — with alt text. Include Gemini/ChatGPT generation prompt.
8. **At least 5 interlinks** — natural, contextual links to project's other pages
9. **At least 2 outlinks** — authoritative external sources (research papers, official docs)
10. **Data citations** — 3+ data points with specific numbers, source, and year

### Structure by Content Type

**Blog post (cluster):** TL;DR → intro → 4-7 question H2s → FAQ → CTA
**Comparison page:** TL;DR → why compare → feature table → section per differentiator → verdict → FAQ
**Glossary term:** One-line definition → detailed explanation → related terms → examples → FAQ
**Pillar page:** TL;DR → overview → 8-12 section H2s linking to cluster posts → FAQ → resource list
**FAQ section:** 5-7 Q&As with schema markup, embedded on host page

---

## C. How to Write Content

### Banned Words (AI detection signals)
Never use: delve, tapestry, pivotal, furthermore, moreover, in conclusion, leverage, robust, comprehensive, seamless, utilize, harness, navigate, "in today's digital landscape", "it's important to note", "it's worth noting", "without further ado", "let's dive in"

### Burstiness (sentence length variance)
- Mix aggressively: 4-word punches with 20-word context sentences
- Never 3 similar-length sentences in a row
- Single-sentence paragraphs for key insights
- Start sentences with "And", "But", "Because", "So" for rhythm

### Point of View
- Take a clear position. No hedging. No "it might be possible that perhaps..."
- Expert perspective: "In our experience..." not "Some say..."
- First person "I" for personal insights. "We" only for team actions.
- Write for one person reading right now. Use "you" constantly.

### Real > Hypothetical
- Specific numbers: "from 12 failing tests to 2" not "significant improvement"
- Named examples: "when Stripe launched..." not "a company might..."
- Customer quotes and real conversations over generic scenarios
- Cite exact sources: "Gartner 2025 report found 47% of..." not "studies show..."

### Non-Commodity Content (Google's #1 recommendation)
- **Unique POV:** What do you know from first-hand experience that competitors don't?
- **Proprietary data:** Your own metrics, customer results, A/B test outcomes
- **Expert perspective:** Exceed common knowledge — not "7 tips", but deep analysis
- **Case studies:** Real results with real numbers from real customers

### H.U.M.A.N. Editing Framework (post-draft)
- **H — Hear it aloud:** Read every paragraph. Rewrite anything that sounds like a textbook.
- **U — Unique perspective:** Does the piece have a stance? Add one if missing.
- **M — Mix it up:** Check paragraph/sentence length. Break patterns.
- **A — Anecdotes and specifics:** Replace every generic example with a specific one.
- **N — Natural language:** Run against banned word list. Strip remaining formal phrasing.

### Two-Pass Technique
- **Pass 1:** Generate for completeness — structure, data, sections, links
- **Pass 2:** Humanize — voice, burstiness, specifics, banned word check

### Anti-Patterns (NEVER)
- "In this article, I will..."
- Summary/recap conclusions
- "Moving on..." or "Let's dive in..."
- Listicle headers ("5 Things I Learned...")
- Generic endings: "What do you think?", "Agree?"
- Long compound sentences joined with commas
- Passive voice
- Three paragraphs of similar length in a row

---

## D. Post-Publish & GEO Strategy

### What Actually Works (per Google's AI Optimization Guide)

1. **Unique point of view** — first-hand experience, proprietary insights
2. **Non-commodity content** — expert perspectives exceeding common knowledge
3. **Quality organization** — clear paragraphs, sections, headings
4. **Multimedia** — high-quality images/video with proper SEO
5. **Technical fundamentals** — crawlability, page speed, semantic HTML
6. **No scaled content abuse** — don't spam variations targeting query permutations

### What's Overhyped (per Google)

| Myth | Reality |
|------|---------|
| FAQ schema = GEO lever | "Structured data isn't required for AI search." Helps rich snippets only. |
| Content chunking for AI | "No requirement to break into tiny pieces." |
| AI-specific writing style | "AI can understand synonyms and general meanings." |
| llms.txt files | "You don't need machine-readable files for AI search." |
| Manufactured social mentions | "Pursue organic mentions through quality." |

### Still Valuable Tactics

- **Comparison pages** — high conversion (7.5%), brand visibility when competitors are searched
- **Content freshness** — update stats/dates, add "Last updated" timestamps
- **YouTube** — AI overviews increasingly pull from video content
- **Reddit/UGC** — genuine participation, not manufactured. AI overviews cite Reddit heavily.
- **Partner blogs/trade publications** — external citations boost authority
- **FAQ schema** — still helps traditional rich snippets and PAA boxes
- **Glossary terms** — highly citation-worthy for AI engines (clear, structured definitions)
