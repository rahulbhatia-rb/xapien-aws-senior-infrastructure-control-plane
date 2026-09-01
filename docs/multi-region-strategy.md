# Multi-region strategy

Not every service should be active-active.

Classify services by business criticality, RTO, RPO and data constraints.

Patterns:
- active/passive for stateful workloads where operational simplicity matters
- active/active for stateless reads when business need justifies complexity
- regional queues and explicit replay
- DNS failover with health validation
- restore/failover testing as evidence, not documentation only
