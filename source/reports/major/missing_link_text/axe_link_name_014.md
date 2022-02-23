---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: link_name_014
severity: major
title: link_name_014
summary: Відсутнє текстове значення у посилання з селектором `.tn-elem__4015363661642340466012 > a`
---
Bug report `link_name_014`

SUMMARY|Відсутнє текстове значення у посилання з селектором `.tn-elem__4015363661642340466012 > a`
-|-
ID|link_name_014
SEVERITY|major

## Description

Текст посилання, 
самостійно або у контексті оточуючого текстового контента, 
повинен чітко визначати призначення цього посилання.

Вимога: 

- [WCAG 2.4.4 Link Purpose (In Context)](https://www.w3.org/TR/WCAG21/#link-purpose-in-context)
- [WCAG 4.1.2 Name, Role, Value](https://www.w3.org/TR/WCAG21/#name-role-value)

## Environment

- Windows 10 (64-біт) Версія 21H1 (збірка системи 19043.1526)
- Mozilla Firefox 97.0.1 (64-біт)

## Steps to reproduce

|#|Step|
-|-
1|відкрий [odynokovteam.kiev.ua/about](http://odynokovteam.kiev.ua/about)
2|користуючись DevTools знайди посилання з наступним CSS-селектором: `.tn-elem__4015363661642340466012 > a`
<!-- 3|переконайся що вказане зображення має текстову альтернативу -->

## Expected result

Посилання з CSS-селектором `.tn-elem__4015363661642340466012 > a` має текстове значення, 
яке чітко і зрозуміло описує призначення цього посилання. 

## Actual result

У посилання з CSS-селектором `.tn-elem__4015363661642340466012 > a` 
відсутнє текстове значення.
