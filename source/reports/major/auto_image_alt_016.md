---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: image_alt_016
severity: major
title: image_alt_016
summary: Відсутній альтернативний текст у зображення з селектором `img[imgfield="tn_img_1643144690567"]`
---
<!-- # {{summary}} -->
# Bug report `image_alt_016`

SUMMARY|{{summary}}
-|-
ID|image_alt_016
SEVERITY|major

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
2|користуючись DevTools знайди зображення з наступним CSS-селектором: `img[imgfield="tn_img_1643144690567"]`
<!-- 3|переконайся що вказане зображення має текстову альтернативу -->

## Expected result

Зазначене зображення має альтернативний текст з відповідним значенням

## Actual result

У зазначенного зображення відсутній альтернативний текст

