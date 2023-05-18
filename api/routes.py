from . import api
from api.resources.role import RoleAPI
from api.resources.skills import SkillsAPI
from api.resources.vacancy import VacancyAPI
from api.resources.user import UserAPI,UserRoleAPI,UserResumesAPI
from api.resources.login import LoginAPI,RefreshLoginAPI
from api.resources.company import СompanyAPI

api.add_resource(RoleAPI,'/role','/role/<id>',strict_slashes=False)
api.add_resource(SkillsAPI,'/skills','/skills/<id>',strict_slashes=False)
api.add_resource(VacancyAPI,'/vacancy','/vacancy/<id>',strict_slashes=False)
api.add_resource(UserAPI,'/user','/user/<id>',strict_slashes=False)
api.add_resource(UserRoleAPI,'/user/role',strict_slashes=False)
api.add_resource(UserResumesAPI,'/user/resumes','/user/resumes/<id>',strict_slashes=False)
api.add_resource(LoginAPI,'/jwt/create',strict_slashes=False)
api.add_resource(RefreshLoginAPI,'/jwt/refresh',strict_slashes=False)
api.add_resource(СompanyAPI,'/company',strict_slashes=False)
