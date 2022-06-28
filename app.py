import os

from flask import Flask,Blueprint
# from flask_restful import Api,Resource

from flasklib.apis.health_check_api import health_check_api
from flasklib.apis.voucher_refactor_api import voucher_refactor_api

app_name = "voucher-selection-api"
app = Flask(app_name)
# api = Api(app)
# api.add_resource(health_check_api)
app.register_blueprint(health_check_api)
app.register_blueprint(voucher_refactor_api)
