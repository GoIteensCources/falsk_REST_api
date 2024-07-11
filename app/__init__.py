import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from settings import Config

# init application of the Flask
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
   SWAGGER_URL,
   API_URL,
   config={
       'app_name': 'Access API'
   }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)



from app.routes import *
from app.routes_api import QuoteListApi, QuoteApi


api.add_resource(QuoteApi,
                 "/api/quotes/<int:id>/",
                 )

api.add_resource(QuoteListApi,
                 "/api/quotes/",
                 )
