{% macro log_model_start_event() %}
    {% do log("Model " ~ this.name ~ " started", info=True) %}
{% endmacro %}

{% macro log_model_end_event() %}
    {% do log("Model " ~ this.name ~ " finished", info=True) %}
{% endmacro %}