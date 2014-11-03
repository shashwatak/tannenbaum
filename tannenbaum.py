#!/usr/bin/python

from storage import db
from storage import Portfolio, Position
db.create_all()


admin = Portfolio('admin', 5000)
guest = Portfolio('guest', 100)

position = Position(guest.id, 200)



db.session.add(admin)
db.session.add(guest)
db.session.add(position)
db.session.commit()


portfolios = Portfolio.query.all()

admin = Portfolio.query.filter_by(name='admin').first()
position = Position.query.filter_by(portfolio_id=guest.id).first()

print portfolios
print admin
print guest
print guest.id
print position

