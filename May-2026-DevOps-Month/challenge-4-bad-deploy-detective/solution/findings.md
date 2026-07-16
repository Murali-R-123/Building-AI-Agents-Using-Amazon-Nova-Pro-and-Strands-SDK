# Challenge 4 — Findings

## Root cause

The AWS DevOps Agent identified that the Lambda function code was correct, but its execution role was missing the required IAM permission to access the DynamoDB table `challenge4-data`.

The Lambda execution role only had the `AWSLambdaBasicExecutionRole` policy attached, which provides CloudWatch Logs access but does not grant permission to perform DynamoDB operations.

As a result, every invocation failed with an `AccessDeniedException` when attempting to execute the `dynamodb:GetItem` operation.

---

## Fix applied

I updated the Lambda execution role by adding an IAM policy that grants the `dynamodb:GetItem` permission on the `challenge4-data` DynamoDB table.

After updating the IAM permissions:

- The Lambda function executed successfully.
- The DynamoDB item was retrieved successfully.
- No further `AccessDeniedException` errors occurred.
- The CloudWatch alarm `challenge4-app-fn-errors` returned to the **OK** state.
- The AWS DevOps Agent confirmed that the application was healthy.

---

## Verification

| Check | Status |
|-------|--------|
| Lambda Execution | ✅ Successful |
| DynamoDB Access | ✅ Successful |
| AccessDeniedException | ✅ Resolved |
| CloudWatch Alarm (`challenge4-app-fn-errors`) | ✅ OK |
| AWS DevOps Agent Health Check | ✅ Healthy |

---

## Evidence

- [x] Screenshot 1: AWS DevOps Agent root-cause investigation
- [x] Screenshot 2: AWS DevOps Agent confirmation showing the function is healthy