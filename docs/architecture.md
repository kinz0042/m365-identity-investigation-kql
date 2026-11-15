# Architecture

```mermaid
flowchart TD
    A[Labelled synthetic events] --> B[Free Azure Data Explorer tables]
    B --> C[Exact duplicate removal]
    C --> D[Conflicting ID quarantine]
    D --> E[Identity and time correlation]
    C --> F[Source quality review]
    E --> G[Expected versus observed tests]
    E --> H[Analyst review and response plan]
    F --> I[Live dashboard]
    G --> I
```

The correlation joins Batch and UserId, then checks the event interval. Case is used only to report fixture outcomes. No join establishes shared tokens or sessions. The standalone forwarding review can surface changes even when authentication cannot be correlated.
