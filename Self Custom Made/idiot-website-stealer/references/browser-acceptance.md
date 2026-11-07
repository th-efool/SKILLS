# Browser acceptance, with concrete measurements

Use the available browser automation tool and read its documentation. The following read-only browser expressions describe the checks; adapt them to the tool's supported frame/locator API. The import is inside `iframe[title]`, so inspect its document, rather than the outer Next.js shell.

## Desktop, then narrow viewport

1. Load the selected route. Wait for the hero's text animation to settle by observing a stable full headline. Inspect a screenshot: original typeface/scale, aligned header, logo, hero background, CTA, and one intended vertical scrollbar. Compare against the bundled CSS/markup or available reference screenshot.
2. Scroll one viewport at a time through the footer. This triggers lazy images, videos, scroll reveals, and carousels. Inspect every major section visually. At each stop collect the visible media diagnostics:

```js
// Apply within the imported frame using its supported locator evaluation API.
Array.from(document.images, img => ({
  src: img.currentSrc || img.src,
  visible: img.getBoundingClientRect().bottom > 0 && img.getBoundingClientRect().top < innerHeight,
  ready: img.complete && img.naturalWidth > 0
}))
Array.from(document.querySelectorAll('video'), video => ({
  src: video.currentSrc,
  readyState: video.readyState,
  error: video.error?.message
}))
```

Visible images have natural dimensions. Active videos reach readyState >= 2 with no media error. Offscreen lazy media are evaluated when brought into view. Canvas/particles show visual activity when motion is enabled; reduced-motion mode may intentionally simplify them.

3. Exercise the first present example of each type: dropdown open/close, mobile navigation toggle, carousel next/previous, in-page anchor, video play/pause. Confirm an actual visible state change. Inspect links' destinations; official subpages absent from the archive open on the original host. Newsletter submission and downloads can be checked structurally without submitting data or installing software.
4. Read console and network errors after these interactions. Local CSS/JS/media requests have successful statuses and matching content types. Fix source-specific failures, reload, and recheck. Report external services separately when they require unavailable accounts or APIs.
   When an archive has beautifier damage, also inspect line breaks after `return`, `throw`, `yield`, and `async`. For example, `return\n typeof a === 'string' ? a : null` parses but returns undefined; restore `return typeof a === 'string' ? a : null` when the original expression and calling behavior establish that intent. Verify the affected behavior, since syntax checks establish parsing rather than semantic equivalence.
5. Set a narrow viewport (e.g. 390 x 844). Repeat hero, mobile-menu open/close, section layout, and horizontal-overflow checks. The frame document's scrollWidth fits its clientWidth, allowing rounding of a pixel. Reset viewport overrides afterward.
6. Save desktop and mobile screenshots. In the import note record URLs, viewport sizes, build result, checked controls, and actual unresolved findings. Include a screenshot and local route in the final reply.

## Interpret a failed view

| Observation | Next concrete check and repair |
| --- | --- |
| Blue links and stacked menus | Inspect stylesheet request paths and MIME types; scope them to served asset prefix. |
| Styled page, missing animated hero | Read module console errors; parse reported scripts and inline modules. |
| Image request is 200, image is broken | Inspect binary signature and response MIME; recover the exact asset rather than saving HTML as an image. |
| Video says unable to play | Inspect file signature, browser media error and currentSrc; recover original and confirm decode. |
| Two outer scrollbars | Full-viewport fixed iframe; let only the imported document scroll. |
| Missing lower-page media | Scroll into view to trigger loading, then inspect asset request and natural dimensions. |
| Internal link opens a local 404 | Resolve absent original subpage to original host; preserve local section anchors. |
