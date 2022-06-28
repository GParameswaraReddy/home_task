import json
import os

# from tests import env_variables
#
# env_variables.add_os_variables()

import app
from flask import Flask
from flasklib.apis import voucher_refactor_api

def test_health_check():
    app = Flask(__name__)
    voucher_refactor_api(app)
    client = app.test_client()
    url = '/api/healthcheck'

    response = client.get(url)
    assert response.status_code == 200

def test_voucher_factor():
    app = Flask(__name__)
    voucher_refactor_api(app)
    client = app.test_client()
    url = '/api/vouchervalue'
    data = {
            "country_code": "Peru",
            "last_order_ts": "2020-03-22 00:00:00+00:00",
            "first_order_ts": "2014-04-17T05:30:00.000+05:30",
            "total_orders": 36,
            "segment_name":"frequent_segment"
    }

    response = client.post(url, data = json.dumps(data))
    assert response.status_code == 200