from flask import jsonify
from flask_restful import Resource, reqparse
from app.models import QuotesModel
from app import db


def collect_response(data, code = 200):
    response = jsonify(data)
    response.status_code = code
    return response


class QuoteListApi(Resource):
    def get(self):
        """ Отримати всі цитати з бд"""
        quotes = QuotesModel.get_all()
        response = jsonify(quotes)
        response.status_code = 200
        return response

    def post(self):
        """ Додати цитату до бд """

        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()

        answer = QuotesModel.create(author=params["author"], quote=params["quote"])

        response = jsonify(f"Records create with id {answer}")
        response.status_code = 201
        return response


class QuoteApi(Resource):
    def get(self, id):
        """ Отримати одну цитату по id """
        quote = QuotesModel.get_by_id(id)
        if quote:
            response = jsonify(quote)
            response.status_code = 200
            return response
        response = jsonify({"message": "not found"})
        response.status_code = 404
        return response

    def delete(self, id):
        """ Видалити цитату по id """
        res = QuotesModel.delete(id)
        response = jsonify({"message": f"quote {id} deleted"})
        response.status_code = 200
        return response

    def put(self, id):
        """ Змінити цитату по id """
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()

        QuotesModel.update(id, author=params["author"], quote=params["quote"])

        response = jsonify(f"Records edit with id {id}")
        response.status_code = 202
        return response

