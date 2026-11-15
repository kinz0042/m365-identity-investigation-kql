# Synthetic replay schema

IdentityLab is a custom Azure Data Explorer table. It is not native SigninLogs or OfficeActivity. All rows are synthetic. Protocol and result conventions borrow from the Microsoft sign-in schema. ForwardTo is a deliberately normalized fixture field, not a claim about a native OfficeActivity column.

Batch scopes replays. EventId identifies the fictional source record. Kind separates signin and mailbox_rule. UserId is the fictional identity key. Case is a test label and is excluded from the join. TimeGenerated is a fictional UTC event time. EvidenceType remains synthetic in every record.

The correlation matches successful deviceCode sign-ins to forwarding-rule changes on the same Batch and UserId within 30 minutes. It does not prove shared sessions, token theft, rule execution or exfiltration. A legitimate approved-forwarding case is intentionally returned to demonstrate the need for analyst context. The query does not suppress it using a hidden test label.

Repeated loading appends the same rows. Exact-row deduplication prevents inflated results. Version one does not handle conflicting IDs. Version two adds a separate quality check and removes conflicting Batch/EventId records before correlation.
