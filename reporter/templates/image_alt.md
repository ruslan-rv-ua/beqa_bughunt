{% set summary = "Відсутній альтернативний текст у зображення з селектором `" + selector + "`" -%}
---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: {{report_id}}
severity: {{severity}}
title: {{report_id}}
summary: {{summary}}
---
# Bug report `{{report_id}}`

SUMMARY|{{summary}}
-|-
ID|{{report_id}}
SEVERITY|{{severity}}

## Description

Кожне зображення повино мати текстову альтернативу 
щоб користувачі скрінрідерів розуміли його призначення. 

Якщо зображення не несе смислового навантаження (наприклад декоративне), 
тоді текстова альтернатива повинна містити пусте значення. 
У такому разі скрінрідер буде ігнорувати зображення.
Наприклад:

    :::HTML
    <img src="line.jpg" alt="">

Вимога: [WCAG 1.1.1 Non-text Content](https://www.w3.org/TR/WCAG21/#non-text-content)

## Environment

- Windows 10 (64-біт) Версія 21H1 (збірка системи 19043.1526)
- Mozilla Firefox 97.0.1 (64-біт)

## Steps to reproduce

|#|Step|
-|-
1|відкрий [odynokovteam.kiev.ua/about](http://odynokovteam.kiev.ua/about)
2|користуючись DevTools знайди зображення з наступним CSS-селектором: `{{selector}}`
<!-- 3|переконайся що вказане зображення має текстову альтернативу -->

## Expected result

Зображення з CSS-селектором `{{selector}}` має текстову альтернативу. 
Її значення:

- пустий текст, якщо зображення не несе смислового навантаження
- текст, який коротко і точно описує зображення

## Actual result

У зображення з CSS-селектором `{{selector}}` 
відсутній альтернативний текст
