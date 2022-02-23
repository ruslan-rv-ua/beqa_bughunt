---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
data:
  - test: нетекстовий контент
    result: проведено
  - test: зрозумілість контента
    result: in progress
  - test: семантика розмітки сторінки
    result: planned
  - test: трейсінг фокуса скрінрідера по сторінці
    result: planned
  - test: процес запису до команди
    result: не проведено - форма запису повністю недосяжна для асистивних технологый
---
# Журнал тестування

#|test|result
-|-|-
{% for row in data -%}
{{loop.index}}| {{row.test}} | {{row.result}}
{% endfor %}
