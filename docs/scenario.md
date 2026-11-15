# Investigation design

## Main question

Did suspicious authentication lead to unauthorised mailbox changes or access?

## Planned stages

1. A reported message or user report provides the initial lead. Preserve an authorised sample if available. Do not invent a delivered phishing message.
2. Identify successful deviceCode sign-ins, client applications, users and event times.
3. Review mailbox-rule creation or modification, forwarding targets and independent authorisation context.
4. Inspect mailbox-access evidence only where the available log/licence actually records it.
5. Correlate stable user IDs and verified session identifiers where available. Document limitations when only account and time agree.
6. Recommend evidence preservation, session controls and mailbox remediation. Distinguish recommendation, approval, execution and verified outcome.

## Planned tests

| Case | Expected interpretation |
| --- | --- |
| Successful device code plus unauthorised forwarding rule | Escalate with both source records and authorisation evidence |
| Approved device-code workflow without mailbox changes | Hunt result, no automatic compromise verdict |
| Failed device-code sign-in plus unrelated rule | No successful-authentication chain |
| Rule belonging to another user | Do not correlate |
| Rule before sign-in or outside selected interval | Do not include in the proposed sequence |
| Duplicate source event | Must not inflate counts |
| Missing protocol or user identifier | Report incomplete evidence |
| Travel or shared egress IP | No compromise verdict from location/IP alone |
| Legitimate approved forwarding | Document justification and narrowly scoped tuning |
| Hidden or unavailable risk fields | Continue with evidence limits, never interpret hidden as safe |

No credential collection, token theft or live phishing kit is required. Use controlled benign lab operations or explicitly labelled fixtures to test detection logic.
