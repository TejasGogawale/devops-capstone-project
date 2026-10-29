"""REST routes for customer accounts."""
from flask import Blueprint, abort, jsonify, request
from sqlalchemy.exc import IntegrityError

from service import db
from service.models import Account

accounts_blueprint = Blueprint("accounts", __name__)


def _account_payload():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        abort(400, description="A JSON object is required.")
    required = ("name", "email", "address", "phone_number")
    missing = [field for field in required if not data.get(field)]
    if missing:
        abort(400, description="Missing required fields: " + ", ".join(missing))
    return data


@accounts_blueprint.post("/accounts")
def create_account():
    """Create an account and return its representation."""
    account = Account().deserialize(_account_payload())
    db.session.add(account)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(409, description="An account with this email already exists.")
    response = jsonify(account.serialize())
    response.status_code = 201
    response.headers["Location"] = f"/accounts/{account.id}"
    return response


@accounts_blueprint.get("/accounts")
def list_accounts():
    """Return every account; an empty database returns an empty list."""
    return jsonify([account.serialize() for account in Account.all()]), 200


@accounts_blueprint.get("/accounts/<int:account_id>")
def read_account(account_id):
    """Return one account or a 404 response."""
    account = Account.find(account_id)
    if account is None:
        abort(404, description="Account not found.")
    return jsonify(account.serialize()), 200


@accounts_blueprint.put("/accounts/<int:account_id>")
def update_account(account_id):
    """Update an account or return 404 if it does not exist."""
    account = Account.find(account_id)
    if account is None:
        abort(404, description="Account not found.")
    account.deserialize(_account_payload())
    try:
        account.update()
    except IntegrityError:
        db.session.rollback()
        abort(409, description="An account with this email already exists.")
    return jsonify(account.serialize()), 200


@accounts_blueprint.delete("/accounts/<int:account_id>")
def delete_account(account_id):
    """Delete an account if present and return an empty 204 response."""
    account = Account.find(account_id)
    if account is not None:
        account.delete()
    return "", 204
