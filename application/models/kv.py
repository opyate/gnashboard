from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql.expression import text

from application.extensions import db


class KV(db.Model):
    "A keyvalue store"

    __tablename__ = 'kv'

    id = db.Column('id', db.Integer(), primary_key=True)
    key = db.Column('key', db.Text(), nullable=False)
    value = db.Column('value', JSONB, nullable=False)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
