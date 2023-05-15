from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import config
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
api = Api(app,prefix='/api/v1')
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/docs/openapi/swagger.yml'  # Our API url (can of course be a local resource)
# from . models import *

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL
)
app.register_blueprint(swaggerui_blueprint)


from . import routes




