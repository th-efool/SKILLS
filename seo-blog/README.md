# SEO/GEO Blog Skill for Claude Code

A Claude Code skill that generates SEO and GEO (Generative Engine Optimization) optimized content — blogs, FAQs, glossary terms, comparison pages, and pillar guides.

Built from real conversations with SEO/GEO practitioners and [Google's official guide to optimizing for AI search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).

## What's inside

| File | What it does |
|------|-------------|
| `SKILL.md` | The Claude Code skill — install it and use `/seo-blog` |
| `seo_geo_playbook.md` | Complete research, structure, writing, and post-publish rules |
| `content_architecture.md` | Website content map — what pages to build, where they go, how they connect |
| `humanization_prompts.md` | Copy-paste prompts for making AI content sound human + image generation templates |
| `learnings.md` | Pre-seeded insights that improve over time with `--improve` |

## Install

Copy the skill to your Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills/seo-blog
cp SKILL.md seo_geo_playbook.md content_architecture.md humanization_prompts.md learnings.md ~/.claude/skills/seo-blog/
```

The skill also reads a shared writing style guide. If you don't have one, it works without it — but creating one at `~/.claude/skills/content-shared/writing_style_guide.md` will improve voice consistency.

## Usage

```
/seo-blog [topic]                          # Full pipeline: research → outline → write → output
/seo-blog --outline [topic]                # Research + outline only (review before writing)
/seo-blog --research-only [topic]          # Keyword research + forum mining + competitor audit
/seo-blog --type comparison [topic]        # Generate a specific content type
/seo-blog --type glossary [term]           # Generate a glossary entry
/seo-blog --type pillar [topic]            # Generate a pillar page
/seo-blog --improve "your feedback"        # Save a learning for future posts
```

Works with any project. Pass `--project [name]` to inject project-specific context, or the skill will ask.

## What it does

### Research phase
- Keyword research via Google Trends + Keyword Planner MCPs (if available)
- Forum mining — finds actual questions people ask on Reddit, HN, StackOverflow, Quora
- Competitor content audit — what top-ranking articles cover and what they miss
- Data sourcing — finds citable stats with specific numbers
- Classifies funnel position and recommends the right content type

### Writing phase
- Question-based H2 headings from real search queries
- Self-contained sections (each answers its heading question — critical for GEO)
- TL;DR on top, tables, FAQs, interlinks, outlinks, data citations
- Two-pass technique: completeness first, then humanization (H.U.M.A.N. framework)
- Banned word list to avoid AI-detection signals

### Output
- MDX format (for Next.js blogs) or generic Markdown
- Full SEO meta tags, structured data (BlogPosting, FAQ, Breadcrumb)
- Verification checklist (17 checks across structure, SEO, humanization)
- Image generation prompts for Gemini/ChatGPT (copy-paste ready)

## What Google actually says about GEO

The skill is aligned with [Google's AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), which debunks several popular "GEO hacks":

| Popular advice | Google says | This skill's approach |
|---|---|---|
| FAQ schema = GEO must-have | "Structured data isn't required for AI search" | Adds FAQ schema (helps rich snippets), doesn't treat it as a GEO lever |
| Chunk content for AI | "No requirement to break into tiny pieces" | Self-contained sections for readability, not AI parsing |
| Write specifically for AI | "AI understands synonyms" | Writes for humans, structures for scannability |
| llms.txt files | "Don't need machine-readable files" | Doesn't prioritize |

**What Google does emphasize:**
1. Unique point of view with first-hand experience
2. Non-commodity content (case studies, proprietary data, specific numbers)
3. Quality organization (clear sections, headings)
4. Multimedia (images/video)
5. Technical fundamentals (crawlability, speed)

## Content architecture

The `content_architecture.md` file includes a complete website content map:

- Blog posts, pillar pages, comparison pages, glossary terms
- FAQ strategy (embedded sections, not standalone pages)
- Linking rules between content types
- Priority build order for any new project
- URL patterns and funnel mapping

Inspired by how [reo.dev](https://www.reo.dev/blog) and [firecrawl.dev](https://www.firecrawl.dev/blog) structure their content.

## Sources

This skill was built from:

- **[Google's guide to optimizing for generative AI in search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)** — the official source on what actually matters for GEO
- **AEO/GEO panel discussion** featuring SEO/GEO practitioners — practical advice on content structure, research workflows, and what's working in 2026
- **Content humanization research** — techniques for burstiness, perplexity, voice consistency, and avoiding AI-detection signals
- **Reference blogs** — reo.dev (content ecosystem approach) and firecrawl.dev (minimal structure + programmatic SEO)

## License

MIT
