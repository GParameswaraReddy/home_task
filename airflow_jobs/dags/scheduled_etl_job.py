import pandas as pd
from sqlalchemy import create_engine
from os.path import join, expandvars
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

default_args = {
    'description': 'Voucher Selection pipeline - importing data to PostgresDB + ETL job',
    'start_date': days_ago(2),
    'catchup': False,
}

# set temp output in environment variable
SQL_DIR = join(expandvars('$AIRFLOW_HOME'), 'sql_queries')
# CUR_DATE = expandvars('$CUR_DATE')

def upload_data():
    data = pd.read_parquet(join(SQL_DIR,"data.parquet.gzip")):
    engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
    data.to_sql('task.test_data', engine)

with open(join(SQL_DIR, 'ETL_sql.sql'), 'r') as sql_file:
    etl_sql = sql_file.read()

dag = DAG(dag_id='voucher_selection',
          schedule_interval=None,
          default_args=default_args)

upload_data = PythonOperator(task_id='upload_data',
                             dag=dag,
                             python_callable=upload_data)

voucher_etl_query = PostgresOperator(task_id='voucher_etl_query',
                                    dag=dag,
                                    postgres_conn_id='postgres_db',
                                    sql=etl_sql)
end = DummyOperator(task_id="end")

upload_data >> voucher_etl_query >> end
