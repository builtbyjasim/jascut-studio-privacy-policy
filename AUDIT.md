# JASCUT Studio policy source audit

Audit date: **24 October 2026**. This describes the inspected local working tree, including existing uncommitted Phase 1.2 work. No Android edits were made for this website. Source inspection does not establish runtime behavior on every device, statutory compliance or enforceability of the terms.

## Reference sites and contact provenance

Read the actual `main/index.html` and `main/terms.html` for:

- <https://github.com/builtbyjasim/pathkeeper-privacy-policy>
- <https://github.com/builtbyjasim/netblocker-privacy-policy>

Raw GitHub content was fetched after the web reader could not retrieve the repository pages. Path Keeper provides a clean reading column, semantic sections and reciprocal legal navigation. Net Blocker adds a branded icon, responsive card, light/dark styles and visible effective date. The new site preserves those conventions with JASCUT navy/indigo tokens, a contents index and print styling. Policy claims from those unrelated apps were not copied into JASCUT.

Both references publish `zasimkhan3@gmail.com`; Net Blocker explicitly names **Jasim Khan**. This verifies consistency with the developer’s published references, not legal identity, inbox access or email delivery.

Target public endpoint `https://api.github.com/repos/builtbyjasim/jascut-studio-privacy-policy/contents/` returned **HTTP 404**. No remote content was overwritten and no repository was created. Private/nonexistent/unavailable cannot be distinguished from that response alone.

## Evidence map

All paths below are relative to the Android repository, not files to copy into this policy repository.

| Finding | Source inspected | Policy consequence |
| --- | --- | --- |
| Kotlin + Compose; one `:app` module; package preserved; minSdk 31 | `app/build.gradle.kts`, `settings.gradle.kts`, `gradle/libs.versions.toml` | Native Android 12+ scope; no React Native/iOS claim |
| Phase 1.2 complete, 1.3 pending; tested limitations documented | `docs/ARCHITECTURE.md`, `docs/PHASE_1_2_NATIVE_TIMELINE.md`, earlier export/UI reports | No claim of a complete editor or production performance acceptance |
| Current video import, trim, reordering, playlist preview and timeline | `feature/editor/trimmerge/*`, `feature/editor/timeline/*`, `domain/model/EditedTimeline.kt`, `media/playback/*` under the production package | Implemented features listed truthfully; compressed seeking is not promised frame-perfect |
| Maximum two clips; one session | `data/repository/EditingSessionRepositoryImpl.kt`, `OrderedVideoPicker.kt` | No multiple named-project library claim |
| Future tools kept separate from implementation | `core/designsystem/help/HelpRegistry.kt`, Phase 1.2 limitations, and the developer’s requested product roadmap | Multi-layer/effects/transitions/keyframes/filters/text/subtitles/photo kept separate |
| Selected-video picker/fallback and private streamed copies | `feature/mediaimport/MediaImportRoute.kt`, `OrderedVideoPicker.kt`, `data/repository/VideoImportRepositoryImpl.kt` | No broad library scanning; cloud picker provider caveat |
| Local names, sizes, MIME, duration, dimensions, rotation and SHA-256 content hashes | `VideoImportRepositoryImpl.kt`, `EditingSessionRepositoryImpl.kt` | Disclose local metadata and integrity/identity use |
| Source copies and `session.json`/`current.json` use `noBackupFilesDir/video_imports` | Same repositories | No developer cloud project backup; retention and prune behavior disclosed |
| In-memory, bounded thumbnail cache | `media/thumbnails/ThumbnailLoader.kt`, `VideoThumbnailProvider.kt` | No persistent disk filmstrip or thumbnail-upload claim |
| MP4 rendered locally; resolution caps and existing audio | `media/processing/VideoCompositionEngine.kt`, `domain/model/VideoExportSettings.kt` | No remote processing, universal encoding or upscale guarantee; no JASCUT watermark operation found |
| `Movies/JASCUT Studio/`; pending rows verified before publication | `media/export/MediaStorePublisher.kt`, `OutputVerifier.kt` | Shared exports outlive uninstall; incomplete owned outputs may be cleaned |
| Intermediate files under `noBackupFilesDir/intermediate_outputs` | `media/export/IntermediateOutputManager.kt` | Completed files may persist; do not promise every temporary file is immediately deleted |
| Export metadata stored locally under `noBackupFilesDir/export_records` | `core/navigation/StudioModels.kt`, `data/repository/FileExportRecordStore.kt` | Disclose output metadata and no-backup placement |
| Share/view content URI with read grant | `media/export/ExportIntents.kt` | Recipient controls subsequent handling; no automatic social upload |
| Appearance and motion use SharedPreferences | `data/repository/PreferencesRepositoryImpl.kt` | Eligible preferences may enter OS backup |
| `allowBackup=true`; sample backup rules have no active exclusions for preferences | `app/src/main/AndroidManifest.xml`, `res/xml/backup_rules.xml`, `res/xml/data_extraction_rules.xml` | Never claim all Android backup is disabled |
| Source manifest declares no uses-permission entries; existing merged release adds library permissions | `app/build/intermediates/merged_manifests/release/processReleaseManifest/AndroidManifest.xml` | Disclose actual merged permissions, not just source manifest |
| `ACCESS_NETWORK_STATE` and `WAKE_LOCK` originate from Media3 1.11.1 | `app/build/outputs/logs/manifest-merger-release-report.txt` | Declaration does not prove a wake lock is held during export |
| Signature `com.builtbyjasim.jascutstudio.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION` | Existing merged release manifest, AndroidX merger entries | Internal receiver protection, not personal-data permission |
| No INTERNET, camera, RECORD_AUDIO, location, broad storage/media, notification or advertising-ID permission in merged release | Existing merged release manifest | No microphone-recording or permission-dialog inventions |
| Embedded AndroidX, Material/Compose, Kotlin coroutines and Media3; no ad/billing/analytics/account SDK in declared dependencies | `app/build.gradle.kts`, `gradle/libs.versions.toml`; source scan | No current AdMob, billing, Firebase, Crashlytics or Sentry disclosure |
| No app-operated endpoint or upload code found in production source scan | Production Kotlin and resources | No JASCUT media-upload service; OS/store/support/site services distinguished |
| JASCUT brand vector and colors already owned by the project | `res/drawable/jascut_brand.xml`, `core/designsystem/theme/Color.kt` | SVG adaptation and #0d1120 / #414fbb / #b3beff branding; no third-party editor logos |

Merged manifests are existing build artifacts, not freshly generated by this website task. Their permission provenance was checked against the current dependency declarations and manifest merger report. Rebuild/recheck the exact release artifact before distribution. This is a source/privacy audit, not packet-capture evidence or an exhaustive third-party SDK binary audit.

## Relevant platform guidance consulted

- Google Play User Data: <https://support.google.com/googleplay/android-developer/answer/10144311>
- Android Auto Backup, including preferences and no-backup directories: <https://developer.android.com/identity/data/autobackup>
- Android shared media and media picker: <https://developer.android.com/training/data-storage/shared/media>
- GitHub Privacy Statement, including Pages visitor IP handling: <https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement>

The website references GitHub hosting separately from offline app processing. It introduces no tracking, fonts or third-party content requests of its own.

## Required publisher/legal review

See the complete checklist in `README.md`: appropriate legal/controller identity and contact, intended markets and child audience, any required business address/lawful-basis/transfer disclosures, support retention process, approved date, actual release behavior, future monetization disclosures, and asset ownership. No jurisdiction, company registration, physical address, fixed response deadline, permanent free/ad-free guarantee or blanket GDPR/CCPA compliance claim has been invented. These documents have not been reviewed by legal counsel.

## Verification

- `python3 tools/validate.py` — passed for both pages: balanced markup, unique IDs, accessible label references, relative page/asset/fragment links, local-only loaded resources, required content, SVG XML, CSS block balance and Pages files.
- `html-validate` **11.17.0**, recommended preset (`tools/htmlvalidate.json`) — passed with exit code 0 for `index.html` and `terms.html`. A temporary npm cache was used; nothing was added to app or website runtime dependencies. Initial validation found 5 issues (doctype style and semantic region labeling); all were corrected and the same check passed afterward. A first local npm invocation reported a Node 23 engine warning; the final invocation explicitly selected the installed Node 24 runtime.
- Live local-browser width checks on both pages at **320, 390, 768, 1024 and 1280 CSS pixels** — no document horizontal overflow. No broken images found on the Privacy page; both use the same local brand asset. Desktop and 390px mobile screenshots inspected; mobile permissions table readable and contained.
- Header navigation Privacy → Terms → Privacy, permissions contents anchor, Back to top and keyboard activation of Skip to content — verified. Skip link moved focus to `main`. Header current-page state changed correctly. Local browser warning/error log was empty in the inspected session.
- Principal text/background colors were calculated at **5.36:1 or higher** in the checked light and dark palette pairs. This is not a full automated accessibility audit or screen-reader certification. Dark-mode and print CSS were checked structurally; neither was separately visually emulated. Keyboard checks were targeted rather than exhaustive.
- Local HTTP checks and source-preservation results are recorded in the completion note below.
- SHA-256 comparison of **151 Android/source files** (excluding Git, build, Gradle and IDE generated directories) found **zero changes** during the website task. Android configuration, source, documentation and the separate HTML design project were not edited. No Gradle compilation or Android test was run for this static website task.
- A local preview server was used for browser QA and stopped afterward. Browser screenshots are supplied as separate review artifacts, outside the repository package. No GitHub Pages deployment, live URL verification or Play Console change is part of this task. No Gradle build is necessary for static website changes; the Android project is intentionally untouched.


### Completion note

Local `GET /index.html` and `GET /terms.html` checks each returned **HTTP 200**. Browser rendering also loaded `assets/styles.css` and `assets/brand-mark.svg`. All 151 snapshotted source hashes remained unchanged. No commit, push, remote write or deployment was executed. The package is prepared for `main` / repository root and awaits developer approval and the confirmations in README. Screenshots in the separate review folder show the actual local pages, not generated mockups.


## Source upload authorization — 24 October 2026

After the initial local-only delivery, the developer explicitly requested a push. Git remote access succeeded and cloning the target reported an empty repository. The prepared website files were transferred to that checkout for the initial commit on `main`. GitHub Pages settings remain unchanged; legal-review confirmations still apply before publication. The Android repository is a separate checkout and is not part of this commit.
