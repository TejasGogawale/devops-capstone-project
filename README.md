# Account Microservice

[![Account Service CI](https://github.com/TejasGogawale/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/TejasGogawale/devops-capstone-project/actions/workflows/ci-build.yaml)

A Flask REST API for customer accounts with Create, Read, Update, Delete, and List operations. The API uses Flask-SQLAlchemy and SQLite by default.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create the database and start the service:

```bash
flask --app run:app db-create
make run
```

The service listens at `http://127.0.0.1:5000`.

## REST endpoints

| Method | Endpoint | Behavior |
|---|---|---|
| POST | `/accounts` | Create an account (201 Created) |
| GET | `/accounts` | List all accounts (200 OK; empty list when none exist) |
| GET | `/accounts/<account_id>` | Read an account (404 if missing) |
| PUT | `/accounts/<account_id>` | Update an account (404 if missing) |
| DELETE | `/accounts/<account_id>` | Delete an account (204 No Content) |

Every account uses `name`, `email`, `address`, and `phone_number`. Create and update require these fields in a JSON object. Duplicate email addresses return 409 Conflict.

## Tests and quality

```bash
nosetests
flake8 service tests run.py
pylint service run.py
```

The `setup.cfg` file configures Nose's verbose, colored spec output and coverage reporting. Confirm the actual coverage percentage locally after installing dependencies.

## Example

```bash
curl -i -X POST http://127.0.0.1:5000/accounts \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1212"}'
curl -i http://127.0.0.1:5000/accounts
curl -i http://127.0.0.1:5000/accounts/1
curl -i -X PUT http://127.0.0.1:5000/accounts/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1111"}'
curl -i -X DELETE http://127.0.0.1:5000/accounts/1
```

## Agile planning

See [docs/AGILE_PLAN.md](docs/AGILE_PLAN.md) for the original planning artifacts and user-story template at [.github/ISSUE_TEMPLATE/user-story.md](.github/ISSUE_TEMPLATE/user-story.md).
