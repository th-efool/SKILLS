# Worked example: Antigravity export

Input: `antigravity.google.zip`. Existing Next.js app has `/` listing five placeholder pages. User: “using it make LandingPageA.”

## Discover

ZIP entries include `antigravity.google/index.html`, `_astro/*.css`, `_astro/*.js`, images, and videos. Read the homepage: it references `/_astro/BaseLayout.CIyAz6Yx.css` and `/assets/video/hero_video.mp4`. The confirmed origin is `https://antigravity.google`.

Choose `/LandingPageA` because the user supplied the name. For the same request with no page name, choose `/antigravity`.

## Prepare and mount

The normal one-prompt path now starts with `scripts/import_site.py --zip <archive> --project <project> --route /LandingPageA`. It performs discovery, preparation, repairs, and mounting. The detailed steps below explain what the runner produces and how to finish verification. Omitting `--route` on this archive derives `/antigravity`.

Run `prepare.py` as shown in SKILL.md. Suppose its returned `served_entry` is `/website-imports/landingpagea-abcdef1234/antigravity.google/index.html`. Create `app/LandingPageA/page.tsx`:

```tsx
export default function LandingPageA() {
  return (
    <iframe
      src="/website-imports/landingpagea-abcdef1234/antigravity.google/index.html"
      title="Google Antigravity"
      style={{ border: 0, position: "fixed", inset: 0, width: "100%", height: "100dvh", background: "white" }}
    />
  );
}
```

Use the actual returned prefix, including its hash. The CSS reference now resolves inside that import. Fonts served by valid external URLs can continue loading externally. Font files in this particular ZIP were tiny invalid files, so their presence alone didn't establish usability.

## Repair observed defects

The first broken attempt showed plain blue links and stacked desktop/mobile menus. Cause: assets were under `/antigravity/_astro` while HTML requested `/_astro`. Scoped asset references fix the actual request paths.

After CSS loaded, animations still failed. Parsing `gsap.Bi_c5vh2.js` located `n || = t && !f`. Restoring `n ||= t && !f` made that expression parse. Other reported expressions needed `f ? .play()` → `f?.play()` and `e ? ? fallback` → `e ?? fallback`. Parse all modules again; confirm that text or template contents weren't modified by the repair.

The hero video existed but its first bytes weren't an MP4 container. Fetching the exact original `/assets/video/hero_video.mp4` supplied a valid video; the browser reached `readyState: 4`. The missing `/assets/image/product/new-chat.png` and landing thumbnails were recovered at their exact original paths. Verify signatures and rendered dimensions, including lazy images after scrolling.

Subpage links such as `/product` and `/download` point to `https://antigravity.google/product` and `https://antigravity.google/download` in a new tab. The app's `/` remains the five-page index.

## Evidence of completion

The hero shows the Google Antigravity logo, large centered headline, animated particles, and Download button. Products opens its styled dropdown. The lower product sections and lazy images display; both videos decode. Check narrow-screen navigation. The Next.js production build passes. Save a screenshot and return the actual local URL.

This sequence turns each encountered defect into a concrete observation, repair, and recheck. A successful HTML request or build is one checkpoint within that sequence.
