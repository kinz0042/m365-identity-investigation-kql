# Release review

Reviewed 15 November 2026. Ready for owner review as a synthetic KQL investigation portfolio lab.

## Executed evidence

- Version one loaded 16 rows and returned two expected review candidates.
- Version two loaded 33 rows and passed all 16 expected-versus-observed cases.
- Version-two correlation returned six candidates, including intentionally legitimate activity.
- The quality query exposed one conflicting event ID with two variants. Correlation quarantines both variants.
- Standalone forwarding review returned 12 changes.
- Three dashboard tiles were viewed and refreshed in the authenticated browser.
- The included 14-second recording uses actual browser screenshots during refresh.

## Reproduction and package checks

Fixture hashes and JSON structure were checked. Expected counts agree with saved live validation. Local Markdown links and common credential patterns were checked by scripts/check_package.py. ZIP integrity was verified. These checks do not replace running KQL in the Microsoft engine.

## Evidence boundaries

All events are generated. No real phishing delivery, credential theft, token replay, mailbox exfiltration or containment was performed. The source-ID and timing logic is validated only on the supplied cases. Production precision, recall, adversarial resilience and native tenant-schema compatibility remain unmeasured.

The original native SigninLogs hunt is a reference draft. The implemented queries operate on custom IdentityLab tables. Native OfficeActivity parameter parsing, session linkage, mailbox-access analysis and a Sentinel deployment remain potential extensions, not release claims.

The dashboard uses fixed replay data. Its time picker does not filter tiles that do not reference time parameters. Microsoft-account dashboard sharing is unavailable in the observed UI. Reviewers can reproduce the queries in their own free cluster from the included files.

The owner approved publication. The project was made public at kinz0042/m365-identity-investigation-kql on 15 November 2026.
