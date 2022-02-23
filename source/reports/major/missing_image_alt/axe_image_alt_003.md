---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: image_alt_003
severity: major
title: image_alt_003
summary: Відсутній альтернативний текст у зображення з селектором `img[imgfield="tn_img_1642337338346"]`
---
# Bug report `image_alt_003`

SUMMARY|Відсутній альтернативний текст у зображення з селектором `img[imgfield="tn_img_1642337338346"]`
-|-
ID|image_alt_003
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
2|користуючись DevTools знайди зображення з наступним CSS-селектором: `img[imgfield="tn_img_1642337338346"]`
<!-- 3|переконайся що вказане зображення має текстову альтернативу -->

## Expected result

Зображення з CSS-селектором `img[imgfield="tn_img_1642337338346"]` має текстову альтернативу. 
Її значення:

- пустий текст, якщо зображення не несе смислового навантаження
- текст, який коротко і точно описує зображення

## Actual result

У зображення з CSS-селектором `img[imgfield="tn_img_1642337338346"]` 
відсутній альтернативний текст