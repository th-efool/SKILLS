# Content Architecture Blueprint

Reference document for the `/seo-blog` skill. Defines what content types to build on a product/SaaS website, where they go, and how they connect.

---

## Website Content Map

```
├── / (Homepage)
├── /blog/ (Blog hub — index with category filters)
│   ├── /blog/[category]/ (Category index pages)
│   └── /blog/[slug] (Individual posts — cluster content)
├── /compare/ (Comparison hub)
│   ├── /compare/[product]-vs-[competitor] (Head-to-head)
│   └── /alternatives/[competitor] (Alternative-to pages)
├── /glossary/ (Definitions hub)
│   └── /glossary/[term] (Individual term pages)
├── /learn/ or /guides/ (Pillar pages)
│   └── /learn/[broad-topic] (3000-5000 word comprehensive guides)
├── /solutions/ or /use-cases/ (By role/industry/workflow)
│   └── /solutions/[use-case]
├── /customers/ or /case-studies/ (Customer stories)
│   └── /customers/[company]
├── /features/ (Individual feature pages)
│   └── /features/[feature]
├── /integrations/ (Programmatic — one per tool)
│   └── /integrations/[tool]
├── /templates/ or /resources/ (Downloadable assets)
│   └── /templates/[template]
├── /docs/ (Knowledge base — separate from blog)
│   └── /docs/[section]/[page]
├── /pricing (With embedded FAQ section)
├── /tools/ (Free tools — lead gen + backlinks)
└── FAQ sections (Embedded on host pages, NOT standalone)
```

---

## Content Types

| Type | URL Pattern | Funnel | Purpose | Frequency |
|---|---|---|---|---|
| Blog posts (cluster) | `/blog/[slug]` | TOFU/MOFU | Long-tail keywords, authority | 2-4/week |
| Pillar pages | `/learn/[topic]` | TOFU | Hub for topic clusters, head terms | 4-6 total, update quarterly |
| Comparison pages | `/compare/[x-vs-y]` | BOFU | Evaluation-stage buyers (7.5% conversion) | 1 per competitor |
| Alternative pages | `/alternatives/[competitor]` | BOFU | Switching-intent traffic | 1 per competitor |
| Glossary terms | `/glossary/[term]` | TOFU | Definitional queries, topical moat | 20-50 terms |
| FAQ sections | Embedded on host pages | All | Remove friction, capture PAA | On every key page |
| Use case pages | `/solutions/[use-case]` | MOFU | Product solving specific problems | 3-5 to start |
| Case studies | `/customers/[company]` | BOFU | Social proof with real numbers | As customers come |
| Feature pages | `/features/[feature]` | MOFU/BOFU | "[feature] tool" queries | 1 per feature |
| Integration pages | `/integrations/[tool]` | MOFU/BOFU | Programmatic SEO at scale | 10-20 to start |
| Free tools | `/tools/[tool]` | TOFU | Lead gen, backlink magnet | 1-3 |

---

## Blog Categories

Categories reflect content types, not topics:

| Category | What goes here |
|----------|---------------|
| **Guides** | Deep how-to content (pillar/cluster) |
| **Comparisons** | vs. pages, alternative pages |
| **Case Studies** | Customer stories with data |
| **Product Updates** | Changelog, new features, launch weeks |
| **Industry** | Thought leadership, trends, research |
| **Playbooks** | Actionable frameworks, step-by-step strategies |

---

## FAQ Strategy

FAQs are NOT a standalone `/faq` page. They are **embedded sections** on:
- Pricing page (pricing objections, plan differences)
- Feature pages (how does X work? what are the limits?)
- Use case pages (is this right for my team?)
- Homepage (what is [product]? who is it for?)
- Blog posts (complex topics that generate questions)

**Each FAQ section:**
- 5-7 questions sourced from Reddit/forums/sales calls (NEVER assumed)
- First sentence = the answer directly
- 40-60 words per answer
- Links to deeper content (blog posts, docs, glossary)
- FAQ schema markup (helps rich snippets, not required for AI search per Google)

---

## Linking Rules

| From | Links to |
|------|----------|
| Pillar pages | 8-12 cluster posts + glossary terms + comparison pages |
| Cluster posts | Parent pillar (mandatory) + sibling clusters + glossary terms |
| Comparison pages | Feature pages + case studies + pricing |
| Glossary terms | Related pillar/cluster content + product features |
| FAQ answers | Blog posts + docs for deeper reading |
| Use case pages | Features + case studies + integrations |
| Blog posts | 5+ interlinks + 2+ outlinks (authoritative external) |

---

## Priority Build Order (for any new project)

1. Homepage + feature pages + pricing (foundation)
2. 3 comparison pages (top competitor, top alternative, category comparison)
3. First pillar page + 8-12 cluster articles (topical authority)
4. Glossary hub (20-30 terms to start)
5. Use case pages (3-5 for primary personas)
6. Integration pages (programmatic, top 10-20)
7. Case studies (as customers come in)
8. Free tools (lead gen + backlinks)

---

## Reference Patterns

**reo.dev:** Blog as content ecosystem — guides, playbooks, case studies, academy all in one hub with category filters. Deep content (49-65 min reads) signals expertise. Categories: Technical Prospecting, Playbooks, Guides, DevGTM Academy, Alternatives, Case Study.

**firecrawl.dev:** Clean minimal structure. Launch weeks as marketing campaigns. Free tools for lead gen. Integration pages at scale. Customer stories positioned as social proof. Explicit AI/LLM user support (agent onboarding).
