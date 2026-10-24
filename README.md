# JASCUT Studio · Privacy & Terms

A buildless, responsive legal website for the current native Android app. Prepared locally on **24 October 2026** for <https://github.com/builtbyjasim/jascut-studio-privacy-policy>.

**Status: website source approved by the developer for commit and push on 24 October 2026. GitHub Pages deployment has not been enabled by this task; the legal publication checklist below remains for review.** The public contents endpoint returned HTTP 404 during the initial audit. A subsequent successful Git clone verified that the target repository was empty before transferring these files.

## Files

| File | Responsibility |
| --- | --- |
| `index.html` | Complete Privacy Policy with media, permissions, storage, backup, support and website disclosures |
| `terms.html` | Terms covering scope, content rights, responsible use, limitations and mandatory legal rights |
| `assets/styles.css` | Shared responsive, light/dark and print styling; system fonts only |
| `assets/brand-mark.svg` | Website SVG adaptation of the developer’s existing original Android clapperboard vector |
| `.nojekyll` | Serves the root files directly without Jekyll processing |
| `AUDIT.md` | Source evidence, verification results, limitations and publication review checklist |
| `tools/htmlvalidate.json` | Recommended preset for optional HTML conformance checks |
| `tools/validate.py` | Standard-library structural, local-link, asset and content checks |

No JavaScript, cookies, trackers, external fonts, package manager, build step or runtime dependencies are required. No Android files, app IDs, SDK versions or dependencies were changed.

## Preview and validate

From this directory:

```sh
python3 tools/validate.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Open <http://127.0.0.1:8765/> and follow the Terms link. The pages also work as local files. Preview commands do not deploy anything. For an optional additional check with Node 24.8+ and npm, without adding a dependency to this site:

```sh
npm exec --yes --package=html-validate@11.17.0 -- html-validate --config tools/htmlvalidate.json index.html terms.html
```

This optional command downloads developer tooling into npm’s cache. The Python validator checks selected structural and project requirements; it is not a full HTML conformance checker, accessibility certification or legal review.

## GitHub Pages deployment — only after approval

1. Complete the confirmations below and review both rendered documents. Reconfirm that the release being distributed matches the audit; development changes can make policy text stale.
2. The target repository was verified empty by Git clone before the initial website upload. Preserve existing content and settings during future updates.
3. The developer authorized the initial commit and push. Keep `index.html`, `terms.html`, `assets/`, `.nojekyll` and the accompanying documentation at the repository root on `main`. Do not put the HTML inside another enclosing folder.
4. After explicit approval to publish, open **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main → Folder: / (root)** and save. No custom Actions workflow is needed.
5. Wait for GitHub’s Pages deployment to finish. Check both expected HTTPS URLs below, the navigation, favicon, stylesheet, anchor links and mobile layout. Enable HTTPS enforcement when available. Only then describe the pages as live.
6. Use the verified public Privacy Policy URL in Play Console. Adding in-app links is a separate Android task and was not performed here. Reconcile the Play Data safety answers with the exact distributed app and all included SDKs.

Expected URLs **after successful deployment**, not verified live:

- Privacy: <https://builtbyjasim.github.io/jascut-studio-privacy-policy/>
- Terms: <https://builtbyjasim.github.io/jascut-studio-privacy-policy/terms.html>

All internal links and assets are relative so the site works under GitHub Pages’ repository subpath. Do not add a root-leading `/assets/` path. No custom domain or CNAME is assumed.

## Developer confirmations before publication

- **Identity/contact:** Jasim Khan / Built by Jasim and `zasimkhan3@gmail.com` match both existing policy websites. Confirm these are the appropriate publisher/controller identity and actively monitored address for JASCUT. Public consistency is verified; mailbox access/deliverability is not.
- **Audience and distribution:** Confirm the general-audience wording, whether the app is directed to children, Play target-age settings, and intended countries. No specific minimum age, registered company, postal address, governing country or exclusive court has been invented.
- **Legal requirements:** Determine whether the intended markets require a controller/business postal address, representative, lawful-basis/transfer details or additional consumer/child protections. The terms preserve mandatory rights and do not impose arbitration or a fixed monetary liability cap. Obtain appropriate legal review; this draft is not a certification of compliance or enforceability.
- **Support correspondence:** Confirm the described purpose, email provider, retention and deletion-request practice. Unlike local app behavior, these practices cannot be verified from Kotlin source. Establish a real support-retention process; no arbitrary deletion deadline is promised.
- **Date and release:** The draft date is 24 October 2026. Confirm or revise it when approving publication. Phase 1.2 is completed in the documentation; Phase 1.3 remains pending. Re-audit if features, permissions or dependencies change before distribution.
- **Backup behavior:** The draft accurately discloses enabled Android backup with eligible preferences and excludes `noBackupFilesDir` media/session/export records. Confirm this is intentional. Gallery/cloud providers operate independently. Disabling all app backup would require a separately approved Android change, not a wording change alone.
- **Commercial plans:** Confirm currently free, no accounts, no cloud processing, no added JASCUT watermark and no ads/subscriptions/purchases. Future ads are possible; add actual SDK, data, consent and user-choice disclosures before an advertising release. Do not publish speculative current AdMob/Firebase claims.
- **Notices/assets:** Confirm ownership or permission for the existing JASCUT mark. This website adapts that app-owned vector; it uses no stock assets or other apps’ icons. Choose a repository license if desired; public visibility alone is not an open-source license.

## Keeping the policies accurate

Update both pages’ visible dates when practices change. Edit the static HTML directly and rerun validation. Keep current capabilities distinct from plans. Read `AUDIT.md` before changing statements about network access, storage or backups. The site contains no automatic consent mechanism and does not by itself satisfy any required in-app disclosure or consent flow.
