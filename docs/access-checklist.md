# Access decision and scope

Checked 15 November 2026.

The personal Microsoft account could sign in, but the Entra portal rejected tenant access. A Microsoft 365 Business Premium trial requested a payment card, which was unavailable. No paid tenant or Sentinel workspace was provisioned.

With owner approval, a free Azure Data Explorer cluster was created in Europe, with database IdentityInvestigation. Live KQL queries and a three-tile dashboard were verified. No credit card or paid Azure subscription was used.

| Capability | Verified state |
| --- | --- |
| Azure Data Explorer query engine | Available, live queries executed |
| Custom IdentityLab / IdentityLabV2 tables | Loaded with labelled synthetic records |
| Dashboard | Original correlation, version-two validation and conflict alert displayed |
| Entra organisational log access | Not available for this project |
| Native SigninLogs / OfficeActivity ingestion | Not deployed or validated |
| Actual mailbox or token response | Not performed |

The included native SigninLogs query remains an unexecuted reference draft. There is no real-tenant takeover claim. The free cluster is an execution environment for testing KQL on generated fixtures. It does not replace Microsoft 365 licensing or Sentinel ingestion.

Microsoft references are listed in sources.md. Azure Data Explorer free-cluster guidance https://learn.microsoft.com/en-us/azure/data-explorer/start-for-free
