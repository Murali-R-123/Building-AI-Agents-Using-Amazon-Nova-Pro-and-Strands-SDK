# Challenge 2 — Findings

## Root cause

The AWS DevOps Agent investigated the failing Lambda function `challenge2-broken-fn` and identified that it was throwing a `NameError` on every invocation because the variable `config` was referenced before being defined.

**Error observed:**
```
NameError: name 'config' is not defined
```

The function attempted to execute:

```python
return {"result": config["value"]}
```

However, the `config` variable was never initialized, causing the Lambda to fail with a **100% error rate**. As a result, the CloudWatch alarm `challenge2-broken-fn-errors` was triggered.

---

## Fix applied

The Lambda function was updated by defining the missing `config` dictionary before accessing it.

**Updated code:**

```python
def handler(event, context):
    config = {"value": "hello"}
    return {"result": config["value"]}
```

After deploying the updated code:

- The Lambda function executed successfully.
- The function returned the expected response:
  ```json
  {
    "result": "hello"
  }
  ```
- No further execution errors were observed.
- The CloudWatch alarm `challenge2-broken-fn-errors` returned to the **OK** state.

---

## Verification

The AWS DevOps Agent confirmed that the environment had recovered successfully.

| Check | Status |
|-------|--------|
| Lambda Invocation | ✅ Successful |
| Error Rate | ✅ 0% |
| CloudWatch Alarm | ✅ OK |
| Function Health | ✅ Healthy |

---

## Evidence

- [x] Screenshot 1: AWS DevOps Agent root-cause investigation
- [x] Screenshot 2: Successful Lambda execution and CloudWatch alarm in **OK** state