from flasklib.support.db import postgress_connect
from flask import Blueprint,request
import traceback,json
voucher_refactor_api = Blueprint('voucher_refactor_api', __name__)

@voucher_refactor_api.route('/api/vouchervalue',methods=['POST'])
def vouchervalue():
    try:
        request_parameters = json.loads(request.data)
        return postgress_connect.postgres_connection(request_parameters)
        # return Response(status_code=200, body={"code": "Success", "message": "Data Synced Successfully"})
    except Exception as e:
        traceback.print_exc()
        print(str(e))
        return 400
        # return Response(status_code=400, body={"code": "BadRequestError", "message": str(e)})

# @health_check_api.route('/api/vouchervalue',methods=['POST'])
# def vouchervalue():
#     try:
#         request_parameters = json.loads(health_check_api.current_request.raw_body.decode())
#         postgress_connect.postgres_connection(request_parameters)
#         return Response(status_code=200, body={"code": "Success", "message": "Data Synced Successfully"})
#     except Exception as e:
#         traceback.print_exc()
#         print(str(e))
#         return Response(status_code=400, body={"code": "BadRequestError", "message": str(e)})






