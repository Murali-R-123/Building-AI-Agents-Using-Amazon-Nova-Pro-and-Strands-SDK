# Challenge 5 — Findings

## What I built and how I broke it

I created a custom AWS Lambda function named `challenge5-timeout` to simulate a timeout issue. The function intentionally paused execution for 10 seconds using `time.sleep(10)`, while the Lambda timeout configuration was set to only 3 seconds. This caused every invocation to fail because the execution exceeded the configured timeout.

---

## What the agent found

The AWS DevOps Agent investigated the failures and determined that the Lambda function was timing out because the configured execution timeout (3 seconds) was shorter than the function's execution time. The agent identified a 100% timeout failure rate and explained that the function was blocked long enough to hit the timeout limit on every invocation.

---

## Fix applied

I modified the Lambda function by reducing the sleep duration from 10 seconds to 1 second while keeping the Lambda timeout configured at 3 seconds.

Updated code:

```python
import time

def lambda_handler(event, context):
    time.sleep(1)
    return {
        "statusCode": 200,
        "body": "Hello from Challenge 5"
    }
```

After deploying the updated code, the function completed successfully in approximately 1 second, well within the configured timeout. The AWS DevOps Agent confirmed that the function was healthy and no timeout errors remained.

---

## Evidence

- [x] Screenshot 1: AWS DevOps Agent investigation showing the timeout root cause.
- [x] Screenshot 2: AWS DevOps Agent confirmation showing the Lambda function is healthy after the fix.
- [ ] Bonus: Slack integration / runbook / coding-assistant fix.