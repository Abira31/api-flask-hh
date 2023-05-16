from functools import wraps
from flask_jwt_extended import current_user
from flask import jsonify,make_response,request

def is_admin():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if request.method == 'GET':
                return fn(*args, **kwargs)
            else:
                if current_user.is_admin:
                    return fn(*args, **kwargs)
                response = make_response(
                    jsonify(msg="Не достаточно прав"),403
                )
                response.headers["Content-Type"] = "application/json"
                return response
        return decorator
    return wrapper