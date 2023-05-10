from flask_restful import Resource
from api.models import User
from flask import jsonify,request,make_response
from api.schemas.user import UserBase,UserDetailBase
from api import db
class UserAPI(Resource):
    def get(self,id=None):
        if not id:
            users_db = db.session.query(User).all()
            users = [UserBase.from_orm(users) for users in users_db]
            response = make_response(
                jsonify([user.dict() for user in users]),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response

        users_db = db.session.query(User).filter_by(id=id).first()
        if not users_db:
            return [],204
        user = UserDetailBase.from_orm(users_db)
        response = make_response(
            jsonify(user.dict()),
            200
        )
        response.headers["Content-Type"] = "application/json"
        return response

