# Publishing Status

Дата проверки: 2026-06-01

## Обновление этапа

Добавлены авторские метаданные, начальная библиография, академически отредактированные вводные и архитектурные главы, проектная позиция по юридическому статусу сертификата/удостоверения и рамка открытой публикации материалов.

## Обновление от 2026-06-01

Ветка 8 усилена воспроизводимой Jupyter-версией итогового проекта. Новый notebook `book/02_dpo_course_design/final_project_workbook.ipynb` подключен в раздел курса ДПО после текстовой спецификации `final_project_model.md`. Сопроводительная карточка сохранена как `book/02_dpo_course_design/final_project_workbook_notes.md`.

Первая статья научно-публикационного контура обновлена до рабочей версии v0.4: публичный текст перенесен в `book/06_research_articles/article_01_platform_concept.md`, исходный редакционный пакет сохранен в `data/branches/06_research_articles/article_01_platform_concept_v0_3/`, а внешний научный слой зафиксирован в `article_01_platform_concept_external_sources_v0_4.yaml`.

Вторая статья научно-публикационного контура обновлена до рабочей версии v0.2: `book/06_research_articles/article_02_dpo_methodology.md`. Статья получила обобщённую рамку «Методология проектирования программ ДПО по ИИ-инструментам для преподавателей: компетенции, оценивание и цифровое сопровождение образовательного результата». Авторская программа на 72 часа описана как апробационная конфигурация универсализируемой модели, а не как узкий локальный отчёт. В v0.2 добавлен внешний обзор исследований по ДПО педагогов, цифровым компетенциям, ИИ-компетентности, оцениванию результатов и барьерам внедрения ИИ.

Третья статья научно-публикационного контура обновлена до рабочей версии v0.2: `book/06_research_articles/article_03_certification_model.md`. Статья описывает методико-техническую модель цифрового документа результата обучения, QR-проверку, аудит, хранение PDF и разграничение методического, технического и юридического статуса документа. В v0.2 добавлен внешний обзор по микроквалификациям, digital credentials, Open Badges, Verifiable Credentials, Europass Digital Credentials и сертификации компетенций педагогов.

Для статей 01-03 добавлен первый воспроизводимый визуальный слой: карта публикационного контура проекта, граф компетенций ПК-ИИ-1 — ПК-ИИ-10, жизненный цикл цифрового документа результата обучения и схема QR-проверки с минимизацией раскрытия данных. Диаграммы генерируются скриптом `scripts/generate_article_visuals.py` и подключены в соответствующие статьи как SVG-иллюстрации.

Карта публикационного контура дополнительно выровнена: колонки приведены к единой сетке, стрелки вынесены в отдельные строки основного потока и обратной связи, а нижний блок границы открытой публикации расширен так, чтобы текст не выходил за пределы рамки.

Визуальный слой продолжен: добавлены `module_map.svg` для статьи 02 и `platform_data_model.svg` для статьи 01. Карта модулей показывает 8 модулей, 72 часа и связь с компетенциями ПК-ИИ-1 — ПК-ИИ-10; модель данных показывает только публичный доменный уровень платформы без production-схемы, персональных данных и инфраструктурных деталей.

## Что собрано

Создан Jupyter Book-репозиторий для книги «Проектирование цифровой образовательной экосистемы факультета: методология, архитектура и реализация курса ДПО по ИИ-инструментам».

Подготовлены:

- корневые файлы Jupyter Book: `_config.yml`, `_toc.yml`, `index.md`, `requirements.txt`;
- авторская строка: Морозов Артём Михайлович, младший научный сотрудник, преподаватель курса «Введение в ИТ», кафедра «Бизнес-информатики», СПБГТИ(ТУ);
- публичные главы в `book/`;
- структурированные данные веток в `data/branches/`;
- изображения и диаграммы в `assets/`;
- скрипты проверки `scripts/validate_data.py` и `scripts/check_book.py`;
- скрипт генерации визуализаций `scripts/generate_article_visuals.py`;
- GitHub Actions workflow `.github/workflows/deploy-book.yml`;
- правила для будущих AI-агентов в `AGENTS.md`;
- README с командами локального запуска;
- библиографическая база `bibliography.bib`.
- редакционный архив статьи 01 v0.3 в `data/branches/06_research_articles/article_01_platform_concept_v0_3/`.
- редакционный архив статьи 02 v0.1 в `data/branches/06_research_articles/article_02_dpo_methodology_v0_1/`.
- редакционный архив статьи 03 v0.1-v0.2 в `data/branches/06_research_articles/article_03_certification_model_v0_1/`.

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
| 8. Итоговый проект | подключена как спецификация, приложение и notebook-глава | `book/02_dpo_course_design/final_project_model.md`, `book/02_dpo_course_design/final_project_workbook.ipynb` |
| 9. Право, этика, безопасность | подключена как главы стратегии | `book/03_ai_integration_strategy/legal_ethics_security.md` |
| 10. Сертификат или удостоверение | подключена как отдельная часть книги | `book/05_certification/` |
| 11. Платформенная интеграция курса | подключена как notebook-глава архитектуры | `book/01_platform_architecture/architecture_overview.ipynb` |
| Статья 01. Концепция платформы | подключена как публикационная редакция v0.4 | `book/06_research_articles/article_01_platform_concept.md` |
| Статья 02. Методология ДПО | подключена как публикационная редакция v0.2 | `book/06_research_articles/article_02_dpo_methodology.md` |
| Статья 03. Цифровой документ результата обучения | подключена как публикационная редакция v0.2 | `book/06_research_articles/article_03_certification_model.md` |

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

Для публичной версии добавлен раздел `book/05_certification/legal_status.md`. В нем зафиксирована проектная позиция: до организационного утверждения документ описывается как методико-техническая модель документа об обучении или цифрового документа результата обучения, а не как самостоятельный юридически утвержденный регламент.

## Визуальный слой статей 01-03

Добавлены SVG-диаграммы в `assets/diagrams/research_articles/`:

- `publication_contour_map.svg` — карта публикационного контура проекта для статьи 01;
- `competency_graph.svg` — граф компетентностной модели ПК-ИИ-1 — ПК-ИИ-10 для статьи 02;
- `module_map.svg` — карта модулей курса ДПО по ИИ-инструментам для статьи 02;
- `platform_data_model.svg` — публичная доменная модель данных платформы для статьи 01;
- `certificate_lifecycle.svg` — жизненный цикл цифрового документа результата обучения для статьи 03;
- `qr_verification_flow.svg` — схема QR-проверки и минимизации раскрытия данных для статьи 03.

Диаграммы подключены через MyST figure-блоки и используют проектные данные из `book/05_certification/data/competencies.yaml`, `book/05_certification/implementation_spec.yaml`, `data/branches/11_platform_course_integration/platform_course_integration.yaml` и публичного описания модели данных `book/01_platform_architecture/data_model.md`. Визуализации не меняют названия компетенций, не утверждают юридический статус документа и не раскрывают закрытые данные.

## Библиография и источники

В `bibliography.bib` добавлены 41 источниковая запись: 11 начальных нормативных, международных и технических источников, 11 внешних русскоязычных научных публикаций для статьи 01, 10 дополнительных источников для статьи 02 и 9 источников для статьи 03.

Начальная рамка включает:

- Федеральный закон № 273-ФЗ «Об образовании в Российской Федерации»;
- приказ Минобрнауки России от 24.03.2025 № 266 по ДПО;
- Федеральный закон № 152-ФЗ «О персональных данных»;
- Федеральный закон № 63-ФЗ «Об электронной подписи»;
- UNESCO Guidance for Generative AI in Education and Research;
- UNESCO AI Competency Framework for Teachers;
- OECD AI Principles;
- Указ Президента Российской Федерации от 10.10.2019 № 490 о развитии искусственного интеллекта и Указ Президента Российской Федерации от 15.02.2024 № 124 о внесении изменений;
- документация Jupyter Book по `_config.yml` и `_toc.yml`.

Внешняя научная база статьи 01 включает публикации по:

- цифровой трансформации высшего образования и восприятию изменений преподавателями;
- цифровой образовательной экосистеме и онлайн-образованию;
- повышению квалификации и цифровым компетенциям педагогов;
- генеративному ИИ в высшем образовании и преподавательской работе;
- учебной аналитике и цифровому следу.

Внешняя научная база статьи 02 включает публикации и рамки по:

- международным компетентностным рамкам UNESCO AI Competency Framework for Teachers и DigCompEdu;
- повышению квалификации и развитию цифровых компетенций преподавателей;
- оцениванию результатов и эффективности программ ДПО педагогов;
- отношению университетских преподавателей к ИИ, практикам применения ИИ и барьерам внедрения ИИ в ДПО.

Внешняя научная и стандартизационная база статьи 03 включает источники по:

- микроквалификациям и коротким образовательным результатам в рамках UNESCO, OECD и Совета Европейского союза;
- цифровым credentials, проверяемым утверждениям, DID, Open Badges и Europass Digital Credentials;
- гибкой профессиональной подготовке и сертификации компетенций педагогов в российском научно-методическом контексте.

Раздел `book/07_appendices/bibliography.md` теперь выводит полный список источников через Jupyter Book bibliography directive.

## Границы открытой публикации

Добавлен раздел `book/07_appendices/publication_scope.md`, где материалы разделены на три группы:

- можно публиковать открыто;
- можно публиковать после редактирования и обезличивания;
- не следует публиковать без отдельного разрешения или вообще не следует раскрывать.

## Ноутбуки, которые исполняются при сборке

При `jupyter-book build .` выполнены и закэшированы:

- `book/01_platform_architecture/architecture_overview.ipynb`;
- `book/02_dpo_course_design/course_concept.ipynb`;
- `book/02_dpo_course_design/competency_model.ipynb`;
- `book/02_dpo_course_design/curriculum_plan.ipynb`;
- `book/02_dpo_course_design/final_project_workbook.ipynb`;
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

- `scripts/validate_data.py`: OK, проверено 70 JSON и 87 YAML.
- `scripts/check_book.py`: OK, проверено 41 TOC-цель.
- `jupyter-book build .`: OK, HTML создан в `_build/html`, библиография распознана как 41 запись.

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

Репозиторий проекта: <https://github.com/vnuchenic777-bot/fem-ai-education-book>.

Публичная HTML-версия книги: <https://vnuchenic777-bot.github.io/fem-ai-education-book/>.

Чтобы включить публикацию:

1. Отправить ветку `main` в GitHub.
2. В GitHub открыть **Settings → Pages**.
3. В **Build and deployment → Source** выбрать **GitHub Actions**.
4. Запустить workflow push-ем или вручную через `workflow_dispatch`.

GitHub Pages включен в режиме `workflow`, первый deploy завершился успешно.

## Что требует доработки

- Уточнить библиографию статьи 01 под требования выбранного журнала и при необходимости проверить карточки eLIBRARY/EDN для внешних источников.
- Уточнить библиографию статьи 02 под требования выбранного журнала и проверить EDN/eLIBRARY-карточки для новых внешних источников.
- Заполнить черновые разделы: PWA-стратегия, роли, хранение, backend-основание и научные статьи.
- Согласовать с образовательной организацией юридический статус документа об обучении, порядок подписи, регистрации, хранения, отзыва и публичной проверки.
- Принять организационное решение о том, какие внутренние материалы СПБГТИ(ТУ) могут быть открыто опубликованы.
- При необходимости дополнить визуальный слой отдельными диаграммами для фонда оценочных средств и итогового проекта.
- Перед журнальной подачей расширить библиографический поиск статей 01-03 по требованиям выбранного издания, включая eLIBRARY/EDN и профильные международные базы.

## Рекомендуемая следующая задача

Продолжить проработку серии статей: перейти к сквозной редактуре единого академического стиля всей серии или дополнить визуальный слой фонда оценочных средств и итогового проекта.
