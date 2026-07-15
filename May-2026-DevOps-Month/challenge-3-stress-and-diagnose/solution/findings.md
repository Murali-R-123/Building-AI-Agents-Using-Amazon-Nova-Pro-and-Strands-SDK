# Challenge 3 — Findings

## Root cause

The AWS DevOps Agent determined that the EC2 instance `challenge3-stress` was intentionally overloaded by a startup (User Data) script executed during instance launch. The script created one infinite busy-loop (`while true`) process for each available vCPU using `setsid`, causing both CPU cores to remain continuously utilized at nearly 100%.

This sustained CPU usage resulted in poor instance performance and triggered the CloudWatch alarm `challenge3-high-cpu`.

**User Data script responsible:**

```bash
#!/bin/bash
for i in $(seq $(nproc)); do
  setsid bash -c 'while true; do :; done' >/dev/null 2>&1 < /dev/null &
done
```

This script launches persistent CPU-intensive processes that continue running until they are manually terminated.

---

## Fix applied

I connected to the EC2 instance using **AWS Systems Manager Session Manager** and terminated the runaway busy-loop processes using the following command:

```bash
sudo pkill -f 'while true'
```

After stopping the processes:

- CPU utilization dropped from approximately **100%** to **23%**.
- The EC2 instance returned to normal performance.
- The CloudWatch alarm `challenge3-high-cpu` returned to the **OK** state.
- The AWS DevOps Agent confirmed that the instance had recovered successfully.

---

## Verification

| Check | Status |
|-------|--------|
| EC2 Instance State | ✅ Running |
| CPU Utilization | ✅ ~23% (Recovered from ~100%) |
| CloudWatch Alarm (`challenge3-high-cpu`) | ✅ OK |
| AWS DevOps Agent Health Check | ✅ Healthy |

---

## Evidence

- [x] Screenshot 1: AWS DevOps Agent diagnosis showing the root cause
- [x] Screenshot 2: Recovery showing the `challenge3-high-cpu` alarm in **OK** state and confirmation that the instance is healthy