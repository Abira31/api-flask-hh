from . import api
from api.resources.role import RoleAPI
from api.resources.skills import SkillsAPI
from api.resources.vacancy import VacancyAPI
from api.resources.user import UserAPI


api.add_resource(RoleAPI,'/role','/role/<id>',strict_slashes=False)
api.add_resource(SkillsAPI,'/skills','/skills/<id>',strict_slashes=False)
api.add_resource(VacancyAPI,'/vacancy','/vacancy/<id>',strict_slashes=False)
api.add_resource(UserAPI,'/user','/user/<id>',strict_slashes=False)