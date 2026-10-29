# Capstone submission evidence

This directory contains helpers for collecting **real** evidence from your own lab environment. It intentionally does not include invented test logs, Docker/Kubernetes outputs, Tekton logs, or simulated Kanban screenshots.

## REST cURL outputs

1. Install dependencies: `python -m pip install -r requirements.txt`
2. Initialize the database: `flask --app run:app db-create`
3. Start the app in another terminal: `make run`
4. From the repository root, run `bash submission/collect-rest-evidence.sh`.
5. Inspect each generated file and make sure the HTTP status and account ID match the actual response. The script uses account ID 1 as an example; adjust it if your database returns a different ID.

Generated files:
- `rest-create-done.txt`
- `rest-list-done.txt`
- `rest-read-done.txt`
- `rest-update-done.txt`
- `rest-delete-done.txt`

## Docker and Kubernetes outputs

After building and deploying the image in your lab, run `bash submission/collect-kubernetes-evidence.sh`. Review the current Kubernetes context first with `kubectl config current-context`.

## GitHub Actions and Tekton

- GitHub Actions: open the repository's **Actions** tab, select the actual run, and use its logs/step output. Do not mark a run successful unless GitHub reports success.
- Tekton: use `tkn pipelinerun list` followed by `tkn pipelinerun logs <actual-run-name> -f`. Save the full output from your real run as `pipelinerun.txt`.

## Kanban screenshots

Kanban evidence must be captured from the real GitHub Projects board after the requested story is in the specified column. This repository helper cannot generate genuine screenshots of the live board. Use the exact filenames required by the assessment, and make sure estimates, sprint assignments, and labels are visible when requested.

## Security headers and tests

Run `nosetests -vv --with-spec --spec-color --with-coverage --cover-erase --cover-package=service` in your lab. Save the actual terminal output as `security-headers-done`. To inspect response headers locally, use `curl -i -H 'Origin: http://localhost:3000' http://127.0.0.1:5000/accounts` and verify the CORS and security headers in the response.

Do not submit this guide as execution evidence; it documents how to collect it.
