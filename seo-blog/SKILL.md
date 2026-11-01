---
name: seo-blog
description: Generate SEO/GEO-optimized content — blogs, FAQs, glossary terms, comparison pages, pillar guides. Full research-to-publish pipeline with keyword research, forum mining, humanization. Works for any project.
argument-hint: "[topic] or --outline [topic] or --research-only [topic] or --type [blog|faq|glossary|comparison|pillar] [topic] or --improve 'learning'"
---

# /seo-blog — SEO/GEO Content Generator

Generate search-optimized content for any project. Full pipeline from keyword research to publish-ready output.

**Project-agnostic.** Pass `--project [name]` to inject project context, or the skill will ask which project on invocation.

## Modes

### 1. Default: `/seo-blog [topic]`
Full pipeline: research → outline → write → humanize → output. Produces a blog post by default.

### 2. Outline: `/seo-blog --outline [topic]`
Research + structured outline only. Review before committing to a full write.

### 3. Research Only: `/seo-blog --research-only [topic]`
Keyword research + forum mining + competitor audit. Outputs a research brief with topic candidates and recommended content type. No writing.

### 4. Type-Specific: `/seo-blog --type [blog|faq|glossary|comparison|pillar] [topic]`
Generate a specific content type. Each type has its own structure template.

### 5. Improve: `/seo-blog --improve "learning"`
Append a learning to the learnings file. Skip content generation.

---

## Improve Mode Flow

1. Read `~/.claude/skills/seo-blog/learnings.md`
2. Append the learning under `## User Feedback` with today's date and context
3. Confirm what was saved
4. Done

---

## Research-Only Mode Flow

1. Load context (Step 1 from Default Mode)
2. Run full research (Step 2 from Default Mode)
3. Output a research brief:

```markdown
## Research Brief: [Topic]

### Search Demand
- Primary keyword: [keyword] — [volume/mo]
- Secondary keywords: [list with volumes]
- Trending: [rising/stable/declining]

### Related Queries (Google Trends)
- [query 1]
- [query 2]

### Forum Questions (actual questions people ask)
- [question from Reddit/SO/forum — with source link]
- [question — source]

### Competitor Content (top 3-5 ranking articles)
- [URL] — [word count, structure, gaps]

### Data Sources Found
- [citation with specific number, source, year]

### Recommended Content Type
[blog/comparison/glossary/pillar/FAQ] — [reason based on funnel position and search intent]

### Recommended Angle
[1-2 sentences: what unique POV can we take that competitors miss?]
```

---

## Outline Mode Flow

1. Load context (Step 1)
2. Run research (Step 2)
3. Build outline (Step 3)
4. Output the outline WITHOUT writing prose. Includes:
   - Title + meta description
   - Content type recommendation
   - TL;DR bullets
   - All H2 question headings with first-sentence answers noted
   - FAQ candidates (from forums)
   - Interlink + outlink targets
   - Table placements
   - Image placements with **Gemini/ChatGPT generation prompts**
   - Data citations to include

---

## Default Mode Flow

### Step 1: Load Context (parallel reads)

Read these files:
- `~/.claude/skills/seo-blog/learnings.md`
- `~/.claude/skills/seo-blog/seo_geo_playbook.md`
- `~/.claude/skills/seo-blog/content_architecture.md`
- `~/.claude/skills/content-shared/writing_style_guide.md`
- `~/.claude/skills/content-shared/notion_config.md`

**Project context** (based on `--project` flag or ask user):
- Read the project's blog directory to get existing post slugs/titles (for interlinks)
- Read any product overview or CLAUDE.md for product context
- If no project specified, ask: "Which project is this for? I need the blog directory path and product context."

### Step 2: Research

Run these in parallel where possible:

**2a. Keyword Research (MCP tools):**
- `mcp__google-trends__compare_keywords` — compare 3-5 core topic keywords
- `mcp__google-trends__get_related_queries` — for top 2 keywords
- `mcp__google-trends__get_trending_searches` — check if topic is trending
- `mcp__keyword-planner__generate_keyword_ideas` — seed with core keywords
- `mcp__keyword-planner__get_historical_metrics` — search volumes

If MCP tools unavailable, note the limitation and proceed with manual analysis via WebSearch.

**2b. Forum/Community Mining:**
- WebSearch: `"[topic] site:reddit.com"`, `"[topic] site:stackoverflow.com"`
- Extract 5-8 actual questions people ask (exact phrasing)
- These become H2 headings and FAQ candidates

**2c. Competitor Content Audit:**
- WebSearch for top 3-5 ranking articles on target keyword
- Note: structure, word count, headings, data, what they MISS
- Identify the gap we can fill

**2d. Data & Numbers Sourcing:**
- WebSearch for research papers, industry reports, benchmarks
- Find 3+ citable data points with specific numbers, source name, and year
- Google Scholar when applicable

**2e. Semantic Mapping:**
- What does ChatGPT/Claude currently cite for this topic?
- Which sources appear in AI overviews?

**2f. Classify:**
- Funnel position: top (listicle/glossary), middle (how-to/guide), bottom (comparison/case study)
- Recommend content type from content_architecture.md
- Determine effort level based on funnel position

### Step 3: Build Outline

Construct:
- **Title:** Under 60 chars, includes primary keyword
- **Meta description:** Under 155 chars, includes primary keyword
- **Content type:** blog/comparison/glossary/pillar/FAQ (recommend based on research)
- **TL;DR:** 3-5 bullets, under 100 words total
- **Short intro:** 2-3 sentences establishing tension/hook
- **H2 headings:** 4-7 question-based headings from search queries
- **For each H2:** First-sentence answer + key points + tables/data to include
- **FAQ section:** 5-7 questions from forum research. Each answer: 40-60 words.
- **Interlinks:** 5+ links to project's existing pages (pulled from Step 1)
- **Outlinks:** 2+ authoritative external sources
- **Tables:** Where to use (comparisons, pricing, pros/cons)
- **Images:** Placement + **Gemini/ChatGPT image generation prompts** (copy-paste ready from `humanization_prompts.md` templates)

### Step 4: Write First Draft

Apply `seo_geo_playbook.md` Section C (writing rules) with:

**Structure (non-negotiable):**
1. TL;DR on top — bullets, under 100 words
2. Short intro (not a preamble)
3. H2s are questions people search for
4. Each section self-contained — first sentence answers heading question
5. No "as mentioned above", no "we'll cover this later"
6. Tables wherever structured data exists
7. At least 1 image (with alt text)
8. At least 5 interlinks, at least 2 outlinks
9. 3+ data citations with specific numbers
10. FAQs at bottom with researched questions

**Voice:** Apply `writing_style_guide.md` — peer-to-peer, honest, direct, real examples over hypotheticals.

**Non-commodity:** Unique POV, proprietary insights, expert perspective exceeding common knowledge (Google's #1 recommendation).

### Step 5: Humanization Pass

After the first draft, run a second pass:

1. **H — Hear aloud:** Rewrite anything that sounds like a textbook
2. **U — Unique perspective:** Verify clear stance. Add one if missing.
3. **M — Mix it up:** Check sentence/paragraph length variance. Break patterns.
4. **A — Anecdotes and specifics:** Replace every generic example with a specific one
5. **N — Natural language:** Run against banned word list from playbook. Strip remaining formal phrasing.

Also verify: every section passes the independence check (can be extracted and still make sense).

### Step 6: Generate Output

**Determine format based on project:**

**Format A: MDX (for Next.js blogs)**

```mdx
---
title: '[Title]'
description: '[Meta description]'
date: '[YYYY-MM-DD]'
author: '[Author]'
authorEmail: '[email]'
tags: ['Tag1', 'Tag2', 'Tag3']
featured: false
keywords:
  - keyword-1
  - keyword-2
  - keyword-3
---

import { BlogHeader } from '../BlogHeader';

export const metadata = {
  title: '[Title]',
  description: '[Meta description]',
};

<BlogHeader slug="[slug]" />

## TL;DR

- Bullet 1
- Bullet 2
- Bullet 3

[Short intro]

## [Question-based H2]?

[First sentence answers the question.] [Rest of section...]

[... more sections with tables, data, interlinks ...]

## Frequently Asked Questions

### [Researched question]?

[40-60 word answer with link to deeper content]

### [Researched question]?

[40-60 word answer]
```

**Format B: Markdown (generic — for any project)**

```markdown
---
title: "[Title]"
description: "[Meta description]"
date: "YYYY-MM-DD"
author: "[Author]"
keywords: [keyword1, keyword2, keyword3]
---

## TL;DR

- Bullet 1
- Bullet 2

[Content with same structure rules...]

## FAQ

**Q: [Question]?**
A: [40-60 word answer]

<!-- FAQ Schema (add to page): -->
<!-- [JSON-LD FAQ schema block for developer to copy] -->
```

**Always include with output:**
- Image generation prompts (Gemini/ChatGPT ready) for each suggested image
- Verification checklist results (see below)
- Reminder: create banner image at `public/blog/{slug}.webp` (if MDX project)

### Step 7: Verification Checklist

Run and report pass/fail:

| Check | Category | Pass? |
|-------|----------|-------|
| TL;DR present, under 100 words, bullets | Structure | |
| All H2s are questions | Structure | |
| Each section self-contained (no cross-refs) | Structure | |
| First sentence answers heading question | Structure | |
| At least 1 table | Structure | |
| At least 5 interlinks | SEO | |
| At least 2 outlinks | SEO | |
| 3+ data points with specific numbers | SEO/GEO | |
| FAQ section with 5+ researched questions | SEO | |
| FAQ answers 40-60 words each | SEO | |
| Image generation prompts included | Content | |
| No banned words present | Humanization | |
| Sentence length variance (burstiness) | Humanization | |
| Clear point of view (not commodity) | Google's guide | |
| Unique insight or proprietary data | Google's guide | |
| Title under 60 chars | SEO | |
| Meta description under 155 chars | SEO | |

### Step 8: Save + Feedback

Ask: "Want me to save this draft to Notion?"

If yes and Notion MCP available:
1. Read `~/.claude/skills/content-shared/notion_config.md`
2. Create page with title, status "Draft", platform "Blog", body = full content

Then ask: "Any feedback on structure, voice, or content? Use `/seo-blog --improve 'your feedback'` to save it for future posts."

---

## Content Type Templates

### --type comparison

Structure: TL;DR → Why compare → Feature comparison table → Section per key differentiator → Verdict (recommend each for different situations, don't declare winner) → FAQ

### --type glossary

Structure: One-line definition (first sentence) → Detailed explanation → Why it matters → Examples → Related terms (link to other glossary entries) → FAQ (2-3 questions)

Length: 500-800 words. Short, authoritative, definitional.

### --type pillar

Structure: TL;DR → Overview → 8-12 H2 sections (each linking out to a cluster blog post) → Resource list → FAQ

Length: 3000-5000 words. Comprehensive hub.

### --type faq

Generates an FAQ section to embed on an existing page (not standalone). Output:
- 5-7 researched Q&As (40-60 words each)
- FAQ schema JSON-LD block
- Instructions for where to embed (pricing, features, homepage, etc.)

---

## Anti-Patterns (NEVER)

- Hardcode project-specific paths or product details — always inject from context
- Assume FAQ questions — ALWAYS research from forums/Reddit/SO
- Use banned words from the playbook
- Write commodity content ("7 tips for...") — unique POV or don't publish
- Create standalone /faq pages — FAQs are embedded sections
- Skip the humanization pass — always run two-pass
- Use hypothetical examples when real ones exist
- Ignore the verification checklist
- Write sections that reference other sections ("as mentioned above")
- Produce content without image generation prompts
- Skip data citations — every post needs 3+ specific numbers
