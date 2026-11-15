# Expanded live validation

On 15 November 2026, 33 generated rows were loaded into custom table IdentityLabV2. The live KQL engine returned 16 passed cases, zero failed cases and six correlation findings. This validates fixture behavior rather than production precision or recall.

The expanded cases cover failed authentication, different users, event ordering, a rule just beyond 30 minutes, the exact 30-minute boundary, identical timestamps, missing identity, other authentication protocol, empty forwarding, read-only rule operations, rule modification, mixed-case protocol and conflicting source IDs. One exact duplicate does not multiply a result.

The data-quality query returned conflicting_id-signin with two distinct variants. The correlation removes both variants before joining. The rule event remains available to the standalone forwarding-review query, which returned 12 changes. A missing authentication correlation does not make a mailbox change safe.

Case labels are used for test reporting, never as correlation filters. The approved_forwarding case intentionally matches. Its benign label is fixture ground truth, not an independently collected approval. Same-account timing does not prove token theft, a shared session or unauthorised access. Forwarding configuration does not prove message delivery.

The dashboard retains the original two-row fixture result beside version-two test totals and the conflicting-ID alert. The tests show 16 passed and zero failed. Version-two query proof is regression-v2-summary.jpg. The updated dashboard is dashboard-final.jpg. demo/live-dashboard.mp4 captures an actual refresh through sampled browser screenshots.
