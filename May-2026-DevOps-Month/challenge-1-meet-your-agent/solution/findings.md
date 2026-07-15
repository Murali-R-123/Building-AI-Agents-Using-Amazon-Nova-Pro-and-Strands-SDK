# Challenge 1 - Meet Your Agent

## AWS Account Information

- **AWS Account ID:** 366183011774
- **Active Regions:**
  - us-east-1
  - eu-north-1

---

# Resource Inventory

## CloudFormation

| Stack | Region | Status |
|-------|--------|--------|
| challenge-2 | us-east-1 | CREATE_COMPLETE |

### Resources Created

- Lambda Function: `challenge2-broken-fn`
- CloudWatch Alarm: `challenge2-broken-fn-errors`

---

## Compute

| Service | us-east-1 | eu-north-1 |
|---------|-----------|------------|
| Lambda Functions | 1 (`challenge2-broken-fn`) | 0 |

---

## Monitoring

| Service | us-east-1 | eu-north-1 |
|---------|-----------|------------|
| CloudWatch Alarm | 1 (`challenge2-broken-fn-errors`) | 0 |
| X-Ray Sampling Rule | 1 | 1 |

---

## Networking

- Default VPCs in both regions
- Default public subnets
- Default Internet Gateways
- Default Route Tables
- Default Network ACLs
- Default Security Groups

---

## Other AWS Resources

- Athena WorkGroup (primary)
- EventBridge Event Bus (default)
- ElastiCache Default User

---

## Resources Not Present

- EC2 Instances
- RDS Databases
- S3 Buckets
- ECS Clusters
- EKS Clusters

---

# Health Check

## Overall Health

**Status:** ✅ Healthy

### CloudWatch Alarms

| Alarm | Region | State | Description |
|-------|--------|-------|-------------|
| challenge2-broken-fn-errors | us-east-1 | OK | Lambda error alarm – no errors detected |

### Lambda Health

- Lambda function `challenge2-broken-fn` is deployed.
- The function has **not yet been invoked**.
- No execution errors have been recorded.

### CloudFormation Health

- Stack `challenge-2` is in **CREATE_COMPLETE** state.

### Network Health

- Default networking resources are available in both active regions.

---

# Environment Health Summary

| Category | Status | Details |
|----------|--------|---------|
| CloudWatch Alarms | ✅ Healthy | One alarm present and currently in OK state |
| Lambda Functions | ✅ Healthy | Function deployed but not yet invoked |
| CloudFormation | ✅ Healthy | Stack creation completed successfully |
| Networking | ✅ Healthy | Default VPC infrastructure available |

---

# Resource Summary

| Service | us-east-1 | eu-north-1 |
|----------|-----------|------------|
| Lambda Functions | 1 | 0 |
| CloudWatch Alarms | 1 (OK) | 0 |
| CloudFormation Stacks | 1 | 0 |
| VPCs | 1 | 1 |

---

# Observations

- The AWS account initially contained only default AWS infrastructure.
- A CloudFormation stack (`challenge-2`) was successfully deployed.
- The deployment created an intentionally broken Lambda function.
- A CloudWatch alarm has been configured to monitor Lambda execution failures.
- The Lambda function has not yet been executed, so the alarm remains in the **OK** state.
- No application workloads or production resources are currently running.

---

# Conclusion

The AWS DevOps Agent successfully inventoried the AWS account and assessed the health of all deployed resources. The environment is currently healthy because the intentionally broken Lambda function has not yet been invoked. The infrastructure is ready for the next investigation, where invoking the Lambda is expected to generate errors and trigger the associated CloudWatch alarm.