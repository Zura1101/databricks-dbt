{% snapshot customer_snapshot %}

{{
    config(
      target_schema=generate_schema_name('snapshots', node),
      unique_key='customer_id',
      strategy='timestamp',
      updated_at='updated_at'
    )
}}

SELECT
    customer_id,
    first_name,
    last_name,
    email,
    updated_at
FROM {{ source('raw', 'raw_customers') }}

{% endsnapshot %}