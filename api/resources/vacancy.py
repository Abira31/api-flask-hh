from flask_restful import Resource
from api.models import Vacancy
from api import db
from flask import jsonify,request,make_response
from api.schemas.vacancy import VacancyBase,VacancyDetailBase
from pydantic import ValidationError



class VacancyAPI(Resource):
    def get(self,id=None):
        if not id:
            vacancy_db = db.session.query(Vacancy).all()
            vacancy = [VacancyBase.from_orm(vacancy) for vacancy in vacancy_db]
            response = make_response(
                jsonify([v.dict() for v in vacancy]),
            200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        vacancy_db = db.session.query(Vacancy).filter_by(id=id).first()
        if not vacancy_db:
            return [],204
        vacancy = VacancyDetailBase.from_orm(vacancy_db)
        response = make_response(
            jsonify(vacancy.dict()),
            200
        )
        response.headers["Content-Type"] = "application/json"
        return response

    def post(self):
        try:
            vacancy = VacancyDetailBase.parse_obj(request.json)
        except ValidationError as e:
            response = make_response(
                e.json(),400
            )
            response.headers["Content-Type"] = "application/json"
            return response
        vacancy_db = Vacancy(**vacancy.dict())
        db.session.add(vacancy_db)
        db.session.commit()
        vacancy = VacancyBase.from_orm(vacancy_db)
        response = make_response(
            jsonify(vacancy.dict()),
            201
        )
        response.headers["Content-Type"] = "application/json"
        return response

    def put(self,id):
        vacancy_db = db.session.query(Vacancy).filter_by(id=id).first()
        if not vacancy_db:
            return [],204
        try:
            vacancy = VacancyDetailBase.parse_obj(request.json)
        except ValidationError as e:
            response = make_response(
                e.json(),400
            )
            response.headers["Content-Type"] = "application/json"
            return response
        vacancy_db.name = vacancy.name
        db.session.add(vacancy_db)
        db.session.commit()
        vacancy = VacancyBase.from_orm(vacancy_db)
        response = make_response(
            jsonify(vacancy.dict()),
            200
        )
        response.headers["Content-Type"] = "application/json"
        return response

    def delete(self,id):
        vacancy_db = db.session.query(Vacancy).filter_by(id=id).first()
        if not vacancy_db:
            return [],204
        db.session.delete(vacancy_db)
        db.session.commit()
        return [],204


        