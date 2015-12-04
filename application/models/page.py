from sqlalchemy.sql.expression import text

from application.extensions import db


class Page(db.Model):
    "An HTML page."

    __tablename__ = 'page'

    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column('name', db.Text(), nullable=False)
    html = db.Column('html', db.Text(), nullable=False)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
