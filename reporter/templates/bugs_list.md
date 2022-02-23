# Список дефектів

|#|ID|SEVERITY|SUMMARY|
-|-|-|-
{% for row in data -%}
{{loop.index}}|{{row.report_id}}|{{row.severity}}|[{{row.summary}}]({{row.link}})
{% endfor %}