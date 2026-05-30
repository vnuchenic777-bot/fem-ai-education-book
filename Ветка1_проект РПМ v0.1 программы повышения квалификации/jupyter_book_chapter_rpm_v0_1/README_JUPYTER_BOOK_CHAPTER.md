# Jupyter Book chapter: РПМ ДПО ИИ 72ч v0.1

## Состав пакета

```text
jupyter_book_chapter_rpm_v0_1/
  chapters/
    rpm_dpo_ai_72h_v0_1.ipynb
  data/
    rpm_dpo_ai_72h_v0_1.yaml
    rpm_dpo_ai_72h_v0_1.json
  TOC_SNIPPET.yml
  NOTEBOOK_CELL_STRUCTURE_AND_CODE.md
  README_JUPYTER_BOOK_CHAPTER.md
```

## Как подключить в `_toc.yml`

Добавьте строку:

```yaml
- file: chapters/rpm_dpo_ai_72h_v0_1
```

или подключите главу внутри раздела:

```yaml
- caption: Методическое проектирование ДПО
  chapters:
    - file: chapters/rpm_dpo_ai_72h_v0_1
```

## Как запускать

Ноутбук не использует внешние закрытые сервисы. Требуемые библиотеки:

```text
pandas
matplotlib
networkx
json
yaml
pathlib
dataclasses
```

Данные читаются из `data/rpm_dpo_ai_72h_v0_1.yaml` и `data/rpm_dpo_ai_72h_v0_1.json`. Ноутбук проверяет, что оба файла содержат одинаковую структуру.

## Примечание

Глава работает строго в рамках ветки №1: проект РПМ v0.1 программы повышения квалификации. Она не расширяет предмет на весь продукт, а показывает методическую модель, визуализации, алгоритмы проверки компетенций и ТЗ на реализацию данного этапа.
