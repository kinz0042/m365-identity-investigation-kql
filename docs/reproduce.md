# Reproduce the first correlation

Use a free Azure Data Explorer database. This does not require Sentinel.

1. Open detections/load-fixture.kql and run the complete management command in an empty query editor. It creates/appends the custom IdentityLab table.
2. Run detections/device-code-to-forwarding.kql as one complete query block.
3. Expect exactly two rows, approved_forwarding and suspicious. Compare source IDs with tests/expected-results.json.
4. Pin the result to a dashboard if needed. The query uses fixed fixture timestamps and no dashboard time parameters. The dashboard time picker does not filter this tile.

Loading the fixture again appends repeated records. Exact-row deduplication keeps findings stable. In a larger lab, define source-ID conflict handling before trusting duplicate IDs.

The separate device-code-signins.kql file is an unexecuted native SigninLogs hunt. It cannot run against IdentityLab without an adapter. Do not report it as validated.

## Expanded version-two validation

Run load-fixture-v2.kql once, then validate-v2.kql as a single query block. Each of the 16 rows should have Passed=true. Run validation-summary-v2.kql and expect Cases=16, PassedCases=16, FailedCases=0 and Findings=6. Run data-quality-v2.kql and expect one conflicting ID with two variants. Run forwarding-rule-review-v2.kql to inspect the 12 rule changes.

The correlation quarantines conflicting Batch/EventId records rather than selecting an arbitrary successful version. Same-time events are included as temporally compatible because no finer sequence is available. This is not a causal-order claim.
