from flask_sqlalchemy import SQLAlchemy
from flask_name import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Some int param
    rating = db.Column(db.Integer, nullable=False)

    def del_from_db(self):
        db.session.delete(self)
        upd()

    def add_to_db(self):
        db.session.add(self)
        upd()

    def upd_db(self):
        upd()

    def __repr__(self):
        return f"{self.username} - {self.email} - {self.rating}"


def upd():
    db.session.commit()
