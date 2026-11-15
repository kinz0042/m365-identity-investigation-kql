# First synthetic investigation

## Scope

Executed on Azure Data Explorer using custom IdentityLab records. These are generated test events, not actual Microsoft 365 logs. Fictional event times are unrelated to the real execution clock.

## Observed result

Sixteen rows were ingested, including one exact duplicate. The KQL returned two review candidates. For each, a successful deviceCode sign-in at 09:20 UTC was followed by a forwarding-rule event at 09:25 UTC for the same fictional user.

| Candidate | Source IDs | Interpretation |
| --- | --- | --- |
| suspicious | suspicious-signin, suspicious-rule | Review candidate requiring independent authorisation and session evidence |
| approved_forwarding | approved_forwarding-signin, approved_forwarding-rule | Deliberate benign test label; the rule correctly does not decide authorisation from telemetry alone |

The failed sign-in, different-user rule, earlier rule, out-of-window rule, missing-user case and legitimate-device-only case were absent from the result. The repeated sign-in did not multiply the finding.

## Limits

Same-account timing does not establish token linkage or account takeover. The fixture contains neither a real phishing message nor independent user confirmation. The benign label is test ground truth, not a collected approval record. Forwarding configuration does not prove email delivery or exfiltration. No response action was performed.

## Next evidence

A real investigation would need the original sign-in and audit exports, session identifiers where available, exact rule parameters, verified user context and mailbox-access evidence. Native OfficeActivity normalization and broader schema coverage are still pending.
