{% macro create_audit_log_if_not_exists() %}
  {% set audit_table = target.schema ~ '.audit_log' %}
  
  {% set create_audit_log %}
    CREATE TABLE IF NOT EXISTS {{ audit_table }} (
      model_name STRING,
      event_info STRING,
      timestamp TIMESTAMP
    )
  {% endset %}
  
  {% do run_query(create_audit_log) %}
{% endmacro %}

{% macro log_audit_event(model_name, event_info) %}
  INSERT INTO {{ target.schema }}.audit_log (model_name, event_info, timestamp)
  VALUES ('{{ model_name }}', '{{ event_info }}', current_timestamp())
{% endmacro %}