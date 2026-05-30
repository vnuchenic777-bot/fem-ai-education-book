# Карта ячеек ноутбука `rpm_dpo_ai_72h_v0_1.ipynb`

## Ячейка 1: markdown

**Назначение:** Проект РПМ v0.1 программы повышения квалификации

**Markdown-содержимое:**

```markdown
# Проект РПМ v0.1 программы повышения квалификации

**Тема главы:** проект рабочей программы модуля / программы повышения квалификации «ИИ-инструменты в преподавательской, научной и повседневной работе: от понимания принципов до практического применения».

**Объем программы:** 72 академических часа.  
**Формат главы:** исследовательский Jupyter Notebook для включения в Jupyter Book.  
**Граница главы:** рассматривается только ветка №1 — проект РПМ v0.1. Вопросы разработки всей платформы, коммерческой модели и последующих веток затрагиваются только как контекст, необходимый для требований к РПМ и реализации данного этапа.

Глава предназначена для воспроизводимого анализа структуры РПМ: данные хранятся отдельно в `data/rpm_dpo_ai_72h_v0_1.yaml` и `data/rpm_dpo_ai_72h_v0_1.json`, а таблицы, графы и диаграммы строятся кодом.

```

## Ячейка 2: markdown

**Назначение:** Карта ячеек ноутбука

**Markdown-содержимое:**

```markdown
## Карта ячеек ноутбука

| № | Тип | Назначение | Ожидаемый результат |
|---:|---|---|---|
| 1 | Markdown | Название и границы главы | Читатель понимает тему и ограничения главы |
| 2 | Markdown | Карта ячеек | Список markdown- и code-ячеек с ожидаемым результатом |
| 3 | Code | Импорт библиотек, поиск корня проекта, загрузка YAML/JSON | Проверка наличия данных и вывод основных ключей |
| 4 | Markdown | Постановка задачи | Описание методической задачи РПМ v0.1 |
| 5 | Code | Нормализация данных программы, модулей и компетенций | Таблицы `modules_df`, `competencies_df`, `tasks_df` |
| 6 | Markdown | Описание структуры данных | Интерпретация источника данных и ограничений |
| 7 | Code | Паспорт программы и задачи | Таблица паспорта программы и перечень задач |
| 8 | Markdown | Компетентностная логика | Объяснение роли ПК-ИИ-1 — ПК-ИИ-10 |
| 9 | Code | Матрица компетенций и модулей | Таблица бинарной связи компетенций с модулями |
| 10 | Code | Тепловая карта формирования компетенций | Диаграмма распределения компетенций по модулям |
| 11 | Markdown | Учебный план | Объяснение распределения 72 часов |
| 12 | Code | Таблица модулей и диаграмма часов | Таблица модулей и столбчатая диаграмма |
| 13 | Code | Диаграмма состава часов по видам деятельности | Состав часов: видео/конспекты, практика, самостоятельная работа, контроль |
| 14 | Markdown | Процессная модель РПМ | Интерпретация процесса разработки РПМ |
| 15 | Code | Граф процесса разработки РПМ | Направленный граф этапов от исходных документов до реализации |
| 16 | Code | Граф связей «модули — компетенции — доказательства» | Сетевой граф связей модулей, компетенций, артефактов и тестов |
| 17 | Markdown | Оценивание и итоговая аттестация | Объяснение двухчастного доказательства освоения компетенции |
| 18 | Code | Модель статуса освоения компетенции | Демонстрация алгоритма определения статуса по артефакту и тесту |
| 19 | Code | Пример данных слушателей и итоговых статусов | Синтетическая таблица освоения компетенций и итогов курса |
| 20 | Markdown | ТЗ на реализацию этапа | Логика перевода РПМ в исполнимые задачи для разработки |
| 21 | Code | Таблицы deliverables, требований и приемки этапа | Структурированные таблицы ТЗ реализации |
| 22 | Code | Диаграмма жизненного цикла реализации этапа | Направленная схема жизненного цикла текущего этапа |
| 23 | Markdown | Риски и открытые вопросы | Интерпретация организационных и методических рисков |
| 24 | Code | Таблицы рисков и открытых вопросов | Две таблицы для дальнейшего методического согласования |
| 25 | Markdown | Научно-публикационный потенциал | Как глава может стать основой статьи, доклада или выпуска журнала |
| 26 | Code | Экспорт аналитических таблиц в JSON/YAML | Воспроизводимый экспорт производных таблиц в `data/derived/` |
| 27 | Markdown | Итоговые выводы главы | Сжатое резюме результатов ветки №1 |

```

## Ячейка 3: code

**Назначение:** from pathlib import Path

**Полный код:**

```python
from pathlib import Path
from dataclasses import dataclass
import json
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


def resolve_project_root() -> Path:
    """Find a project root that contains the data directory used by this notebook."""
    current = Path.cwd().resolve()
    candidates = [current, *current.parents]
    for candidate in candidates:
        if (candidate / "data" / "rpm_dpo_ai_72h_v0_1.yaml").exists():
            return candidate
    raise FileNotFoundError("Cannot find data/rpm_dpo_ai_72h_v0_1.yaml from current working directory.")


PROJECT_ROOT = resolve_project_root()
DATA_DIR = PROJECT_ROOT / "data"
YAML_PATH = DATA_DIR / "rpm_dpo_ai_72h_v0_1.yaml"
JSON_PATH = DATA_DIR / "rpm_dpo_ai_72h_v0_1.json"

with YAML_PATH.open("r", encoding="utf-8") as f:
    data_from_yaml = yaml.safe_load(f)

with JSON_PATH.open("r", encoding="utf-8") as f:
    data_from_json = json.load(f)

assert data_from_yaml == data_from_json, "YAML and JSON versions must contain the same structured data."
project_data = data_from_yaml

print("Project root:", PROJECT_ROOT)
print("Loaded data keys:")
for key in project_data.keys():
    print("-", key)

```

## Ячейка 4: markdown

**Назначение:** Постановка задачи главы

**Markdown-содержимое:**

```markdown
## Постановка задачи главы

Задача главы — представить проект РПМ v0.1 как воспроизводимую исследовательско-методическую модель. Обычный текст РПМ фиксирует содержание программы, но плохо показывает внутреннюю связность: как цель связана с компетенциями, как компетенции распределены по модулям, какие артефакты подтверждают освоение, какие требования передаются в этап реализации.

В этой главе РПМ рассматривается как структурированный объект. Его основные элементы представлены в данных, а затем проверяются и визуализируются кодом:

- паспорт программы;
- задачи и результаты обучения;
- 10 профессиональных компетенций ПК-ИИ-1 — ПК-ИИ-10;
- 8 модулей общей трудоемкостью 72 часа;
- артефакты и тесты как доказательства освоения;
- итоговый проект;
- требования к цифровой среде;
- техническое задание на реализацию этапа;
- риски и открытые вопросы для образовательной организации.

```

## Ячейка 5: code

**Назначение:** @dataclass

**Полный код:**

```python
@dataclass
class ProgramSummary:
    title: str
    hours_total: int
    format: str
    target_audience: str
    final_assessment: str


program = project_data["program"]
program_summary = ProgramSummary(
    title=program["title"],
    hours_total=program["hours_total"],
    format=program["format"],
    target_audience=program["target_audience"],
    final_assessment=program["final_assessment"],
)

modules_df = pd.DataFrame([
    {
        "module": m["module_number"],
        "title": m["title"],
        "hours_total": m["hours_total"],
        "video_and_notes": m["hours_breakdown"].get("video_and_notes", 0),
        "practice": m["hours_breakdown"].get("practice", 0),
        "independent_work": m["hours_breakdown"].get("independent_work", 0),
        "control": m["hours_breakdown"].get("control", 0),
        "competencies": ", ".join(m["competencies"]),
        "artifact": m["artifact"],
    }
    for m in project_data["modules"]
])

competencies_df = pd.DataFrame([
    {
        "code": c["code"],
        "title": c["title"],
        "formed_in_modules": ", ".join(str(x) for x in c["formed_in_modules"]),
        "artifact": c["artifact"],
        "test": c["test"],
    }
    for c in project_data["competencies"]
])

tasks_df = pd.DataFrame({"task": project_data["tasks"]})

print(program_summary)
print("\nModules:", len(modules_df), "Competencies:", len(competencies_df), "Tasks:", len(tasks_df))
modules_df

```

## Ячейка 6: markdown

**Назначение:** Описание структуры данных

**Markdown-содержимое:**

```markdown
## Описание структуры данных

Источник данных главы — структурированное представление РПМ v0.1. Оно сохранено в двух эквивалентных форматах:

- `data/rpm_dpo_ai_72h_v0_1.yaml` — основной человекочитаемый формат;
- `data/rpm_dpo_ai_72h_v0_1.json` — строгий машинный формат.

Дублирование форматов позволяет использовать данные как в исследовательском ноутбуке, так и в инженерных средах. Ноутбук проверяет, что YAML и JSON совпадают, поэтому таблицы и графы строятся из одной и той же модели.

Юридические и нормативные формулировки не задаются как окончательные. Если требуется утверждение порядка выдачи документа, подписи, регистрации или хранения персональных данных, это фиксируется как вопрос к образовательной организации.

```

## Ячейка 7: code

**Назначение:** passport_rows = [

**Полный код:**

```python
passport_rows = [
    ("Наименование программы", project_data["program"]["title"]),
    ("Вид программы", project_data["program"]["type"]),
    ("Объем", f"{project_data['program']['hours_total']} академических часа"),
    ("Формат", project_data["program"]["format"]),
    ("Целевая аудитория", project_data["program"]["target_audience"]),
    ("Итоговая аттестация", project_data["program"]["final_assessment"]),
    ("Примечание к документу", project_data["program"]["certificate_note"]),
]
passport_df = pd.DataFrame(passport_rows, columns=["position", "content"])

print("Паспорт программы")
print(passport_df.to_string(index=False))
print("\nЗадачи программы")
print(tasks_df.to_string(index=False))

```

## Ячейка 8: markdown

**Назначение:** Компетентностная логика РПМ

**Markdown-содержимое:**

```markdown
## Компетентностная логика РПМ

Компетенции ПК-ИИ-1 — ПК-ИИ-10 задают проверяемую структуру программы. Они не должны оставаться декларацией: каждая компетенция связывается с модулями, артефактом и тестом или практической проверкой.

Для РПМ это означает следующее:

1. компетенция должна быть сформулирована как профессиональное действие преподавателя;
2. модули должны показывать, где компетенция формируется;
3. артефакт должен подтверждать способность создать продукт;
4. тест или практическая проверка должны подтверждать понимание принципов и ограничений;
5. итоговый проект должен объединять компетенции в применимую модель обновления собственной дисциплины.

```

## Ячейка 9: code

**Назначение:** module_numbers = sorted(modules_df["module"].tolist())

**Полный код:**

```python
module_numbers = sorted(modules_df["module"].tolist())
competency_module_matrix = pd.DataFrame(0, index=competencies_df["code"], columns=[f"M{n}" for n in module_numbers])

for c in project_data["competencies"]:
    for module_number in c["formed_in_modules"]:
        competency_module_matrix.loc[c["code"], f"M{module_number}"] = 1

competency_module_matrix["total_modules"] = competency_module_matrix.sum(axis=1)
print("Матрица формирования компетенций по модулям")
competency_module_matrix

```

## Ячейка 10: code

**Назначение:** fig, ax = plt.subplots(figsize=(10, 5))

**Полный код:**

```python
fig, ax = plt.subplots(figsize=(10, 5))
visual_matrix = competency_module_matrix.drop(columns=["total_modules"])
image = ax.imshow(visual_matrix.values, aspect="auto")
ax.set_xticks(range(len(visual_matrix.columns)))
ax.set_xticklabels(visual_matrix.columns)
ax.set_yticks(range(len(visual_matrix.index)))
ax.set_yticklabels(visual_matrix.index)
ax.set_title("Формирование компетенций по модулям")
ax.set_xlabel("Модули")
ax.set_ylabel("Компетенции")
for row in range(visual_matrix.shape[0]):
    for col in range(visual_matrix.shape[1]):
        ax.text(col, row, str(visual_matrix.iloc[row, col]), ha="center", va="center")
plt.tight_layout()
plt.show()

```

## Ячейка 11: markdown

**Назначение:** Учебный план и распределение часов

**Markdown-содержимое:**

```markdown
## Учебный план и распределение часов

Программа имеет фиксированную трудоемкость 72 академических часа. Внутри каждого модуля часы распределяются между видеолекциями и конспектами, практической работой, самостоятельной работой и контролем.

Такое представление важно для проектирования курса в цифровой среде: каждый вид деятельности должен быть связан с конкретным элементом курса — видеоматериалом, конспектом, заданием, тестом, артефактом или итоговой проверкой.

```

## Ячейка 12: code

**Назначение:** module_hours_df = modules_df[["module", "title", "hours_total", "video_and_notes", "practi

**Полный код:**

```python
module_hours_df = modules_df[["module", "title", "hours_total", "video_and_notes", "practice", "independent_work", "control", "competencies"]]
print("Сумма часов:", module_hours_df["hours_total"].sum())
module_hours_df

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(module_hours_df["module"], module_hours_df["hours_total"])
ax.set_title("Распределение часов по модулям")
ax.set_xlabel("Номер модуля")
ax.set_ylabel("Академические часы")
ax.set_xticks(module_hours_df["module"])
plt.tight_layout()
plt.show()

```

## Ячейка 13: code

**Назначение:** breakdown_columns = ["video_and_notes", "practice", "independent_work", "control"]

**Полный код:**

```python
breakdown_columns = ["video_and_notes", "practice", "independent_work", "control"]
breakdown_df = module_hours_df.set_index("module")[breakdown_columns]
print("Проверка: сумма состава часов по каждому модулю равна общей трудоемкости модуля")
print(breakdown_df.sum(axis=1).to_string())

ax = breakdown_df.plot(kind="bar", stacked=True, figsize=(10, 5))
ax.set_title("Состав часов по видам учебной деятельности")
ax.set_xlabel("Номер модуля")
ax.set_ylabel("Академические часы")
plt.tight_layout()
plt.show()

```

## Ячейка 14: markdown

**Назначение:** Процессная модель разработки РПМ

**Markdown-содержимое:**

```markdown
## Процессная модель разработки РПМ

Проект РПМ v0.1 является не только текстовым документом, но и входом в дальнейшую реализацию этапа. В рамках этой главы процесс рассматривается как последовательность преобразований:

1. исходные решения и стратегия;
2. проект РПМ;
3. компетентностная модель;
4. учебный и учебно-тематический план;
5. фонд оценочных средств;
6. итоговый проект;
7. требования к цифровой среде;
8. техническое задание на реализацию этапа.

Эта схема не расширяет главу на весь проект, а показывает жизненный цикл именно ветки №1.

```

## Ячейка 15: code

**Назначение:** process_edges = [

**Полный код:**

```python
process_edges = [
    ("Исходные решения", "Проект РПМ v0.1"),
    ("Стратегия интеграции ИИ", "Проект РПМ v0.1"),
    ("Проект РПМ v0.1", "Компетентностная модель"),
    ("Проект РПМ v0.1", "Учебный план"),
    ("Проект РПМ v0.1", "ФОС"),
    ("Компетентностная модель", "Итоговый проект"),
    ("Учебный план", "Карта реализации курса"),
    ("ФОС", "Критерии приемки"),
    ("Итоговый проект", "Критерии приемки"),
    ("Карта реализации курса", "ТЗ этапа реализации"),
    ("Критерии приемки", "ТЗ этапа реализации"),
]
process_graph = nx.DiGraph()
process_graph.add_edges_from(process_edges)

fig, ax = plt.subplots(figsize=(12, 7))
pos = nx.spring_layout(process_graph, seed=7)
nx.draw_networkx(process_graph, pos=pos, with_labels=True, node_size=2500, font_size=9, arrows=True, ax=ax)
ax.set_title("Процессная модель ветки №1: от исходных решений к ТЗ реализации")
ax.axis("off")
plt.tight_layout()
plt.show()

```

## Ячейка 16: code

**Назначение:** relation_graph = nx.DiGraph()

**Полный код:**

```python
relation_graph = nx.DiGraph()
relation_graph.add_node("РПМ v0.1")

for m in project_data["modules"]:
    module_node = f"M{m['module_number']}: {m['title']}"
    relation_graph.add_edge("РПМ v0.1", module_node)
    for comp_code in m["competencies"]:
        relation_graph.add_edge(module_node, comp_code)

for c in project_data["competencies"]:
    relation_graph.add_edge(c["code"], f"Артефакт: {c['code']}")
    relation_graph.add_edge(c["code"], f"Проверка: {c['code']}")

fig, ax = plt.subplots(figsize=(16, 10))
pos = nx.spring_layout(relation_graph, seed=11, k=0.6)
nx.draw_networkx(relation_graph, pos=pos, with_labels=True, node_size=900, font_size=7, arrows=True, ax=ax)
ax.set_title("Связи РПМ: модули, компетенции, артефакты и проверки")
ax.axis("off")
plt.tight_layout()
plt.show()

```

## Ячейка 17: markdown

**Назначение:** Оценивание и итоговая аттестация

**Markdown-содержимое:**

```markdown
## Оценивание и итоговая аттестация

Ключевое правило РПМ v0.1: компетенция подтверждается двумя элементами — артефактом и тестом или практической проверкой. Это защищает программу от формального прохождения: слушатель должен не только ответить на вопросы, но и создать проверяемый продукт.

Для итоговой мета-компетенции ПК-ИИ-10 используется итоговый проект. Он связывает содержание курса с реальной дисциплиной преподавателя: терминология, задания с обязательным использованием ИИ, план занятия, предложение по обновлению РПМ, критерии оценивания, риски и рефлексия.

```

## Ячейка 18: code

**Назначение:** def evaluate_competency_status(artifact_accepted: bool, test_passed: bool) -> str:

**Полный код:**

```python
def evaluate_competency_status(artifact_accepted: bool, test_passed: bool) -> str:
    """Return a competency status according to the two-part evidence rule."""
    if artifact_accepted and test_passed:
        return "освоена"
    if artifact_accepted or test_passed:
        return "частично освоена"
    return "не освоена"

status_examples = pd.DataFrame([
    {"artifact_accepted": True, "test_passed": True},
    {"artifact_accepted": True, "test_passed": False},
    {"artifact_accepted": False, "test_passed": True},
    {"artifact_accepted": False, "test_passed": False},
])
status_examples["competency_status"] = status_examples.apply(
    lambda row: evaluate_competency_status(row["artifact_accepted"], row["test_passed"]),
    axis=1,
)
status_examples

```

## Ячейка 19: code

**Назначение:** Synthetic demonstration data: no personal data, only reproducible examples.

**Полный код:**

```python
# Synthetic demonstration data: no personal data, only reproducible examples.
learners = ["Слушатель A", "Слушатель B", "Слушатель C"]
competency_codes = [c["code"] for c in project_data["competencies"]]

records = []
for learner_index, learner in enumerate(learners):
    for comp_index, code_value in enumerate(competency_codes):
        artifact_accepted = (comp_index + learner_index) % 4 != 0
        test_passed = (comp_index + learner_index) % 5 != 0
        records.append({
            "learner": learner,
            "competency": code_value,
            "artifact_accepted": artifact_accepted,
            "test_passed": test_passed,
            "status": evaluate_competency_status(artifact_accepted, test_passed),
        })

evidence_df = pd.DataFrame(records)
summary_df = evidence_df.pivot_table(index="learner", columns="status", values="competency", aggfunc="count", fill_value=0)
summary_df["total_competencies"] = len(competency_codes)
summary_df["course_completed"] = summary_df.get("освоена", 0) == len(competency_codes)

print("Пример статусов освоения компетенций")
print(summary_df.to_string())
evidence_df.head(12)

```

## Ячейка 20: markdown

**Назначение:** Техническое задание на реализацию этапа

**Markdown-содержимое:**

```markdown
## Техническое задание на реализацию этапа

В рамках текущей ветки ТЗ не охватывает всю платформу. Оно описывает реализацию именно методического этапа РПМ v0.1 в цифровой среде:

- создать шаблон курса;
- внести 8 модулей;
- связать модули с компетенциями;
- создать структуру артефактов и тестов;
- зафиксировать итоговый проект;
- подготовить требования к оцениванию и документу об обучении;
- сохранить открытые вопросы для согласования с образовательной организацией.

Такое ТЗ переводит методический документ в набор проверяемых задач для реализации.

```

## Ячейка 21: code

**Назначение:** ta = project_data["implementation_technical_assignment"]

**Полный код:**

```python
ta = project_data["implementation_technical_assignment"]

deliverables_df = pd.DataFrame({"deliverable": ta["deliverables"]})
functional_requirements_df = pd.DataFrame({"functional_requirement": ta["functional_requirements"]})
non_functional_requirements_df = pd.DataFrame({"non_functional_requirement": ta["non_functional_requirements"]})
acceptance_criteria_df = pd.DataFrame({"acceptance_criterion": ta["acceptance_criteria"]})
platform_entities_df = pd.DataFrame({"platform_entity": ta["platform_entities_to_create"]})

print("Stage:", ta["stage_code"], "—", ta["stage_title"])
print("Objective:", ta["objective"])
print("\nDeliverables")
print(deliverables_df.to_string(index=False))
print("\nAcceptance criteria")
print(acceptance_criteria_df.to_string(index=False))

```

## Ячейка 22: code

**Назначение:** lifecycle_edges = [

**Полный код:**

```python
lifecycle_edges = [
    ("Методические данные", "Шаблон курса"),
    ("Шаблон курса", "Модули"),
    ("Модули", "Уроки и материалы"),
    ("Модули", "Компетенции"),
    ("Компетенции", "Артефакты"),
    ("Компетенции", "Тесты"),
    ("Артефакты", "Проверка"),
    ("Тесты", "Проверка"),
    ("Проверка", "Итоговый статус"),
    ("Итоговый проект", "Итоговый статус"),
    ("Итоговый статус", "Документ об обучении"),
]
lifecycle_graph = nx.DiGraph()
lifecycle_graph.add_edges_from(lifecycle_edges)

fig, ax = plt.subplots(figsize=(13, 7))
pos = nx.spring_layout(lifecycle_graph, seed=21)
nx.draw_networkx(lifecycle_graph, pos=pos, with_labels=True, node_size=2400, font_size=9, arrows=True, ax=ax)
ax.set_title("Жизненный цикл реализации РПМ v0.1 в цифровой среде")
ax.axis("off")
plt.tight_layout()
plt.show()

```

## Ячейка 23: markdown

**Назначение:** Риски и открытые вопросы

**Markdown-содержимое:**

```markdown
## Риски и открытые вопросы

Риски в этой главе рассматриваются как часть методического управления качеством. Они не являются препятствием к разработке РПМ, но показывают, какие условия должны быть согласованы до официального запуска программы.

Открытые вопросы отделены от утвержденных положений. Это важно для корректной академической и организационной работы: ноутбук не выдумывает нормативные требования, а фиксирует места, где требуется решение образовательной организации.

```

## Ячейка 24: code

**Назначение:** risks_df = pd.DataFrame(project_data["risks"])

**Полный код:**

```python
risks_df = pd.DataFrame(project_data["risks"])
questions_df = pd.DataFrame({"open_question": project_data["open_questions_for_organization"]})

print("Риски реализации")
print(risks_df.to_string(index=False))
print("\nОткрытые вопросы")
print(questions_df.to_string(index=False))

```

## Ячейка 25: markdown

**Назначение:** Научно-публикационный потенциал

**Markdown-содержимое:**

```markdown
## Научно-публикационный потенциал

Эта глава может стать основой для нескольких типов публикаций.

### 1. Методическая статья

Возможная тема: **«Компетентностная модель программы повышения квалификации преподавателей по применению ИИ-инструментов»**. Материалом для статьи выступают структура РПМ, матрица компетенций, модель артефактов и двухчастное подтверждение освоения компетенций.

### 2. Доклад на методической конференции

Возможная тема: **«Проектирование заданий с обязательным использованием ИИ как инструмент обновления рабочих программ дисциплин»**. В докладе можно использовать граф связей модулей, компетенций, артефактов и итогового проекта.

### 3. Глава исследовательского журнала проекта

Глава может быть опубликована как часть журнала разработки образовательной платформы и курса ДПО. Ее ценность состоит в том, что она показывает не только итоговую РПМ, но и способ ее инженерно-методического представления: данные отдельно, визуализации кодом, проверяемые связи между элементами.

### 4. Основа для эмпирического исследования

После пилотного запуска к этой структуре можно добавить реальные обезличенные данные прохождения: статусы артефактов, результаты тестов, динамику доработок, типичные ошибки слушателей. Тогда глава может быть расширена до исследования эффективности программы.

```

## Ячейка 26: code

**Назначение:** DERIVED_DIR = DATA_DIR / "derived"

**Полный код:**

```python
DERIVED_DIR = DATA_DIR / "derived"
DERIVED_DIR.mkdir(exist_ok=True)

derived_tables = {
    "modules": modules_df.to_dict(orient="records"),
    "competencies": competencies_df.to_dict(orient="records"),
    "competency_module_matrix": competency_module_matrix.reset_index(names="competency").to_dict(orient="records"),
    "module_hours": module_hours_df.to_dict(orient="records"),
    "risks": risks_df.to_dict(orient="records"),
    "open_questions": questions_df.to_dict(orient="records"),
    "acceptance_criteria": acceptance_criteria_df.to_dict(orient="records"),
}

json_export_path = DERIVED_DIR / "rpm_v0_1_derived_tables.json"
yaml_export_path = DERIVED_DIR / "rpm_v0_1_derived_tables.yaml"

with json_export_path.open("w", encoding="utf-8") as f:
    json.dump(derived_tables, f, ensure_ascii=False, indent=2)

with yaml_export_path.open("w", encoding="utf-8") as f:
    yaml.safe_dump(derived_tables, f, allow_unicode=True, sort_keys=False)

print("Exported:")
print("-", json_export_path.relative_to(PROJECT_ROOT))
print("-", yaml_export_path.relative_to(PROJECT_ROOT))

```

## Ячейка 27: markdown

**Назначение:** Итоговые выводы главы

**Markdown-содержимое:**

```markdown
## Итоговые выводы главы

1. Проект РПМ v0.1 представлен как структурированная методическая модель, а не только как текстовый документ.
2. Объем программы составляет 72 академических часа и распределен по 8 модулям.
3. Компетентностная модель включает 10 профессиональных компетенций ПК-ИИ-1 — ПК-ИИ-10.
4. Каждая компетенция подтверждается двумя элементами: артефактом и тестом или практической проверкой.
5. Итоговый проект связывает курс с реальной дисциплиной преподавателя и подготовкой предложений по обновлению РПМ.
6. ТЗ на реализацию этапа переводит методическую структуру в проверяемые задачи для цифровой среды.
7. Все юридически значимые формулировки, связанные с документом об обучении, подписью, регистрацией и хранением данных, требуют согласования с образовательной организацией.

```
