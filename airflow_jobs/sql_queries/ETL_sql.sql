-- Table: task.voucher_table
CREATE TABLE IF NOT EXISTS task.voucher_table AS(
WITH base AS (
    SELECT current_date AS cur_date,
           timestamp,
           country_code,
           last_order_ts,
           first_order_ts,
           total_orders::double precision::int,
           voucher_amount::double precision::int
    FROM task.data_peru
    WHERE lower(country_code) = 'peru'
      AND total_orders <> ''
      AND voucher_amount <> ''
),
     date_diff_ts AS (
         SELECT *,
                (cur_date::DATE - last_order_ts::DATE) AS datediff_last_order,
                dense_rank() over(order by first_order_ts) as customer_id
         FROM base
     ),
     invalid_entries AS (
         SELECT *,
                CASE
                    WHEN total_orders = 0 AND (last_order_ts IS NOT NULL OR first_order_ts IS NOT NULL) THEN TRUE
                    WHEN last_order_ts < first_order_ts THEN TRUE
                    ELSE FALSE
                    END AS invalid
         FROM date_diff_ts
     ),
     segments AS (
         SELECT *,
                CASE
                    WHEN total_orders BETWEEN 1 AND 4 THEN '1-4'
                    WHEN total_orders BETWEEN 5 AND 13 THEN '5-13'
                    WHEN total_orders BETWEEN 14 AND 37 THEN '14-37'
                    WHEN total_orders > 37 THEN 'out_of_range'
                    END AS frequent_segment,
                CASE
                    WHEN datediff_last_order BETWEEN 30 AND 60 THEN '30-60'
                    WHEN datediff_last_order BETWEEN 61 AND 90 THEN '61-90'
                    WHEN datediff_last_order BETWEEN 91 AND 120 THEN '91-120'
                    WHEN datediff_last_order BETWEEN 121 AND 180 THEN '121-180'
                    WHEN datediff_last_order > 180 THEN '180+'
                    END AS recency_segment

         FROM invalid_entries
         WHERE NOT invalid
     ),
     final_table AS (
       select * ,
              CASE
                  WHEN frequent_segment in ('1-4','5-13','14-37') THEN 'frequent_segment'
                  WHEN recency_segment in ('30-60','61-90','91-120','121-180','180+') THEN 'recency_segment'
                  END AS segment_name
       FROM segments
     )
     select * from final_table);
