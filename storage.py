from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    balance = db.Column(db.Float)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return '<Portfolio {0}, balance {1}>'.format(self.name, self.balance)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))
    amount = db.Column(db.Integer)


    def __init__(self, portfolio_id, amount):
        self.portfolio_id = portfolio_id
        self.amount = amount

    def __repr__(self):
        return '<portfolio_id {0}, amount {1}>'.format(self.portfolio_id, self.amount)

