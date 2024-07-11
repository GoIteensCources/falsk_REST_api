from app import app
from app.models import *
import json

quotes = "/media/work/Disk/GoITeens_tech/2_semestr/12_flask_RESTAPI/quotes.json"


def mock_data():
    with open(quotes) as q:
        data = json.load(q)
        for quote in data:
            QuotesModel(**quote)
            db.session.add(QuotesModel(**quote))
    db.session.commit()
    print("mock data added")


with app.app_context():
    db.create_all()
    print("database created")

    mock_data()
