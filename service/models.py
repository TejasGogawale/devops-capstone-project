"""Database model for customer accounts."""
from service import db


class Account(db.Model):
    """A customer account stored in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    address = db.Column(db.String(256), nullable=False)
    phone_number = db.Column(db.String(32), nullable=False)

    def serialize(self):
        """Convert this account into a JSON-friendly dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number,
        }

    def deserialize(self, data):
        """Populate account fields from a request dictionary."""
        for field in ("name", "email", "address", "phone_number"):
            if field in data:
                setattr(self, field, data[field])
        return self

    def update(self):
        """Persist changes to this account."""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete this account from the database."""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find(cls, account_id):
        """Find one account by primary key, or return None."""
        return cls.query.get(account_id)

    @classmethod
    def all(cls):
        """Return all accounts as model instances."""
        return cls.query.order_by(cls.id).all()
