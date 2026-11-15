# Identity and mailbox response workflow

This workflow is a proposed procedure. No real account, mailbox, session or token was changed in this lab.

| Stage | Analyst action | Required record |
| --- | --- | --- |
| Validate | Check source IDs, identity, original UTC times and ingestion coverage. Quarantine conflicting records. | Input hashes, affected identity, gaps and preserved event records |
| Establish context | Verify device-code use and forwarding authorisation through independent user and administrator contact. | Who confirmed what, when, and through which trusted channel |
| Preserve | Preserve sign-in/audit exports, existing rule configuration and relevant message metadata under authorised procedures. | Evidence owner, capture time, hashes and access restrictions |
| Scope | Review other rules, forwarding settings, consent grants and session activity supported by available telemetry. | Related accounts, destinations and missing log sources |
| Escalate | Send the incident lead the timeline, evidence IDs, business impact and uncertainty. | Explicit classification and requested decision |
| Contain | The authorised identity/mail administrator assesses account/session controls and removal of confirmed malicious forwarding. | Approval, action owner, exact target, execution time and observed result |
| Verify | Reinspect rule state and subsequent activity. Check that intended access controls took effect. | Verification evidence, continuing activity and unresolved risk |
| Close or monitor | Close approved benign activity with evidence, or document recovery and monitor for recurrence. | Closure rationale and narrowly scoped tuning |

A same-account time join supports review. It does not prove the same token or attacker. A configured forwarding address does not establish that any message was forwarded. Device-code authentication alone is legitimate in many workflows.

## Approval and execution ledger

Use the fields below for each proposed action. Leave execution and verification blank until supported by evidence.

- Incident ID
- Affected identity and exact proposed action
- Reason and supporting source record IDs
- Business impact and rollback or recovery plan
- Approver and approval time
- Executor and execution time
- Observed outcome and independent verification

## Sources

Microsoft suspicious forwarding-rule investigation guide
https://learn.microsoft.com/en-us/defender-xdr/alert-grading-playbook-inbox-forwarding-rules

Microsoft phishing investigation playbook
https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-phishing

Reference check 15 November 2026. These sources guide the workflow. They do not validate execution in this lab.
