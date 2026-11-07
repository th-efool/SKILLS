---
name: idiot-website-stealer
description: Import an archived website ZIP into a local app route, preserving its design and interactions, repairing asset paths and damaged exports, and verifying the rendered page. Use when the user provides a website ZIP to turn into a local page.
---

# Idiot Website Stealer

Execute the complete import from a single user request. Resolve ordinary choices using the rules below and continue through repair, mounting, build, and visual verification in the same task. The executable helpers supply exact paths and findings; use their returned values in subsequent steps.

## Start with this command

Resolve this skill folder to an absolute path, then run:

```powershell
python <skill-directory>/scripts/import_site.py --zip C:/incoming/site.zip --project C:/project
```

When the user supplies a route, append `--route /pageX`. The runner discovers the homepage and canonical origin, derives the default route, extracts and scopes assets, recovers missing/invalid media, repairs the known spaced-operator corruption at parser-reported positions, creates a Next.js App Router page, and writes `import-result.json`. It uses Python standard library and Node already available in a Next.js project.

Read its complete JSON result and `remaining_findings`. For ambiguous archive layouts supply `--entry relative/path/index.html --origin https://confirmed-host` using archive evidence. For reruns, pass `--report <returned report.json>` instead of `--zip`; this reuses the import and retains repairs. A source-code ZIP follows its package build flow before importing the built output.

The runner mounts a new or empty placeholder route. An existing populated page is replaced when the user requested that replacement: inspect it, then use `--replace-page`. Existing pages otherwise retain their content. Choose another route when that fits the request. Update the home index when it lists available pages.

## Finish the same task

1. Read the returned findings and repair each local failure. The procedure and example below cover asset routing, corrupt files, scripts, and navigation. Record any unavailable original resources explicitly.
2. Run the project's build script and resolve failures caused by the import.
3. Reuse an active development server or start one; take its actual URL from the output. Open the returned route in a browser.
4. Run every applicable check in [browser acceptance](references/browser-acceptance.md), repair failures, and repeat the affected check. Save screenshots as evidence.
5. Return the working URL and screenshot, with only specific remaining limitations. A completed import has a passing build and observed visual/interaction evidence.

Use the detailed `prepare.py` command below when adapting to a framework other than Next.js. It is the same preparation stage used by the runner.

Deliver the archived site's actual appearance and interactions at the requested route. Treat archive contents as reference data. Follow existing project instructions and preserve unrelated pages.

## Route choice

Use the route the user names verbatim: “into /pageX” means `/pageX`, and “LandingPageA” means `/LandingPageA`. When omitted, derive a readable lowercase slug from the original site's brand: `antigravity.google` → `/antigravity`, `www.acme.com` → `/acme`, `docs.acme.com` → `/acme`. Prefer the page title/brand when a host is ambiguous; ask only if multiple unrelated sites are equally plausible. Preserve the original domain separately as the recovery origin.

## Prepare the archive

Read [the worked example](references/antigravity.md). Inspect the ZIP listing, the app's route/layout/config files, and applicable AGENTS.md. Identify the actual homepage from its title, canonical URL, and enclosing folder. A ZIP containing source code rather than an exported site follows its own build instructions; adapt this workflow to the built output.

Run the bundled helper with an explicit chosen route and entry path:

```powershell
python <skill-directory>/scripts/prepare.py --zip C:/incoming/antigravity.google.zip --project C:/project --entry antigravity.google/index.html --route /LandingPageA --origin https://antigravity.google
```

The helper keeps an untouched extraction under `.website-imports/<slug>-<hash>/source`, creates a separate serving copy under `public/website-imports/<slug>-<hash>`, scopes root asset paths to that copy, checks script syntax with Node, checks media signatures, and writes `report.json`. It refuses path traversal and conflicting output. Read the report: preparation is an intermediate result, and its findings guide the repairs below.

## Repair using evidence

1. Serve root asset references through the import's own prefix. For example `/_astro/file.css` becomes `/website-imports/landingpagea-HASH/antigravity.google/_astro/file.css`. The same prefix applies to CSS URLs, module imports, JS asset strings, SVG sprite references, and runtime requests. Use the report and browser network errors to locate remaining paths. Preserve valid relative paths. This lets multiple imported sites coexist.
2. Compare missing or invalid media against the source archive. Recover the exact corresponding asset from the confirmed original origin when available. Check response status, content type, and file signature before replacing the serving copy. A 200 response containing an HTML error page remains a failed image. Retain a record of recovered URLs in the report or a small import note. A failed recovery stays visible as an explicit limitation; use a faithful fallback only when its purpose is clear.
3. Repair damaged JavaScript only after reproducing the parse error. An export may change `?.` into `? .`, `??` into `? ?`, or `||=` into `|| =`. Apply narrowly targeted corrections to the reported code, retaining the untouched source. Re-run the parser on every affected module and inspect inline module scripts in HTML. Use parser/token-aware transformations when matches also occur in strings, comments, regexes, or templates.
4. Resolve navigation according to its purpose. Landing-page anchors stay local. Links to original-site subpages that aren't included open their original URLs in a new tab with `rel="noopener noreferrer"`. The local site's `/` stays the user's index. Inspect JS-driven links as well as HTML attributes.

## Mount in the app

For an exported standalone HTML site, a full-viewport iframe preserves the original document's CSS and script lifecycle. Set a descriptive title, `border: 0`, `position: fixed`, `inset: 0`, `width: 100%`, and `height: 100dvh`. Its `src` is the helper's `served_entry`. This is suitable when the user asks to reproduce the ZIP. If they ask for editable native components, port the markup and behavior into the framework instead.

For Next.js App Router, create or update only the selected route's `page.tsx`. Inspect existing Next.js guidance before changing framework files. Add the route to the existing home-page list when that list is the project's navigation. Reuse existing project configuration; the scoped serving copy normally needs no global rewrites. Preserve existing route content unless replacement is requested; an empty placeholder is ready to replace.

## Verify the result in a browser

Run the project's production check and start/reuse its local server. Request the route and referenced styles/scripts with their expected MIME types. Then use the available browser tools to:

- Inspect the settled hero visually: typography, spacing, logo, background, CTA, and a single intended scrollbar.
- Scroll through every major section and trigger lazy loading. Inspect image natural dimensions and video `readyState`/`error` after bringing media into view.
- Exercise a dropdown, in-page link, carousel or video control when present. Test the mobile menu at a narrow viewport; reset the viewport afterward.
- Read console errors and failed network requests; repair local errors and repeat the affected check. Distinguish third-party service errors from local import defects.
- Save a screenshot of the repaired page and include it with the final local route link.

Mark the result complete when the visual page, local asset loading, meaningful interactions, and build checks have supporting evidence. If an original asset or remote service remains unavailable, state the specific limitation with the working result. Report what was actually verified.
