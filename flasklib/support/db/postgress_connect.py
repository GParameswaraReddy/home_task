import traceback
import psycopg2


def postgres_connection(parameters):
    try:
        conn = psycopg2.connect(
            database="postgres", user='postgres', password='Welcome@2021', host='localhost', port= '5432'
        )
        conn.autocommit = True
        cursor = conn.cursor()
        query = "SELECT voucher_amount from task.voucher_table where customer_id = '{}' and country_code = '{}' and last_order_ts = '{}' and first_order_ts = '{}' and total_orders = {}"\
            .format(parameters['customer_id'],parameters['country_code'],parameters['last_order_ts'],parameters['first_order_ts'],parameters['total_orders'],parameters['segment_name'])
        print(query)
        cursor.execute(query)
        query_result = [dict(line) for line in [zip([ column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
        conn.commit()
        conn.close()
        print(query_result[0])
        return str(query_result[0])
    except Exception as err:
        traceback.print_exc()
        print(err)