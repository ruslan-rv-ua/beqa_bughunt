---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: image_alt_014
severity: major
title: image_alt_014
summary: Відсутній альтернативний текст у зображення з селектором `div[data-slide-index="\34 "] > .t-margin_auto.t-width.t-width_6 > .t-slds__wrapper.t-align_center > .t605__img.t605__img_circle[imgfield="li_img__1644330069755"]`
---
<!-- # {{summary}} -->
# Bug report `image_alt_014`

SUMMARY|{{summary}}
-|-
ID|image_alt_014
SEVERITY|major

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
2|користуючись DevTools знайди зображення з наступним CSS-селектором: `div[data-slide-index="\34 "] > .t-margin_auto.t-width.t-width_6 > .t-slds__wrapper.t-align_center > .t605__img.t605__img_circle[imgfield="li_img__1644330069755"]`
<!-- 3|переконайся що вказане зображення має текстову альтернативу -->

## Expected result

Зазначене зображення має альтернативний текст з відповідним значенням

## Actual result

У зазначенного зображення відсутній альтернативний текст

