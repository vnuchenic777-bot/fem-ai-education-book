# Publishing Status

Дата проверки: 2026-05-30

## Что собрано

Создан Jupyter Book-репозиторий для книги «Проектирование цифровой образовательной экосистемы факультета: методология, архитектура и реализация курса ДПО по ИИ-инструментам».

Подготовлены:

- корневые файлы Jupyter Book: `_config.yml`, `_toc.yml`, `index.md`, `requirements.txt`;
- публичные главы в `book/`;
- структурированные данные веток в `data/branches/`;
- изображения и диаграммы в `assets/`;
- скрипты проверки `scripts/validate_data.py` и `scripts/check_book.py`;
- GitHub Actions workflow `.github/workflows/deploy-book.yml`;
- правила для будущих AI-агентов в `AGENTS.md`;
- README с командами локального запуска.

## Подключенные ветки и материалы

| Ветка | Статус подключения | Основное расположение |
|---|---|---|
| 1. Проект РПМ v0.1 | подключена как notebook-глава | `book/02_dpo_course_design/course_concept.ipynb` |
| 2. Матрица компетенций | подключена как notebook-глава | `book/02_dpo_course_design/competency_model.ipynb` |
| 3. Учебный план | подключена как notebook-глава | `book/02_dpo_course_design/curriculum_plan.ipynb` |
| 4. Карта уроков и микролекций | подключена как Markdown-глава | `book/02_dpo_course_design/lesson_map.md` |
| 5. Фонд оценочных средств | подключена как Markdown-глава и две notebook-главы | `book/02_dpo_course_design/assessment_model.md` |
| 6. Задания с обязательным использованием ИИ | подключена как Markdown-глава | `book/03_ai_integration_strategy/ai_mandatory_assignments.md` |
| 7. Подробная разработка модулей | подключена как Markdown-глава | `book/02_dpo_course_design/module_development.md` |
| 8. Итоговый проект | подключена как спецификация и приложение | `book/02_dpo_course_design/final_project_model.md` |
| 9. Право, этика, безопасность | подключена как главы стратегии | `book/03_ai_integration_strategy/legal_ethics_security.md` |
| 10. Сертификат или удостоверение | подключена как отдельная часть книги | `book/05_certification/` |
| 11. Платформенная интеграция курса | подключена как notebook-глава архитектуры | `book/01_platform_architecture/architecture_overview.ipynb` |

## Ветка 10

Ветка 10 перенесена в `book/05_certification/` с сохранением:

- `certificate_model.md`;
- `certificate_data_model.ipynb`;
- `certificate_lifecycle.ipynb`;
- `qr_verification_flow.ipynb`;
- `implementation_spec.yaml`;
- `implementation_spec.json`;
- `data/`;
- `assets/diagrams/`;
- предупреждений о необходимости согласования юридического статуса документа с образовательной организацией.

Структурированные данные также сохранены в `data/branches/10_certificate_or_credential/`, диаграммы продублированы в `assets/diagrams/certification/`.

## Ноутбуки, которые исполняются при сборке

При `jupyter-book build .` выполнены и закэшированы:

- `book/01_platform_architecture/architecture_overview.ipynb`;
- `book/02_dpo_course_design/course_concept.ipynb`;
- `book/02_dpo_course_design/competency_model.ipynb`;
- `book/02_dpo_course_design/curriculum_plan.ipynb`;
- `book/02_dpo_course_design/notebook_01.ipynb`;
- `book/02_dpo_course_design/notebook_02.ipynb`;
- `book/05_certification/certificate_data_model.ipynb`;
- `book/05_certification/certificate_lifecycle.ipynb`;
- `book/05_certification/qr_verification_flow.ipynb`.

Все проверенные notebooks парсятся как JSON и содержат Markdown-ячейки с объяснениями. Старые outputs с абсолютными путями `/mnt/data` удалены из публикуемых notebooks.

## Ноутбуки, требующие ручной проверки

- `book/01_platform_architecture/platform_course_integration_executed.ipynb` сохранен как дополнительный executed-вариант, но не включен в `_toc.yml`.
- Исходные notebooks в оригинальных папках веток сохранены для трассировки. Они не входят в публичную сборку, потому что публичные версии подключены через `book/`.

## Результаты проверок

Команды выполнены в локальном `.venv`:

```bash
.venv/bin/python scripts/validate_data.py
.venv/bin/python scripts/check_book.py
.venv/bin/jupyter-book build .
```

Результаты:

- `scripts/validate_data.py`: OK, проверено 70 JSON и 80 YAML.
- `scripts/check_book.py`: OK, проверено 38 TOC-целей.
- `jupyter-book build .`: OK, HTML создан в `_build/html`.

## Локальная сборка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_data.py
python scripts/check_book.py
jupyter-book build .
python -m http.server --directory _build/html 8000
```

Для Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts\validate_data.py
python scripts\check_book.py
jupyter-book build .
python -m http.server --directory _build/html 8000
```

## GitHub Pages

Workflow `.github/workflows/deploy-book.yml` настроен на публикацию `_build/html` через GitHub Actions при push в `main`.

Чтобы включить публикацию:

1. Создать GitHub-репозиторий.
2. Заменить `repository.url` в `_config.yml` на фактический URL.
3. Отправить ветку `main` в GitHub.
4. В GitHub открыть **Settings → Pages**.
5. В **Build and deployment → Source** выбрать **GitHub Actions**.
6. Запустить workflow push-ем или вручную через `workflow_dispatch`.

## Что требует доработки

- Указать автора книги в `_config.yml`.
- Заменить `TODO_USERNAME/TODO_REPOSITORY` на реальный URL GitHub-репозитория.
- Добавить библиографию в `bibliography.bib`.
- Заполнить черновые разделы: видение продукта, API-модель, PWA-стратегия, роли, хранение, научные статьи.
- Согласовать юридический статус документа об обучении, порядок подписи, регистрации, хранения, отзыва и публичной проверки.
- Проверить, какие материалы можно публиковать открыто, а какие должны остаться внутренними.

## Рекомендуемая следующая задача

Подготовить содержательное редактирование вводных и архитектурных глав: заменить черновики на связный публичный текст, уточнить автора, репозиторий, границы публикации и список материалов, которые можно раскрывать на GitHub Pages.
