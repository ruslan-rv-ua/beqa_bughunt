---
hide:
#  - navigation # Hide navigation
  - toc        # Hide table of contents
report_id: broken_link_signup_002
severity: critical
title: broken_link_signup_002
summary: Непрацююче друге посилання з текстом "Записатись"
---
# Bug report `broken_link_signup_001`

SUMMARY|{{summary}}
-|-
ID|{{report_id}}
SEVERITY|{{severity}}

<!--
## Description

Текст посилання, 
самостійно або у контексті оточуючого текстового контента, 
повинен чітко визначати призначення цього посилання.
-->

<!--
Вимога: 

- [WCAG 2.4.4 Link Purpose (In Context)](https://www.w3.org/TR/WCAG21/#link-purpose-in-context)
- [WCAG 4.1.2 Name, Role, Value](https://www.w3.org/TR/WCAG21/#name-role-value)
-->

## Environment

- Windows 10 (64-біт) Версія 21H1 (збірка системи 19043.1526)
- Mozilla Firefox 97.0.1 (64-біт)
- NVDA 2021.3.1, локалізація — українська


## Steps to reproduce

|#|Step|Screenreader output|
-|-|-
1|переконайся що скрінрідер запущено і він працює
2|у новій вкладці браузера відкрий [odynokovteam.kiev.ua/about](http://odynokovteam.kiev.ua/about)
3|натисни комбінацію клавіш `NVDA+ctrl+f`|Введіть текст для пошуку  редактор
4|введи текст "Записатись"
5|натисни клавішу `enter`|посилання    Записатись
6|натисни комбінацію клавіш `nvda+F3`|за кліком  посилання    Записатись
7|натисни клавішу `spacebar` щоб активувати посилання|

## Expected result

1. З'являється модальний діалог з інпутом для вводу імені
1. Фокус скрінрідера автоматично встановлюється на інпут для вводу імені
1. Скрінрідер виводить "введіть ваше ім'я редактор"

## Actual result

Фокус скрінрідера не переміщується. Перевірка:

1. натисни комбінацію клавіш `nvda+tab`
1. скрінрідер виводить "Записатись  посилання  у фокусі  відвідане  пов’язане"
