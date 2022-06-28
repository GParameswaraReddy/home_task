**Title:Vocher Selection API**

**TOOLS:**
    Apache Airflow - Job orchestrator that executes workflows \
    Docker - containerisation and standardisation of processes \
    Postgres - Database to store data \
This project uses Python, SQL programming languages,so please install python 3.7 version and postgres 14. 

**Problem statement:**

Analysis of a dataset which includes cleaning and transforming it, in order to derive what is the most used voucher value among predefined customer segments.

segment category as mentioned below: \

**frequent_segment** -  number of orders for customer \
Segments variants: \
        * "0-4" - customers which have done 0-4 orders \
        * "5-13" - customers which have done 5-13 orders \
        * "14-37" - customers which have done 14-37 orders \   
**recency_segment** -  days since last customer order by a customer \
Segments variants: \
       * "30-60" - 30-60 days since the last order \
       * "61-90" - 61-90 days since the last order \
       * "91-120" - 91-120 days since the last order \
       * "121-180" - 121-180 days since the last order \
       * "180+" - more than 180 days since the last order. 
 
**Data Cleaning:**

The dataset was filtered and cleaned according to the following criteria:
        - Only entries holding the Peru country code were included
        - Entries with total_orders of 0 but with last_order_ts or first_order_ts were discarded.
        - Entries with last_order_ts that took place before first_order_ts were discarded.
        - Entries with null total_orders or voucher_amount were discarded.

**Project:**
This project divided into two blocks one is ETL job and API code. \
**ETL job** This job is scheduled on Airflow, Airflow DAG again has two jobs one is reading the parquet file and uploading the file into postgres table. once it uploades the data another airflow job process the data and upload into target table. Here in second job we are applying all Transformation required to achieve the desired output.
**API Script:**: This script helped us in getting the desired voucher value using API call. script json post request will be as mentioned below: \
       {       \
     	 "customer_id":"1", \
	 "country_code": "Peru",  \
	 "last_order_ts": "2020-03-22 00:00:00+00:00", \
	 "first_order_ts": "2014-04-17T05:30:00.000+05:30", \
	 "total_orders": 36, \
     "segment_name":"frequent_segment"\
}

url: http://127.0.0.1:5000/api/vouchervalue \
airflow url:http://0.0.0.0:8080/admin/airflow/tree?dag_id=voucher_selection

**Testing:**
Written unit test cases using Pytest module under test folder, To run those jobs we need to use command pytest test/voucher_refactor_test.py.
which will pass or test the requested api with sample block. 

**Remarks**
Credentials used in this project are default credentails for simple project specific.

**Conclusion:**
This has only repetative voucher values and data is old, it has data till 2018. 


    
  
