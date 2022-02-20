---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: image_alt_015
severity: major
title: image_alt_015
summary: Відсутній альтернативний текст у зображення з селектором `div[data-slide-index="\35 "] > .t-margin_auto.t-width.t-width_6 > .t-slds__wrapper.t-align_center > .t605__img.t605__img_circle[imgfield="li_img__1618401850387"]`
---
<!-- # {{summary}} -->
# Bug report `image_alt_015`

SUMMARY|{{summary}}
-|-
ID|image_alt_015
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
2|користуючись DevTools знайди зображення з наступним CSS-селектором: `div[data-slide-index="\35 "] > .t-margin_auto.t-width.t-width_6 > .t-slds__wrapper.t-align_center > .t605__img.t605__img_circle[imgfield="li_img__1618401850387"]`
<!-- 3|переконайся що вказане зображення має текстову альтернативу -->

## Expected result

Зазначене зображення має альтернативний текст з відповідним значенням

## Actual result

У зазначенного зображення відсутній альтернативний текст

