# Minimal EvalAI submission example

This example checks whether EvalAI starts a FALCON M2 test submission.
The container prints a marker and exits before loading a model or data.

Run these commands from the repository root using Docker and the EvalAI CLI
signed in to an account enrolled in FALCON.

```bash
docker build --platform linux/amd64 -t falcon-diagnostic:latest .
evalai push falcon-diagnostic:latest --phase few-shot-test-2319 --private
evalai submission SUBMISSION_ID
```

Replace `SUBMISSION_ID` with the ID printed by `evalai push`. Seeing
`FALCON_QUEUE_PROBE_STARTED` in the remote logs confirms the container ran.
It intentionally exits with code **42**, so a failed evaluation is expected.
If the status stays `submitted`, the submission ID and timestamp let maintainers
trace the delay.
