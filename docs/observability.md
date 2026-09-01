# Observability

Every service should provide:
- RED / USE metrics where appropriate
- structured logs
- distributed traces
- correlation IDs across async boundaries
- deployment markers
- dependency health
- cost telemetry
- owned alerts with runbooks

For async systems, trace propagation and message metadata are required to connect producer -> queue -> consumer.
