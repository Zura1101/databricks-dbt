{{
    config(
        materialized='table',
        pre_hook=[
            "{{ create_audit_log_if_not_exists() }}",
            "{{ log_audit_event(this.name ~ '_pre', 0) }}"
        ],
        post_hook=[
            "{{ log_audit_event(this.name ~ '_post', target.sql_cmd) }}"
        ]
    )
}}  

SELECT
    customer_id,
    first_name,
    last_name,
    email,
    COUNT(DISTINCT order_id) as total_orders,
    SUM(total_amount) as lifetime_value
FROM {{ ref('int_customer_orders') }}
GROUP BY 1, 2, 3, 4