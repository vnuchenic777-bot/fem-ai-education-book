# Полный код code-ячеек ноутбука 11_platform_course_integration.ipynb
# Этот файл сгенерирован для удобной проверки и переноса кода.

# %% [1] Импорт библиотек и настройка путей
# Ожидаемый результат: Печатает путь к каталогу data и подтверждает наличие JSON/YAML файлов.
from pathlib import Path
from dataclasses import dataclass
import json
import yaml

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Jupyter Book обычно выполняет ноутбук из каталога главы, но для
# переносимости проверяем несколько возможных расположений данных.
candidate_data_dirs = [
    Path.cwd() / "data",
    Path.cwd() / "chapter_11_platform_course_integration" / "data",
    Path.cwd() / "chapters" / "11_platform_course_integration" / "data",
]

DATA_DIR = next(
    (path for path in candidate_data_dirs if (path / "platform_course_integration.json").exists()),
    candidate_data_dirs[0],
)
BASE_DIR = DATA_DIR.parent

json_path = DATA_DIR / "platform_course_integration.json"
yaml_path = DATA_DIR / "platform_course_integration.yaml"

print("Каталог данных:", DATA_DIR)
print("JSON найден:", json_path.exists())
print("YAML найден:", yaml_path.exists())

# %% [2] Загрузка JSON и YAML модели
# Ожидаемый результат: Загружает JSON/YAML, проверяет согласованность ключевых показателей и печатает сводку.
with json_path.open("r", encoding="utf-8") as f:
    data_json = json.load(f)

with yaml_path.open("r", encoding="utf-8") as f:
    data_yaml = yaml.safe_load(f)

assert data_json["course_template"]["estimated_hours"] == data_yaml["course_template"]["estimated_hours"]
assert len(data_json["modules"]) == len(data_yaml["modules"])
assert len(data_json["lessons"]) == len(data_yaml["lessons"])

print("Название главы:", data_json["chapter_title"])
print("Часы:", data_json["course_template"]["estimated_hours"])
print("Модулей:", len(data_json["modules"]))
print("Уроков:", len(data_json["lessons"]))
print("Оценочных элементов:", len(data_json["assessments"]))
print("Компетенций:", len(data_json["competencies"]))

# %% [3] Создание табличных представлений из структурированных данных
# Ожидаемый результат: Формирует DataFrame по модулям, урокам, оценочным элементам, компетенциям и задачам. На экране отображается таблица модулей.
modules_df = pd.DataFrame(data_json["modules"])
lessons_df = pd.DataFrame(data_json["lessons"])
assessments_df = pd.DataFrame(data_json["assessments"])
competencies_df = pd.DataFrame(data_json["competencies"])
tasks_df = pd.DataFrame(data_json["implementation_tasks"])

# Для удобства анализа преобразуем списки компетенций в строку.
for df_name, df in [("modules", modules_df), ("assessments", assessments_df)]:
    if "competencies" in df.columns:
        df["competencies_text"] = df["competencies"].apply(lambda x: "; ".join(x) if isinstance(x, list) else str(x))

modules_df

# %% [4] Сводные показатели курса
# Ожидаемый результат: Показывает компактную сводку масштаба интеграции: часы, модули, уроки, оценочные элементы, компетенции и задачи.
summary = {
    "Показатель": [
        "Академические часы",
        "Модули",
        "Уроки",
        "Оценочные элементы",
        "Компетенции",
        "Задачи реализации"
    ],
    "Значение": [
        data_json["course_template"]["estimated_hours"],
        len(modules_df),
        len(lessons_df),
        len(assessments_df),
        len(competencies_df),
        len(tasks_df)
    ]
}
summary_df = pd.DataFrame(summary)
summary_df

# %% [5] Распределение часов по модулям
# Ожидаемый результат: Строит столбчатую диаграмму часов по модулям и показывает таблицу с количеством уроков/оценочных элементов.
hours_df = modules_df[["module_id", "order_index", "title", "estimated_hours", "lessons_count", "assessments_count"]].copy()
hours_df = hours_df.sort_values("order_index")

ax = hours_df.plot(kind="bar", x="module_id", y="estimated_hours", legend=False, figsize=(10, 4))
ax.set_title("Распределение 72 академических часов по модулям")
ax.set_xlabel("Модуль")
ax.set_ylabel("Часы")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

hours_df

# %% [6] Граф предметных связей CourseTemplate
# Ожидаемый результат: Строит направленный граф основных сущностей и их связей.
G = nx.DiGraph()

nodes = [
    "Organization", "CourseTemplate", "CourseModule", "Lesson", "CourseResource",
    "AssessmentItem", "QuizQuestion", "GradeScheme", "CourseRun", "Cohort",
    "Enrollment", "LessonProgress", "ModuleProgress", "AssignmentSubmission",
    "SubmissionAttempt", "AssignmentReview", "Grade", "IssuedCertificate"
]
G.add_nodes_from(nodes)
G.add_edges_from([
    ("Organization", "CourseTemplate"),
    ("CourseTemplate", "CourseModule"),
    ("CourseModule", "Lesson"),
    ("Lesson", "CourseResource"),
    ("CourseTemplate", "AssessmentItem"),
    ("AssessmentItem", "QuizQuestion"),
    ("AssessmentItem", "GradeScheme"),
    ("CourseTemplate", "CourseRun"),
    ("Cohort", "CourseRun"),
    ("CourseRun", "Enrollment"),
    ("Enrollment", "LessonProgress"),
    ("Enrollment", "ModuleProgress"),
    ("Enrollment", "AssignmentSubmission"),
    ("AssignmentSubmission", "SubmissionAttempt"),
    ("AssignmentSubmission", "AssignmentReview"),
    ("Enrollment", "Grade"),
    ("Grade", "IssuedCertificate"),
])

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42, k=0.9)
nx.draw_networkx_nodes(G, pos, node_size=1800)
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=14)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.title("Граф предметных связей платформенной интеграции курса")
plt.axis("off")
plt.tight_layout()
plt.show()

# %% [7] Диаграмма жизненного цикла CourseRun
# Ожидаемый результат: Строит линейную диаграмму состояний CourseRun: planned → active → completed → archived.
run_states = data_json["course_run_model"]["status_flow"]
RunGraph = nx.DiGraph()
RunGraph.add_edges_from(list(zip(run_states[:-1], run_states[1:])))

plt.figure(figsize=(9, 2.8))
pos = {state: (i, 0) for i, state in enumerate(run_states)}
nx.draw_networkx_nodes(RunGraph, pos, node_size=2200)
nx.draw_networkx_edges(RunGraph, pos, arrows=True, arrowstyle="-|>", arrowsize=18)
nx.draw_networkx_labels(RunGraph, pos, font_size=10)
plt.title("Жизненный цикл CourseRun")
plt.axis("off")
plt.tight_layout()
plt.show()

# %% [8] Загрузка плоских карт контента
# Ожидаемый результат: Загружает CSV-карты и показывает первые строки общей карты загрузки.
content_map_path = DATA_DIR / "content_upload_map.csv"
lessons_map_path = DATA_DIR / "lessons_map.csv"
assessment_map_path = DATA_DIR / "assessment_map.csv"

content_map_df = pd.read_csv(content_map_path)
lessons_map_df = pd.read_csv(lessons_map_path)
assessment_map_df = pd.read_csv(assessment_map_path)

print("Строк в общей карте загрузки:", len(content_map_df))
print("Строк уроков:", len(lessons_map_df))
print("Строк оценочных элементов:", len(assessment_map_df))

content_map_df.head(8)

# %% [9] Структура уроков по типам
# Ожидаемый результат: Строит диаграмму распределения уроков по типам и показывает таблицу counts.
lesson_type_counts = lessons_df.groupby("lesson_type").size().reset_index(name="count")

ax = lesson_type_counts.plot(kind="bar", x="lesson_type", y="count", legend=False, figsize=(8, 4))
ax.set_title("Распределение уроков по типам")
ax.set_xlabel("Тип урока")
ax.set_ylabel("Количество")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

lesson_type_counts

# %% [10] Конвейер загрузки и публикации контента
# Ожидаемый результат: Строит направленную схему этапов загрузки и публикации курса.
pipeline_nodes = [
    "Методическая карта",
    "CourseTemplate",
    "CourseModule",
    "Lesson",
    "StorageObject",
    "CourseResource",
    "AssessmentItem",
    "ContentModerationResult",
    "Published Template",
]
Pipeline = nx.DiGraph()
Pipeline.add_edges_from(list(zip(pipeline_nodes[:-1], pipeline_nodes[1:])))

plt.figure(figsize=(13, 3.2))
pos = {node: (i, 0) for i, node in enumerate(pipeline_nodes)}
nx.draw_networkx_nodes(Pipeline, pos, node_size=2200)
nx.draw_networkx_edges(Pipeline, pos, arrows=True, arrowstyle="-|>", arrowsize=15)
nx.draw_networkx_labels(Pipeline, pos, font_size=8)
plt.title("Конвейер загрузки и публикации контента")
plt.axis("off")
plt.tight_layout()
plt.show()

# %% [11] Карта оценочных элементов
# Ожидаемый результат: Отображает таблицу оценочных элементов: задания, тесты, итоговый проект, схемы оценивания и правила завершения.
assessment_view = assessments_df[[
    "module_id", "assessment_id", "type", "title", "grade_scheme",
    "max_attempts", "competencies_text", "completion_rule"
]].copy()
assessment_view

# %% [12] Матрица покрытия компетенций оценочными элементами
# Ожидаемый результат: Показывает, сколько доказательств освоения связано с каждой компетенцией по типам оценочных элементов.
# Разворачиваем связи компетенций и оценочных элементов.
bindings_df = pd.DataFrame(data_json["competency_bindings"])
coverage = pd.crosstab(bindings_df["competency_code"], bindings_df["assessment_type"])
coverage["total_evidence_items"] = coverage.sum(axis=1)
coverage = coverage.sort_index()

coverage

# %% [13] Визуализация покрытия компетенций
# Ожидаемый результат: Строит матрицу покрытия компетенций по типам оценочных элементов.
coverage_plot = coverage.drop(columns=["total_evidence_items"], errors="ignore")

fig, ax = plt.subplots(figsize=(8, 5))
im = ax.imshow(coverage_plot.values, aspect="auto")
ax.set_xticks(range(len(coverage_plot.columns)))
ax.set_xticklabels(coverage_plot.columns, rotation=30, ha="right")
ax.set_yticks(range(len(coverage_plot.index)))
ax.set_yticklabels(coverage_plot.index)
ax.set_title("Покрытие компетенций оценочными элементами")

for i in range(coverage_plot.shape[0]):
    for j in range(coverage_plot.shape[1]):
        ax.text(j, i, int(coverage_plot.iloc[i, j]), ha="center", va="center")

plt.tight_layout()
plt.show()

# %% [14] Жизненный цикл отправки задания
# Ожидаемый результат: Строит граф состояний отправки задания с возможной доработкой.
submission_states = data_json["submission_lifecycle"]
SubmissionGraph = nx.DiGraph()
SubmissionGraph.add_edges_from([
    ("draft", "submitted"),
    ("submitted", "in_review"),
    ("in_review", "needs_revision"),
    ("needs_revision", "submitted"),
    ("in_review", "accepted"),
    ("in_review", "rejected"),
])

plt.figure(figsize=(9, 5))
pos = nx.spring_layout(SubmissionGraph, seed=7)
nx.draw_networkx_nodes(SubmissionGraph, pos, node_size=2200)
nx.draw_networkx_edges(SubmissionGraph, pos, arrows=True, arrowstyle="-|>", arrowsize=16)
nx.draw_networkx_labels(SubmissionGraph, pos, font_size=10)
plt.title("Жизненный цикл AssignmentSubmission")
plt.axis("off")
plt.tight_layout()
plt.show()

# %% [15] Демонстрационный алгоритм расчета прогресса
# Ожидаемый результат: Создает dataclass DemoProgress и демонстрирует расчет условного прогресса слушателя.
@dataclass
class DemoProgress:
    required_lessons: int
    completed_lessons: int
    required_assessments: int
    passed_assessments: int
    required_competencies: int
    confirmed_competencies: int
    final_project_accepted: bool

    def lesson_percent(self) -> float:
        return self.completed_lessons / self.required_lessons * 100 if self.required_lessons else 0

    def assessment_percent(self) -> float:
        return self.passed_assessments / self.required_assessments * 100 if self.required_assessments else 0

    def competency_percent(self) -> float:
        return self.confirmed_competencies / self.required_competencies * 100 if self.required_competencies else 0

    def total_percent(self) -> float:
        weights = {
            "lessons": 0.35,
            "assessments": 0.40,
            "competencies": 0.25,
        }
        value = (
            self.lesson_percent() * weights["lessons"] +
            self.assessment_percent() * weights["assessments"] +
            self.competency_percent() * weights["competencies"]
        )
        return round(value, 2)

    def completed(self) -> bool:
        return (
            self.completed_lessons == self.required_lessons and
            self.passed_assessments == self.required_assessments and
            self.confirmed_competencies == self.required_competencies and
            self.final_project_accepted
        )

sample = DemoProgress(
    required_lessons=len(lessons_df),
    completed_lessons=40,
    required_assessments=len(assessments_df),
    passed_assessments=16,
    required_competencies=len(competencies_df),
    confirmed_competencies=8,
    final_project_accepted=False,
)

pd.DataFrame([{
    "lesson_percent": sample.lesson_percent(),
    "assessment_percent": sample.assessment_percent(),
    "competency_percent": sample.competency_percent(),
    "total_percent": sample.total_percent(),
    "course_completed": sample.completed(),
}])

# %% [16] Проверка права на выпуск сертификата
# Ожидаемый результат: Демонстрирует алгоритм eligibility: только второй пример получает право на документ.
certificate = data_json["certificate_requirements"]

@dataclass
class CertificateEligibility:
    enrollment_status: str
    confirmed_competencies: int
    required_competencies: int
    final_project_accepted: bool
    required_hours: int
    completed_hours: int

    def is_eligible(self) -> bool:
        return (
            self.enrollment_status == "completed" and
            self.confirmed_competencies == self.required_competencies and
            self.final_project_accepted and
            self.completed_hours >= self.required_hours
        )

examples = [
    CertificateEligibility("active", 8, 10, False, 72, 60),
    CertificateEligibility("completed", 10, 10, True, 72, 72),
    CertificateEligibility("completed", 9, 10, True, 72, 72),
]

pd.DataFrame([
    {
        "enrollment_status": e.enrollment_status,
        "confirmed_competencies": e.confirmed_competencies,
        "final_project_accepted": e.final_project_accepted,
        "completed_hours": e.completed_hours,
        "eligible_for_certificate": e.is_eligible(),
    }
    for e in examples
])

# %% [17] Поля документа об обучении
# Ожидаемый результат: Показывает перечень полей, которые должны быть предусмотрены для IssuedCertificate.
certificate_fields = pd.DataFrame({
    "field": certificate["issuedCertificateFields"],
})
certificate_fields

# %% [18] Матрица API-контрактов
# Ожидаемый результат: Показывает матрицу API endpoint-ов, задействованных в платформенной интеграции курса.
api = data_json["api_contracts"]
api_rows = []
for group, endpoints in api.items():
    if group == "basePrefix":
        continue
    for endpoint in endpoints:
        api_rows.append({"group": group, "endpoint": endpoint})
api_df = pd.DataFrame(api_rows)
api_df

# %% [19] Задачи реализации по зонам ответственности
# Ожидаемый результат: Показывает сводку задач по area и epic.
task_summary = tasks_df.groupby(["area", "epic"]).size().reset_index(name="tasks_count")

task_summary

# %% [20] Диаграмма задач backend/frontend
# Ожидаемый результат: Строит диаграмму количества задач по backend/frontend/qa или другим зонам, если они есть в данных.
area_counts = tasks_df.groupby("area").size().reset_index(name="count")

ax = area_counts.plot(kind="bar", x="area", y="count", legend=False, figsize=(7, 4))
ax.set_title("Количество задач по зонам реализации")
ax.set_xlabel("Зона")
ax.set_ylabel("Количество задач")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

area_counts

# %% [21] Автоматические проверки инвариантов
# Ожидаемый результат: Показывает таблицу автоматических проверок и их статус.
checks = []

def add_check(name, passed, details=""):
    checks.append({"check": name, "passed": bool(passed), "details": details})

add_check("Сумма часов = 72", modules_df["estimated_hours"].sum() == 72, f"sum={modules_df['estimated_hours'].sum()}")
add_check("Количество модулей = 8", len(modules_df) == 8, f"modules={len(modules_df)}")
add_check("Количество компетенций = 10", len(competencies_df) == 10, f"competencies={len(competencies_df)}")
add_check("Каждый модуль имеет уроки", (modules_df["lessons_count"] > 0).all(), "lessons_count > 0")
add_check("Каждый модуль имеет оценочные элементы", (modules_df["assessments_count"] > 0).all(), "assessments_count > 0")
add_check("Итоговый проект присутствует", (assessments_df["type"] == "final_project").any(), "type=final_project")
add_check("Certificate requirements есть", bool(data_json.get("certificate_requirements")), "certificate_requirements")

checks_df = pd.DataFrame(checks)
checks_df

# %% [22] Экспорт производных таблиц для дальнейшей работы
# Ожидаемый результат: Создает каталог data/derived и сохраняет производные CSV-таблицы.
derived_dir = DATA_DIR / "derived"
derived_dir.mkdir(exist_ok=True)

modules_df.to_csv(derived_dir / "modules_summary.csv", index=False)
lessons_df.to_csv(derived_dir / "lessons_summary.csv", index=False)
assessments_df.to_csv(derived_dir / "assessments_summary.csv", index=False)
coverage.to_csv(derived_dir / "competency_coverage.csv")
checks_df.to_csv(derived_dir / "quality_checks.csv", index=False)

print("Экспортировано в:", derived_dir)
print("Файлы:")
for path in sorted(derived_dir.glob("*.csv")):
    print("-", path.name)
