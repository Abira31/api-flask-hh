from flask_restful import Resource
from api.models import User,Role
from flask import jsonify,request,make_response
from api.schemas.user import UserBase,UserDetailBase
from pydantic import ValidationError
from api import db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import current_user,jwt_required

class UserAPI(Resource):
    @jwt_required()
    def get(self):
        user = UserDetailBase.from_orm(current_user)
        response = make_response(
            jsonify(user.dict(exclude={"resumes","is_admin","is_active","password"})),
            200
        )
        response.headers["Content-Type"] = "application/json"
        return response
    def post(self):
        try:
            user = UserBase.parse_obj(request.json)
        except ValidationError as e:
            response = make_response(
                e.json(),400
            )
            response.headers["Content-Type"] = "application/json"
            return response

        user_db = User(**user.dict())
        try:
            db.session.add(user_db)
            db.session.commit()
            return [],201
        except IntegrityError:
            db.session.rollback()
            response = make_response(
                {"msg":"Пользователь с такой почтой уже существует"}, 400
            )
            response.headers["Content-Type"] = "application/json"
            return response

class UserRoleAPI(Resource):
    @jwt_required()
    def post(self):
        roles = request.json.get('roles', None)
        roles_db = db.session.query(Role).filter(Role.id.in_(roles)).all()
        if len(roles_db) > 0:
            current_user.roles.clear()
            for role in roles_db:
                current_user.roles.append(role)
            db.session.commit()
            response = make_response(
                {"msg": "Роль(и) добавлена(ы)"}, 201
            )
            response.headers["Content-Type"] = "application/json"
            return response
        response = make_response(
            {"msg": "Роль(и) с таким(и) индентификатором(рами) отсутсвуют"}, 204
        )
        response.headers["Content-Type"] = "application/json"
        return response