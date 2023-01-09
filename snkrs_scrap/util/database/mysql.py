from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()


def mySqlConnection(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    db.init_app(app)

    with app.app_context():
        db.create_all()


def insert_sneaker(snkr_name, snkr_price, timestamp):

    for name, price in zip(snkr_name, snkr_price):
        alreadyInserted = False
        price = (price.text[2:]).replace('.', '')
        price = float(price.replace(',', '.'))
        name = str(name.text).replace(' ', '')
        name = name.replace('\n', '')
        select = db.select(Sneaker).filter_by(name=name)
        resultSet = db.session.execute(select).scalars()
        for result in resultSet:
            alreadyInserted = True
        if alreadyInserted == False:
            sneaker = Sneaker(name, price, timestamp)
            db.session.add(sneaker)

    try:
        db.session.commit()
    except:
        print('Erro na inserção')


def update_sneaker(snkr_name, snkr_price, timestamp):
    for name, price in zip(snkr_name, snkr_price):
        price = (price.text[2:]).replace('.', '')
        price = float(price.replace(',', '.'))
        name = str(name.text).replace(' ', '')
        name = name.replace('\n', '')
        select = db.select(Sneaker).filter_by(name=name)
        resultSet = db.session.execute(select).scalars()
        for result in resultSet:
            if result.price > price:
                result.price = price
                try:
                    db.session.commit()
                except:
                    print('Erro no update')


def select_sneaker():
    select = db.select(Sneaker)
    result = db.session.execute(select).scalars()
    return result


class Sneaker(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __init__(self, name, price, timestamp):
        self.name = name
        self.price = price
        self.timestamp = timestamp
