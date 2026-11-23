# Minimal EvalAI submission example

This example checks whether EvalAI starts a FALCON M2 test submission.
The container prints a marker and exits before loading a model or data.

You need a running Docker engine and an EvalAI account enrolled in FALCON.
The commands below use `uv` to install Python 3.11 and the official EvalAI CLI
on first use. If `uv` is missing on Linux or macOS, run
`curl -LsSf https://astral.sh/uv/install.sh | sh` and open a new terminal.
[uv installation instructions for other platforms](https://docs.astral.sh/uv/getting-started/installation/)

Run these commands from the repository root. The CLI reuses your existing EvalAI
login. To sign in for the first time, run `uv run evalai_cli.py login`.

```bash
uv run evalai_cli.py --version
docker build --platform linux/amd64 -t falcon-diagnostic:latest .
uv run evalai_cli.py push falcon-diagnostic:latest --phase few-shot-test-2319 --private
```

Use the ID printed by the push command to check the status.

```bash
uv run evalai_cli.py submission SUBMISSION_ID
```

Seeing `FALCON_QUEUE_PROBE_STARTED` in the remote logs confirms the container ran.
It intentionally exits with code **42**, so a failed evaluation is expected.
If the status stays `submitted`, the submission ID and timestamp let maintainers
trace the delay.
