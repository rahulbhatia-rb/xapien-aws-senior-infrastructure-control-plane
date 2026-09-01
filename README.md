# Xapien AWS Senior Infrastructure Control Plane

Independent proof-of-work inspired by Xapien's public Senior Infrastructure Engineer role.

This project models a cloud-native AWS platform contract for a due-diligence / risk-intelligence product that needs to scale reliably while keeping developer experience, observability, security and cost under control.

> Based only on the public job description. It does not represent Xapien's private architecture.

## Role-aligned architecture

```text
Developers
   |
   v
GitHub Actions / CI
   |
   +--> tests
   +--> security checks
   +--> terraform plan
   +--> policy gate
   |
   v
AWS platform
   |
   +--> ECS / containers
   +--> Lambda / FaaS
   +--> API layer
   +--> SQS / SNS
   +--> RDS / DynamoDB
   +--> Cognito
   +--> S3
   +--> search / orchestration
   |
   v
Observability + SLOs
   |
   +--> metrics
   +--> logs
   +--> traces
   +--> cost
   +--> deployment markers
```

## What the readiness gate checks

### AWS foundation
- multi-AZ networking
- private subnets
- controlled egress
- load balancers
- DNS ownership
- IAM least privilege
- encrypted storage
- backup policies
- CloudTrail / audit visibility

### Compute
- ECS / container health
- Lambda timeout/concurrency configuration
- autoscaling
- health checks
- graceful shutdown
- rollback strategy
- immutable images
- resource sizing

### Event-driven systems
- SQS DLQs
- retry/backoff
- idempotency
- poison-message handling
- SNS ownership
- event schema/versioning
- backpressure

### Datastores
- RDS HA / backups / restore tests
- DynamoDB capacity / hot-partition awareness
- caching strategy
- retention
- encryption
- point-in-time recovery
- search index recovery

### CI/CD
- required reviews
- short-lived AWS credentials
- infrastructure plan checks
- container scanning
- release approvals
- progressive delivery
- rollback
- deployment audit trail

### Observability
- metrics
- structured logs
- distributed traces
- correlation IDs
- SLOs
- alert ownership
- on-call runbooks
- dependency health
- deployment markers
- cost telemetry

### Security
- IAM / Cognito review
- network segmentation
- secret management
- vulnerability scanning
- encryption in transit
- encryption at rest
- audit logging
- data protection controls

### Multi-region readiness
- service classification
- explicit RTO / RPO
- data replication strategy
- failover procedure
- DNS failover
- restore test
- regional dependency review
- game day evidence

## Developer experience

The platform should make the safe path the easiest path. A production service should inherit Terraform modules with secure defaults, CI templates, standard dashboards, SLO scaffolding, deployment metadata, alert routing, cost tags, logging/tracing libraries and rollback conventions.

## Distributed-system failure modes considered

- queue backlog
- duplicate message delivery
- partial downstream failure
- retry storms
- database saturation
- hot DynamoDB keys
- dependency timeout cascades
- bad deploys
- region loss
- stale cache / search index
- authentication dependency failure

## Run locally

```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/production.json
python src/cli.py examples/unsafe.json
```

## 30 / 60 / 90 day plan

### 0-30
- map AWS services, ownership and critical paths
- baseline CI/CD and Terraform workflows
- identify top reliability and cost risks
- map current observability gaps
- learn release / incident patterns

### 31-60
- standardize Terraform modules
- improve ECS/Lambda operational patterns
- improve tracing and deployment correlation
- fix top recurring failure modes
- formalize SLOs and cost ownership

### 61-90
- improve multi-region recovery readiness
- reduce deployment toil
- automate common platform controls
- improve developer self-service
- establish recurring resilience / restore testing

## Success metrics

- deployment failure rate
- MTTR
- SLO attainment
- queue-age / DLQ trends
- restore-test success
- infrastructure drift
- cost per workload
- alert actionability
- developer lead time
- recurring incident rate
