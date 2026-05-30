# Глава 11 для Jupyter Book

## Тема

ТЗ платформенной интеграции курса ДПО «ИИ-инструменты в преподавательской, научной и повседневной работе: от понимания принципов до практического применения».

## Главный файл

- `11_platform_course_integration.ipynb`

## Данные

- `data/platform_course_integration.yaml`
- `data/platform_course_integration.json`
- `data/content_upload_map.csv`
- `data/lessons_map.csv`
- `data/assessment_map.csv`
- `data/content_upload_map.jsonl`
- `data/implementation_tasks.jsonl`

## Дополнительные файлы

- `NOTEBOOK_CELL_STRUCTURE.md` — структура ячеек, ожидаемые результаты, фрагмент `_toc.yml`.
- `CODE_CELLS.py` — полный код всех code-ячеек в формате Python-файла.

## Подключение в Jupyter Book

```yaml
- file: chapters/11_platform_course_integration/11_platform_course_integration
  title: ТЗ платформенной интеграции курса ДПО
```

## Ограничения

Ноутбук работает без внешних закрытых сервисов. Используются только: pandas, matplotlib, networkx, json, yaml, pathlib, dataclasses.
