from flask import Flask, request
from flask import Blueprint

health_check_api = Blueprint('health_check_api', __name__)

@health_check_api.route('/api/healthcheck')
def health_check():
    return {
        "status": "RUNNING"
    }
