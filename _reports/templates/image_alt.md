---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: {report_id}
severity: {severity}
title: {report_id}
summary: Відсутній альтернативний текст у зображення з селектором `{selector}`
---
<!-- # {{{summary}}} -->
# Bug report `{report_id}`

SUMMARY|{{{summary}}}
-|-
ID|{report_id}
SEVERITY|{severity}

## Description

Кожне зображення повино мати текстову альтернативу 
щоб користувачі скрінрідерів розуміли його призначення. 

Якщо зображення не несе смислового навантаження (наприклад декоративне), 
тоді текстова альтернатива повинна містити пусте значення, наприклад:

    :::HTML
    <img src="line.jpg" alt="">

Вимога: [WCAG 1.1.1 Non-text Content](https://www.w3.org/WAI/WCAG21/Understanding/non-text-content.html)

## Steps to reproduce

|#|Step|
-|-
1|відкрий [odynokovteam.kiev.ua/about](http://odynokovteam.kiev.ua/about)
2|користуючись DevTools знайди зображення з наступним CSS-селектором: `{selector}`
<!-- 3|переконайся що вказане зображення має текстову альтернативу -->

## Expected result

Зазначене зображення має альтернативний текст з відповідним значенням

## Actual result

У зазначенного зображення відсутній альтернативний текст

