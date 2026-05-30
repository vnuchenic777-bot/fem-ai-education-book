# Цифровая образовательная экосистема ФЭМ

Jupyter Book-репозиторий исследовательско-методической книги:

**«Проектирование цифровой образовательной экосистемы факультета: методология, архитектура и реализация курса ДПО по ИИ-инструментам»**.

Автор: **Морозов Артём Михайлович**, младший научный сотрудник, преподаватель курса «Введение в ИТ», кафедра «Бизнес-информатики», СПБГТИ(ТУ).

Книга собирает Markdown-главы, Jupyter Notebook, YAML/JSON-данные, диаграммы и инженерные спецификации проекта. HTML-версия генерируется автоматически через Jupyter Book; Word, PDF и ручной HTML не являются основным результатом публикации.

## Структура

- `book/` — публичные главы книги.
- `data/branches/` — структурированные данные и исходные материалы веток.
- `assets/` — изображения, диаграммы и логотипы.
- `scripts/` — проверки данных и структуры книги.
- `.github/workflows/deploy-book.yml` — публикация на GitHub Pages.

## Локальный запуск

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

После запуска сервера книга будет доступна по адресу <http://localhost:8000>.

## Публикация на GitHub Pages

1. Создать репозиторий на GitHub.
2. Заменить `repository.url` в `_config.yml` на фактический URL репозитория.
3. Отправить ветку `main` на GitHub.
4. В настройках репозитория открыть **Settings → Pages**.
5. В поле **Build and deployment → Source** выбрать **GitHub Actions**.
6. Дождаться выполнения workflow `Deploy Jupyter Book to GitHub Pages`.

## Важные ограничения

- Не создавать Word/PDF как основной результат публикации.
- Не писать HTML вручную.
- Не удалять `.ipynb`, `.yaml`, `.yml`, `.json`.
- Не менять компетенции ПК-ИИ-1 — ПК-ИИ-10.
- Не раскрывать ключи доступа, закрытые адреса сервисов, персональные данные слушателей и внутренние документы без разрешения.
- Не удалять предупреждения о необходимости юридического согласования с образовательной организацией.
