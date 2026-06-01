#!/usr/bin/env python3
"""Generate article 02 pilot-result charts from aggregated YAML data.

The script is intentionally conservative: it refuses datasets that declare
personal data and marks synthetic examples with a visible demo suffix.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import shorten

import matplotlib.pyplot as plt
import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/branches/06_research_articles/article_02_dpo_methodology_v0_5/pilot_aggregates_template.yaml"
DEFAULT_OUTPUT = ROOT / "assets/diagrams/research_articles/pilot_results"

REQUIRED_FIELDS = {
    "progress_by_module": [
        "module_id",
        "module_title",
        "participants_started",
        "participants_completed",
        "completion_rate_percent",
    ],
    "activity_timeline": [
        "date_or_week",
        "material_views_count",
        "submissions_count",
        "attempts_count",
        "feedback_events_count",
    ],
    "final_grade_distribution": ["grade_band", "participants_count", "percentage"],
    "competency_confirmation_matrix": [
        "competency_code",
        "competency_title",
        "artifact_acceptance_rate_percent",
        "test_success_rate_percent",
        "revision_rate_percent",
    ],
    "final_project_readiness_matrix": [
        "criterion",
        "fully_met_count",
        "partially_met_count",
        "not_met_count",
    ],
    "feedback_likert_summary": [
        "question_id",
        "question_text_public",
        "rating_1_count",
        "rating_2_count",
        "rating_3_count",
        "rating_4_count",
        "rating_5_count",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build SVG charts for the article 02 pilot-results section from aggregated YAML data."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to aggregated pilot YAML data.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT, help="Directory for generated SVG charts.")
    parser.add_argument(
        "--allow-synthetic",
        action="store_true",
        help="Allow synthetic_example datasets. Output charts will be marked as demo.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any expected dataset section is empty or absent.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping at the top level.")
    return data


def validate_public_boundary(data: dict, allow_synthetic: bool) -> bool:
    metadata = data.get("metadata") or {}
    if metadata.get("contains_personal_data") is True:
        raise ValueError("Dataset declares contains_personal_data: true. Refusing to generate public charts.")
    status = metadata.get("dataset_status")
    if status == "template":
        print("Input is a template with no pilot data. Nothing to chart yet.")
        return False
    if status == "synthetic_example" and not allow_synthetic:
        raise ValueError("Synthetic example detected. Re-run with --allow-synthetic to generate demo charts.")
    return status == "synthetic_example"


def table(data: dict, key: str, strict: bool) -> pd.DataFrame:
    rows = data.get(key) or []
    if not rows:
        if strict:
            raise ValueError(f"Missing or empty section: {key}")
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    missing = [field for field in REQUIRED_FIELDS[key] if field not in df.columns]
    if missing:
        raise ValueError(f"Section {key} is missing fields: {', '.join(missing)}")
    return df


def apply_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 13,
            "axes.labelsize": 10,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "#374151",
            "axes.grid": True,
            "grid.color": "#e5e7eb",
            "grid.linewidth": 0.8,
            "legend.frameon": False,
            "svg.fonttype": "none",
        }
    )


def title(text: str, demo: bool) -> str:
    return f"{text} (ДЕМО, не публиковать)" if demo else text


def save(fig: plt.Figure, path: Path) -> None:
    fig.tight_layout()
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"generated: {path}")


def chart_progress(df: pd.DataFrame, output_dir: Path, demo: bool) -> None:
    if df.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 5.4))
    labels = df["module_id"] + " · " + df["module_title"].map(lambda value: shorten(str(value), width=28, placeholder="..."))
    ax.barh(labels, df["completion_rate_percent"], color="#2f80ed")
    ax.set_xlim(0, 100)
    ax.set_xlabel("Доля завершения, %")
    ax.set_title(title("Прогресс по модулям пилотного курса", demo))
    ax.invert_yaxis()
    for index, value in enumerate(df["completion_rate_percent"]):
        ax.text(min(float(value) + 1, 98), index, f"{value:.1f}%", va="center", fontsize=9)
    save(fig, output_dir / "pilot_progress_by_module.svg")


def chart_activity(df: pd.DataFrame, output_dir: Path, demo: bool) -> None:
    if df.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 5.2))
    x = df["date_or_week"].astype(str)
    series = [
        ("material_views_count", "Открытия материалов", "#2f80ed"),
        ("submissions_count", "Отправки заданий", "#27ae60"),
        ("attempts_count", "Попытки", "#f2994a"),
        ("feedback_events_count", "Обратная связь", "#9b51e0"),
    ]
    for column, label, color in series:
        ax.plot(x, df[column], marker="o", linewidth=2, label=label, color=color)
    ax.set_title(title("Активность пользователей по времени", demo))
    ax.set_xlabel("Период")
    ax.set_ylabel("Количество событий")
    ax.legend(loc="upper left", ncols=2)
    save(fig, output_dir / "pilot_activity_timeline.svg")


def chart_grades(df: pd.DataFrame, output_dir: Path, demo: bool) -> None:
    if df.empty:
        return
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.bar(df["grade_band"].astype(str), df["participants_count"], color="#27ae60")
    ax.set_title(title("Распределение итоговых результатов", demo))
    ax.set_xlabel("Диапазон результата")
    ax.set_ylabel("Количество участников")
    for index, row in df.iterrows():
        ax.text(index, row["participants_count"] + 0.15, f"{row['percentage']:.1f}%", ha="center", fontsize=9)
    save(fig, output_dir / "pilot_final_grade_distribution.svg")


def chart_competencies(df: pd.DataFrame, output_dir: Path, demo: bool) -> None:
    if df.empty:
        return
    metrics = [
        "artifact_acceptance_rate_percent",
        "test_success_rate_percent",
        "revision_rate_percent",
    ]
    metric_labels = ["Артефакты приняты", "Тесты/проверки", "Доработки"]
    matrix = df[metrics].to_numpy(dtype=float)
    fig, ax = plt.subplots(figsize=(10, 5.6))
    image = ax.imshow(matrix, cmap="YlGnBu", vmin=0, vmax=100, aspect="auto")
    ax.set_title(title("Матрица подтверждения компетенций", demo))
    ax.set_xticks(range(len(metrics)), labels=metric_labels)
    ax.set_yticks(range(len(df)), labels=df["competency_code"])
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            ax.text(x, y, f"{matrix[y, x]:.0f}%", ha="center", va="center", fontsize=8, color="#111827")
    fig.colorbar(image, ax=ax, label="Доля, %")
    save(fig, output_dir / "pilot_competency_confirmation_matrix.svg")


def chart_final_projects(df: pd.DataFrame, output_dir: Path, demo: bool) -> None:
    if df.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 5.2))
    y = range(len(df))
    full = df["fully_met_count"].astype(float)
    partial = df["partially_met_count"].astype(float)
    not_met = df["not_met_count"].astype(float)
    ax.barh(y, full, color="#27ae60", label="Полностью")
    ax.barh(y, partial, left=full, color="#f2c94c", label="Частично")
    ax.barh(y, not_met, left=full + partial, color="#eb5757", label="Не выполнено")
    ax.set_yticks(y, labels=df["criterion"].map(lambda value: shorten(str(value), width=32, placeholder="...")))
    ax.invert_yaxis()
    ax.set_xlabel("Количество проектов")
    ax.set_title(title("Готовность итоговых проектов", demo))
    ax.legend(loc="lower right", ncols=3)
    save(fig, output_dir / "pilot_final_project_readiness_matrix.svg")


def chart_feedback(df: pd.DataFrame, output_dir: Path, demo: bool) -> None:
    if df.empty:
        return
    rating_columns = [f"rating_{value}_count" for value in range(1, 6)]
    colors = ["#eb5757", "#f2994a", "#f2c94c", "#6fcf97", "#27ae60"]
    fig, ax = plt.subplots(figsize=(10, 5.2))
    labels = df["question_text_public"].map(lambda value: shorten(str(value), width=36, placeholder="..."))
    left = pd.Series([0] * len(df), dtype=float)
    for column, color in zip(rating_columns, colors):
        values = df[column].astype(float)
        ax.barh(labels, values, left=left, color=color, label=column.replace("rating_", "").replace("_count", ""))
        left += values
    ax.invert_yaxis()
    ax.set_xlabel("Количество ответов")
    ax.set_title(title("Сводка обратной связи преподавателей", demo))
    ax.legend(title="Оценка", loc="lower right", ncols=5)
    save(fig, output_dir / "pilot_feedback_likert_summary.svg")


def main() -> int:
    args = parse_args()
    apply_style()

    data = load_yaml(args.input)
    demo = validate_public_boundary(data, args.allow_synthetic)

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    datasets = {key: table(data, key, args.strict) for key in REQUIRED_FIELDS}
    if all(df.empty for df in datasets.values()):
        print("No chart datasets found. Fill the aggregate YAML after the pilot and rerun this script.")
        return 0

    chart_progress(datasets["progress_by_module"], output_dir, demo)
    chart_activity(datasets["activity_timeline"], output_dir, demo)
    chart_grades(datasets["final_grade_distribution"], output_dir, demo)
    chart_competencies(datasets["competency_confirmation_matrix"], output_dir, demo)
    chart_final_projects(datasets["final_project_readiness_matrix"], output_dir, demo)
    chart_feedback(datasets["feedback_likert_summary"], output_dir, demo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
