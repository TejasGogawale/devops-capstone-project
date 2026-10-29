"""Tests for the Account REST API."""
import unittest

from service import create_app, db
from service.models import Account


ACCOUNT_DATA = {
    "name": "John Doe",
    "email": "john@doe.com",
    "address": "123 Main St.",
    "phone_number": "555-1212",
}


class TestAccountRoutes(unittest.TestCase):
    """Exercise the public account endpoints."""

    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
        })
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def create_account(self, data=None):
        return self.client.post("/accounts", json=data or ACCOUNT_DATA)

    def test_create_account(self):
        response = self.create_account()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], ACCOUNT_DATA["name"])
        self.assertEqual(response.headers["Location"], "/accounts/1")

    def test_create_requires_json_fields(self):
        response = self.client.post("/accounts", json={"name": "Incomplete"})
        self.assertEqual(response.status_code, 400)

    def test_create_rejects_duplicate_email(self):
        self.create_account()
        response = self.create_account()
        self.assertEqual(response.status_code, 409)

    def test_list_accounts(self):
        self.create_account()
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]["email"], ACCOUNT_DATA["email"])

    def test_list_empty_accounts(self):
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_read_account(self):
        created = self.create_account()
        account_id = created.json["id"]
        response = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], ACCOUNT_DATA["name"])

    def test_read_missing_account(self):
        response = self.client.get("/accounts/999")
        self.assertEqual(response.status_code, 404)

    def test_update_account(self):
        created = self.create_account()
        updated = dict(ACCOUNT_DATA, phone_number="555-1111")
        response = self.client.put(f"/accounts/{created.json['id']}", json=updated)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["phone_number"], "555-1111")

    def test_update_missing_account(self):
        response = self.client.put("/accounts/999", json=ACCOUNT_DATA)
        self.assertEqual(response.status_code, 404)

    def test_update_requires_valid_json(self):
        created = self.create_account()
        response = self.client.put(
            f"/accounts/{created.json['id']}", json={"name": "Only a name"}
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_account(self):
        created = self.create_account()
        response = self.client.delete(f"/accounts/{created.json['id']}")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, b"")
        self.assertEqual(self.client.get("/accounts").json, [])

    def test_delete_missing_account(self):
        response = self.client.delete("/accounts/999")
        self.assertEqual(response.status_code, 204)

    def test_update_conflicting_email(self):
        self.create_account()
        other = dict(ACCOUNT_DATA, email="jane@doe.com", name="Jane Doe")
        self.create_account(other)
        response = self.client.put("/accounts/2", json=ACCOUNT_DATA)
        self.assertEqual(response.status_code, 409)


if __name__ == "__main__":
    unittest.main()
