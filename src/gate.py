REQUIRED = {
    "aws":["multi_az","private_subnets","controlled_egress","load_balancer","dns_owner","iam_least_privilege","encryption","backup_policy","audit_visibility"],
    "compute":["container_health","lambda_limits","autoscaling","health_checks","graceful_shutdown","rollback","immutable_images","resource_sizing"],
    "events":["dlq","retry_backoff","idempotency","poison_message_handling","sns_owner","schema_versioning","backpressure"],
    "data":["rds_ha","rds_backups","restore_test","dynamodb_capacity","hot_partition_review","cache_strategy","retention","pitr","search_recovery"],
    "cicd":["required_reviews","short_lived_credentials","terraform_plan","container_scan","release_approval","progressive_delivery","rollback","audit_trail"],
    "observability":["metrics","logs","traces","correlation_ids","slos","alert_owner","runbooks","dependency_health","deployment_markers","cost_telemetry"],
    "security":["cognito_review","network_segmentation","secret_management","vuln_scan","tls","at_rest_encryption","audit_logs","data_protection"],
    "multiregion":["service_classification","rto_rpo","replication_strategy","failover_procedure","dns_failover","restore_evidence","dependency_review","game_day"]
}

def evaluate(spec):
    findings=[]
    for section, fields in REQUIRED.items():
        values=spec.get(section,{})
        for field in fields:
            if not values.get(field):
                findings.append(f"{section}.{field} is required")
    return {"allowed": not findings, "findings": findings}
