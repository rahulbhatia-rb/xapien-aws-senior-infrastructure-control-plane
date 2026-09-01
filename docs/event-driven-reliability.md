# Event-driven reliability

For SQS/SNS-style systems:
- consumers must be idempotent
- retries need bounded exponential backoff
- DLQs require ownership and replay procedures
- queue age matters more than queue depth alone
- poison messages must be isolated
- schema changes must be backwards compatible
- downstream saturation requires backpressure
