# Humanization Prompts & Image Generation Templates

Copy-paste prompts for humanizing AI content and generating images. Used by the `/seo-blog` skill and available for manual use.

---

## 1. Rewrite for Human Voice (General Purpose)

```
Rewrite this so it reads like a knowledgeable writer with a clear point of view, not an AI assistant. Apply these rules:
- Open with a short sentence (under 12 words) that states the point directly.
- Vary paragraph length: mix 1-sentence paragraphs with 3-4 sentence blocks.
- Use active voice. Remove all passive constructions.
- Write in second person (you/your) throughout.
- REMOVE these words/phrases entirely: delve, tapestry, pivotal, furthermore, moreover, in conclusion, it is worth noting, it's important to note, in today's digital landscape, leveraging, robust, and any em-dash overuse.
- Replace generic transitions ('Additionally', 'Furthermore') with specific connectives ('Here's the thing', 'That said', 'What this means for you').
- Include at least one sentence that starts with 'Look,' or 'Here's what nobody tells you:' or 'The truth is'.
- Never write three sentences of similar length in a row.
- Include at least one one-word sentence or sentence fragment.
- Use contractions everywhere. 'It is' becomes 'it's'. Always.
```

## 2. Burstiness + Perplexity

```
Write with high burstiness and perplexity:
- Burstiness: Alternate between clusters of longer, detailed sentences and short, punchy ones. Some paragraphs should be one sentence. Others should be 5-6 sentences. Never be uniform.
- Perplexity: Diversify word choices. Favor unexpected vocabulary over the statistically most likely next word. Use at least two metaphors. Mix simple statements with more intricate thoughts.
- Write each section independently with different energy — don't maintain one flat tone throughout.
```

## 3. Blog Post Humanizer

```
Rewrite this blog post draft. Open with a specific story, observation, or bold claim — not a definition. Apply these rules:
1. No sentence starts with 'Additionally', 'Furthermore', 'Moreover', or 'In today's...'
2. Vary sentence length between 4 and 25 words
3. Include at least one rhetorical question per section
4. Add one personal aside or mini-anecdote (make it feel like a real person sharing)
5. Use contractions and plain language — write at an 8th grade reading level
6. End sections with forward momentum, not summaries
7. The conclusion should NOT start with 'In conclusion' — end with a provocation or call to think differently
```

## 4. Cynical Expert Rewrite

```
Rewrite this content from the perspective of a slightly cynical, highly experienced industry veteran who has seen every trend come and go. They respect the reader's intelligence, skip the obvious stuff, and get to what actually matters. They occasionally drop in a dry observation. They never use corporate buzzwords unironically.
```

## 5. Voice Training (Run Once, Save Output)

```
I'm going to share 5 pieces of my writing. After reading all of them, create a detailed voice profile. Capture:
1. My sentence rhythm patterns (short/long ratio)
2. Words and phrases I gravitate toward
3. Words and phrases I never use
4. How I structure arguments
5. My opening and closing patterns
6. My relationship with the reader
7. Rules another writer could follow to mimic my voice

Then compress this into a 200-word "voice prompt" I can paste at the top of any future writing request.
```

## 6. Two-Pass Rewrite

```
Now rewrite this as if a human editor reviewed it. Apply these edits:
- Cut any sentence that sounds like AI wrote it
- Add one personal observation or real-world example
- Make the opening more specific and the ending less neat
- Replace at least 3 generic phrases with something only someone with real experience would say
- Check: would a person actually talk like this? If not, rewrite that part.
```

## 7. Section Independence Check

```
Review each section of this article. For each section, verify:
1. Does it answer the heading question in the first sentence?
2. Can someone read JUST this section and understand it fully?
3. Are there any references to "as mentioned above" or "we'll cover later"?
4. If I extracted this section and put it on a separate page, would it make sense?

Flag any section that fails these checks and rewrite it to be self-contained.
```

---

## Image Generation Prompts (Gemini / ChatGPT)

### Blog Banner (1200x675px)

```
Create a modern, minimal illustration for a blog post titled "[TITLE]". 
Style: Flat design, muted color palette (blues, grays, soft accent color), no text overlaid, clean negative space. 
Concept: [VISUAL CONCEPT related to the topic].
Dimensions: 1200x675 pixels, landscape orientation.
Do NOT include any text, logos, or watermarks.
```

### Data Visualization / Infographic

```
Create a clean, minimal infographic showing [SPECIFIC DATA/COMPARISON].
Style: 2-3 colors max, modern flat design, large readable numbers, simple icons.
Include: [specific data points, e.g., "47% improvement", "3x faster", etc.]
Format: Vertical, suitable for embedding in a blog post.
Do NOT include any logos or branding.
```

### Comparison Graphic

```
Create a side-by-side comparison visual for "[PRODUCT A] vs [PRODUCT B]".
Style: Clean, modern, split layout. Left side = Product A characteristics. Right side = Product B characteristics.
Use abstract icons/shapes to represent each feature — no logos, no screenshots.
Color scheme: Neutral with one accent color for the recommended option.
Format: Landscape, 1200x800px.
```

### Process / Flow Diagram

```
Create a horizontal flow diagram showing these steps: [STEP 1] → [STEP 2] → [STEP 3] → [STEP 4].
Style: Minimal, modern, connected with arrows. Each step has a simple icon and 2-3 word label.
Color: Monochrome with one accent color for the final/important step.
Format: Landscape, suitable for blog embedding.
```

### Section Illustration (Inline)

```
Create a simple illustration representing the concept of "[CONCEPT]".
Style: Flat design, single accent color, suitable as a small inline image in a blog post.
Size: 600x400px.
Keep it abstract/metaphorical — no literal depictions.
```

### Screenshot Annotation

```
I have a screenshot of [WHAT]. Create an annotation overlay that:
- Highlights [SPECIFIC AREA] with a red/orange box
- Adds numbered callouts pointing to [FEATURE 1], [FEATURE 2], [FEATURE 3]
- Includes brief labels (3-5 words each)
Style: Clean, professional, not cluttered.
```
