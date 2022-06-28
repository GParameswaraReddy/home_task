**Title:Vocher Selection API**

**TOOLS:**
    Apache Airflow - Job orchestrator that executes workflows
    Docker - containerisation and standardisation of processes
    Postgres - Database to store data
This project uses Python, SQL programming languages,so please install python 3.7 version and postgres 14. 

**Problem statement:**

Analysis of a dataset which includes cleaning and transforming it, in order to derive what is the most used voucher value among predefined customer segments.

segment category as mentioned below:

**frequent_segment** -  number of orders for customer
Segments variants:
  "0-4" - customers which have done 0-4 orders
  "5-13" - customers which have done 5-13 orders
  "14-37" - customers which have done 14-37 orders    
**recency_segment** -  days since last customer order by a customer
Segments variants:
  "30-60" - 30-60 days since the last order
  "61-90" - 61-90 days since the last order
  "91-120" - 91-120 days since the last order
  "121-180" - 121-180 days since the last order
  "180+" - more than 180 days since the last order.
 
** Data Cleaning:**

The dataset was filtered and cleaned according to the following criteria:

Only entries holding the Peru country code were included
Entries with total_orders of 0 but with last_order_ts or first_order_ts were discarded.
Entries with last_order_ts that took place before first_order_ts were discarded.
Entries with null total_orders or voucher_amount were discarded.
  
