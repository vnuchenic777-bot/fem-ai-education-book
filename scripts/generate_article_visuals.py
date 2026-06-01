"""Generate reproducible SVG diagrams for the research article series."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import textwrap

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "diagrams" / "research_articles"
COMPETENCIES_PATH = ROOT / "book" / "05_certification" / "data" / "competencies.yaml"
SPEC_PATH = ROOT / "book" / "05_certification" / "implementation_spec.yaml"

FONT = "Inter, Arial, 'Noto Sans', sans-serif"
TEXT = "#1f2937"
MUTED = "#64748b"
GRID = "#d6dde7"
BG = "#ffffff"


@dataclass
class Svg:
    width: int
    height: int

    def __post_init__(self) -> None:
        self.items: list[str] = []

    def add(self, raw: str) -> None:
        self.items.append(raw)

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        fill: str = "#ffffff",
        stroke: str = GRID,
        rx: int = 8,
        sw: float = 1.6,
    ) -> None:
        self.add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        stroke: str = "#334155",
        sw: float = 2.2,
        dash: str | None = None,
        arrow: bool = True,
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        arrow_attr = ' marker-end="url(#arrow)"' if arrow else ""
        self.add(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"'
            f'{dash_attr}{arrow_attr}/>'
        )

    def path(
        self,
        d: str,
        stroke: str = "#334155",
        sw: float = 2.2,
        fill: str = "none",
        dash: str | None = None,
        arrow: bool = True,
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        arrow_attr = ' marker-end="url(#arrow)"' if arrow else ""
        self.add(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"{dash_attr}{arrow_attr}/>'
        )

    def text(
        self,
        x: float,
        y: float,
        text: str,
        size: int = 18,
        weight: int = 400,
        color: str = TEXT,
        anchor: str = "start",
    ) -> None:
        self.add(
            f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(text)}</text>'
        )

    def wrapped(
        self,
        x: float,
        y: float,
        text: str,
        width: float,
        size: int = 16,
        line_height: int = 21,
        color: str = TEXT,
        weight: int = 400,
        max_lines: int | None = None,
        anchor: str = "start",
    ) -> int:
        chars = max(8, int(width / (size * 0.54)))
        lines = textwrap.wrap(text, width=chars, break_long_words=False)
        if max_lines and len(lines) > max_lines:
            lines = lines[:max_lines]
            lines[-1] = lines[-1].rstrip(" .,:;") + "..."
        self.add(
            f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">'
        )
        for i, line in enumerate(lines):
            dy = 0 if i == 0 else line_height
            self.add(f'<tspan x="{x}" dy="{dy}">{escape(line)}</tspan>')
        self.add("</text>")
        return len(lines)

    def title(self, title: str, subtitle: str) -> None:
        self.text(60, 58, title, size=30, weight=700, color="#111827")
        self.wrapped(60, 92, subtitle, self.width - 120, size=17, line_height=23, color=MUTED)

    def save(self, path: Path) -> None:
        defs = f"""<defs>
  <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
    <path d="M2,2 L10,6 L2,10 Z" fill="#334155"/>
  </marker>
  <style>
    .small {{ font-size: 13px; fill: {MUTED}; }}
  </style>
</defs>"""
        doc = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}" role="img">'
            f'<rect width="100%" height="100%" fill="{BG}"/>'
            f"{defs}"
            + "".join(self.items)
            + "</svg>\n"
        )
        path.write_text(doc, encoding="utf-8")


def load_competencies() -> list[dict]:
    data = yaml.safe_load(COMPETENCIES_PATH.read_text(encoding="utf-8"))
    return data["competencies"]


def card(
    svg: Svg,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    body: str,
    fill: str,
    stroke: str,
    title_color: str = "#111827",
    body_color: str = TEXT,
    title_size: int = 18,
    body_size: int = 15,
) -> None:
    svg.rect(x, y, w, h, fill=fill, stroke=stroke, rx=8, sw=1.8)
    svg.wrapped(x + 18, y + 31, title, w - 36, size=title_size, line_height=22, weight=700, color=title_color)
    svg.wrapped(x + 18, y + 61, body, w - 36, size=body_size, line_height=20, color=body_color)


def pill(svg: Svg, x: float, y: float, text: str, fill: str, stroke: str, color: str = TEXT) -> None:
    w = 12 + len(text) * 9
    svg.rect(x, y, w, 30, fill=fill, stroke=stroke, rx=8, sw=1.2)
    svg.text(x + w / 2, y + 20, text, size=14, weight=700, color=color, anchor="middle")


def generate_publication_contour() -> None:
    svg = Svg(1600, 960)
    svg.title(
        "Карта публикационного контура проекта",
        "Схема показывает, как проектные материалы, Jupyter Book, серия статей и публичная публикация на GitHub Pages образуют единый исследовательско-методический контур.",
    )

    columns = [
        (72, "Проектная работа", "#ecfeff", "#0891b2"),
        (373, "Исходные материалы", "#f0fdf4", "#16a34a"),
        (674, "Jupyter Book", "#fff7ed", "#ea580c"),
        (975, "Серия статей", "#eff6ff", "#2563eb"),
        (1276, "Публичный доступ", "#f8fafc", "#64748b"),
    ]
    for x, title, fill, stroke in columns:
        svg.rect(x, 142, 252, 46, fill=fill, stroke=stroke, rx=8)
        svg.text(x + 126, 172, title, size=17, weight=700, color="#111827", anchor="middle")

    project = [
        ("Платформа", "роли, доступ, данные, PWA"),
        ("Курс ДПО", "72 часа, 8 модулей, ПК-ИИ-1 — ПК-ИИ-10"),
        ("Оценивание", "артефакты, тесты, итоговый проект"),
        ("Документ результата", "статус, PDF, QR, аудит"),
    ]
    materials = [
        ("Markdown", "главы, README, редакционные версии"),
        ("YAML / JSON", "структуры курса, спецификации, данные"),
        ("Notebooks", "таблицы, графики, проверяемые расчёты"),
        ("Assets", "изображения, диаграммы, схемы"),
    ]
    book = [
        ("_config.yml", "параметры сборки и репозитория"),
        ("_toc.yml", "структура книги и порядок глав"),
        ("book/", "публичные главы и notebooks"),
        ("bibliography.bib", "единая база источников"),
    ]
    articles = [
        ("Статья 01", "концепция платформы и экосистемы"),
        ("Статья 02", "методология ДПО по ИИ-инструментам"),
        ("Статья 03", "цифровой документ результата обучения"),
    ]
    public = [
        ("GitHub Pages", "автоматически собранный HTML"),
        ("Читатель", "переходит от статьи к данным и главам"),
        ("Рецензент", "видит источники и воспроизводимость"),
    ]

    def contour_card(
        x: int,
        y: int,
        title: str,
        body: str,
        fill: str,
        stroke: str,
        w: int = 252,
        h: int = 88,
    ) -> None:
        svg.rect(x, y, w, h, fill=fill, stroke=stroke, rx=8, sw=1.7)
        svg.wrapped(x + w / 2, y + 31, title, w - 36, size=18, line_height=22, weight=700, anchor="middle", max_lines=1)
        svg.wrapped(x + w / 2, y + 59, body, w - 34, size=14, line_height=19, color=TEXT, anchor="middle", max_lines=2)

    def stack(x: int, items: list[tuple[str, str]], fill: str, stroke: str, start_y: int = 218) -> None:
        for i, (title, body) in enumerate(items):
            contour_card(x, start_y + i * 112, title, body, fill, stroke)

    stack(72, project, "#f8fdff", "#67e8f9")
    stack(373, materials, "#fbfffb", "#86efac")
    stack(674, book, "#fffaf2", "#fdba74")
    stack(975, articles, "#f7fbff", "#93c5fd", start_y=274)
    stack(1276, public, "#ffffff", "#cbd5e1", start_y=274)

    centers = [198, 499, 800, 1101, 1402]
    svg.text(800, 685, "основной поток подготовки публичной книги", size=15, weight=700, color="#334155", anchor="middle")
    for left, right in zip(centers[:-1], centers[1:]):
        svg.line(left + 126, 708, right - 126, 708, stroke="#475569", sw=2.4)

    svg.line(1402, 752, 198, 752, stroke="#0f766e", sw=2.0, dash="7 7")
    svg.text(800, 779, "обратная связь: уточнение статей, данных, визуализаций и открытых вопросов", size=15, color="#0f766e", anchor="middle")

    svg.rect(72, 818, 1456, 108, fill="#fff1f2", stroke="#f43f5e", rx=8)
    svg.text(104, 853, "Граница открытой публикации", size=18, weight=700, color="#9f1239")
    svg.wrapped(
        104,
        883,
        "В публичный контур не выносятся ключи доступа, персональные данные и закрытые материалы организации. Юридические утверждения публикуются только после отдельного согласования.",
        1388,
        size=16,
        line_height=22,
        color="#4c0519",
    )
    svg.text(1528, 945, "Источник: проектная структура репозитория Jupyter Book, 2026", size=13, color=MUTED, anchor="end")
    svg.save(OUT_DIR / "publication_contour_map.svg")


def generate_competency_graph(competencies: list[dict]) -> None:
    svg = Svg(1600, 1100)
    svg.title(
        "Граф компетентностной модели ПК-ИИ-1 — ПК-ИИ-10",
        "Визуализация показывает методическую связность компетенций курса ДПО: от понимания ИИ и постановки запросов к профессиональным применениям, ограничениям и итоговому переносу в дисциплину.",
    )

    comp = {item["code"]: item for item in competencies}
    groups = [
        (80, 235, 235, 126, "ПК-ИИ-1", "#ecfeff", "#0891b2"),
        (405, 195, 250, 126, "ПК-ИИ-2", "#f0fdf4", "#16a34a"),
        (405, 365, 250, 126, "ПК-ИИ-3", "#f0fdf4", "#16a34a"),
        (760, 150, 300, 112, "ПК-ИИ-4", "#fff7ed", "#ea580c"),
        (760, 280, 300, 112, "ПК-ИИ-5", "#fff7ed", "#ea580c"),
        (760, 410, 300, 112, "ПК-ИИ-6", "#fff7ed", "#ea580c"),
        (760, 540, 300, 112, "ПК-ИИ-7", "#fff7ed", "#ea580c"),
        (760, 670, 300, 112, "ПК-ИИ-8", "#fff7ed", "#ea580c"),
        (1150, 310, 275, 126, "ПК-ИИ-9", "#fef2f2", "#dc2626"),
        (1150, 540, 275, 126, "ПК-ИИ-10", "#eef2ff", "#4f46e5"),
    ]

    svg.text(197, 150, "Основание", size=16, weight=700, color="#0891b2", anchor="middle")
    svg.text(530, 150, "Операционные навыки", size=16, weight=700, color="#15803d", anchor="middle")
    svg.text(910, 118, "Профессиональные применения", size=16, weight=700, color="#c2410c", anchor="middle")
    svg.text(1288, 270, "Границы", size=16, weight=700, color="#b91c1c", anchor="middle")
    svg.text(1288, 500, "Интеграция", size=16, weight=700, color="#4338ca", anchor="middle")

    for x, y, w, h, code, fill, stroke in groups:
        item = comp[code]
        svg.rect(x, y, w, h, fill=fill, stroke=stroke, rx=8, sw=1.8)
        svg.text(x + 18, y + 30, code, size=19, weight=700, color="#111827")
        svg.wrapped(x + 18, y + 58, item["name"], w - 36, size=15, line_height=19, max_lines=3)
        modules = ", ".join(f"М{m}" if m.isdigit() else m for m in item.get("modules", []))
        svg.text(x + 18, y + h - 18, f"Модули: {modules}", size=13, color=MUTED)

    # Main logic arrows.
    svg.line(315, 298, 390, 258, stroke="#0f766e")
    svg.line(315, 298, 390, 428, stroke="#0f766e")
    svg.path("M655 258 C690 250, 710 220, 745 205", stroke="#92400e")
    svg.path("M655 258 C700 320, 700 420, 745 485", stroke="#92400e")
    svg.path("M655 428 C705 440, 710 610, 745 725", stroke="#92400e")
    svg.path("M1060 205 C1115 225, 1105 318, 1135 365", stroke="#b91c1c")
    svg.path("M1060 336 C1120 350, 1110 380, 1135 386", stroke="#b91c1c")
    svg.path("M1060 596 C1110 590, 1110 603, 1135 603", stroke="#4f46e5")
    svg.path("M1425 373 C1490 415, 1490 556, 1432 603", stroke="#64748b", dash="7 7")
    svg.wrapped(1500, 485, "ограничения учитываются при итоговом переносе", 150, size=13, line_height=17, color=MUTED, anchor="middle")

    svg.rect(90, 870, 1420, 110, fill="#f8fafc", stroke="#cbd5e1", rx=8)
    svg.text(118, 902, "Как читать граф", size=18, weight=700, color="#111827")
    svg.wrapped(
        118,
        932,
        "Стрелки показывают методическую связность, а не жёсткую юридическую последовательность освоения. Каждая компетенция подтверждается через артефакт и тестовую или практическую проверку, а ПК-ИИ-10 собирает результаты в итоговом проекте.",
        1340,
        size=16,
        line_height=22,
        color=TEXT,
    )
    pill(svg, 118, 1012, "артефакт + проверка", "#ecfeff", "#0891b2", "#155e75")
    pill(svg, 330, 1012, "цифровой след", "#f0fdf4", "#16a34a", "#166534")
    pill(svg, 500, 1012, "итоговый проект", "#eef2ff", "#4f46e5", "#3730a3")
    svg.text(1540, 1072, "Источник: book/05_certification/data/competencies.yaml", size=13, color=MUTED, anchor="end")
    svg.save(OUT_DIR / "competency_graph.svg")


def generate_certificate_lifecycle() -> None:
    svg = Svg(1500, 840)
    svg.title(
        "Жизненный цикл цифрового документа результата обучения",
        "Схема фиксирует проектные статусы записи IssuedCertificate и условия переходов; она не утверждает юридический порядок выдачи сертификата или удостоверения.",
    )

    preconditions = [
        ("Права инициатора", "роль и организация проверены"),
        ("Курс завершён", "Enrollment имеет итоговый статус completed"),
        ("Компетенции подтверждены", "ПК-ИИ-1 — ПК-ИИ-10: артефакт + проверка"),
        ("Шаблон активен", "CertificateTemplate выбран и разрешён"),
    ]
    for i, (title, body) in enumerate(preconditions):
        card(svg, 70 + i * 350, 145, 285, 88, title, body, "#f8fafc", "#cbd5e1", body_size=14)
        if i < 3:
            svg.line(355 + i * 350, 189, 405 + i * 350, 189, stroke="#64748b", sw=1.8)

    svg.line(760, 235, 760, 285, stroke="#64748b", sw=2.0)

    states = {
        "draft": (95, 325, "#fff7ed", "#ea580c", "подготовлен, но не выдан"),
        "partial": (385, 325, "#fefce8", "#ca8a04", "частичное освоение или доработка"),
        "issued": (680, 325, "#ecfdf5", "#059669", "выдан после подтверждения условий"),
        "revoked": (1010, 260, "#fef2f2", "#dc2626", "отозван по основанию"),
        "reissued": (1010, 435, "#eef2ff", "#4f46e5", "перевыпущен с сохранением связи"),
    }
    for code, (x, y, fill, stroke, body) in states.items():
        card(svg, x, y, 225, 92, code, body, fill, stroke, title_size=22, body_size=15)

    svg.line(320, 371, 370, 371, stroke="#334155")
    svg.line(610, 371, 665, 371, stroke="#334155")
    svg.path("M320 350 C445 260, 560 260, 680 350", stroke="#334155", dash="7 7")
    svg.path("M905 360 C945 320, 960 304, 995 304", stroke="#b91c1c")
    svg.path("M905 395 C950 450, 960 480, 995 480", stroke="#4338ca")
    svg.path("M1235 480 C1330 480, 1330 371, 918 371", stroke="#4338ca", dash="7 7")

    svg.text(485, 284, "после доработки", size=14, color=MUTED, anchor="middle")
    svg.text(520, 295, "возможен прямой переход draft → issued при полном выполнении условий", size=14, color=MUTED, anchor="middle")
    svg.text(1280, 376, "новая версия документа", size=14, color="#4338ca", anchor="middle")

    svg.rect(95, 585, 1220, 92, fill="#f8fafc", stroke="#cbd5e1", rx=8)
    svg.text(122, 620, "AuditLog сопровождает критические действия", size=18, weight=700)
    svg.wrapped(
        122,
        650,
        "Фиксируются generation, issued, revoked, reissued, downloaded, verified.public и verification.failed. Отзыв и повторная выдача требуют основания, прав доступа и записи в журнале.",
        1140,
        size=16,
        line_height=22,
    )

    svg.rect(95, 710, 1220, 62, fill="#fff1f2", stroke="#f43f5e", rx=8)
    svg.text(122, 748, "Юридический статус, подпись, регистрация и хранение утверждаются отдельно образовательной организацией.", size=16, weight=700, color="#9f1239")
    svg.text(1440, 808, "Источник: book/05_certification/implementation_spec.yaml", size=13, color=MUTED, anchor="end")
    svg.save(OUT_DIR / "certificate_lifecycle.svg")


def generate_qr_verification_flow() -> None:
    svg = Svg(1600, 900)
    svg.title(
        "QR-проверка и минимизация раскрытия данных",
        "Схема показывает публичный контур проверки документа по verificationCode: QR ведёт к ограниченному ответу платформы, а не к раскрытию внутренних данных слушателя.",
    )

    flow = [
        ("PDF-документ", "содержит QR и реквизиты"),
        ("QR / verificationUrl", "код не совпадает с рег. номером"),
        ("Публичный endpoint", "GET /verify/{code}; rate limit"),
        ("Поиск IssuedCertificate", "по неугадываемому verificationCode"),
        ("Проверка статуса", "issued, revoked, reissued или ошибка"),
        ("Публичный ответ", "минимальный набор сведений"),
    ]
    x0 = 55
    y = 175
    for i, (title, body) in enumerate(flow):
        x = x0 + i * 255
        card(svg, x, y, 205, 110, title, body, "#f8fafc" if i != 5 else "#ecfdf5", "#cbd5e1" if i != 5 else "#059669", body_size=14)
        if i < len(flow) - 1:
            svg.line(x + 205, y + 55, x + 248, y + 55, stroke="#334155")

    svg.path("M1180 285 C1130 360, 885 360, 785 305", stroke="#0f766e", dash="7 7")
    svg.text(985, 382, "AuditLog: certificate.verified.public или certificate.verification.failed", size=14, color="#0f766e", anchor="middle")

    svg.rect(80, 455, 660, 260, fill="#f0fdf4", stroke="#16a34a", rx=8)
    svg.text(110, 492, "Публично допустимый минимум", size=20, weight=700, color="#166534")
    public_items = [
        "valid и status документа",
        "registrationNumber",
        "courseTitle и hours",
        "issuedAt и issuer",
        "holderName только ограниченно и при согласовании",
    ]
    for i, item in enumerate(public_items):
        svg.text(125, 535 + i * 34, "•", size=20, color="#166534")
        svg.text(150, 535 + i * 34, item, size=17, color=TEXT)

    svg.rect(860, 455, 660, 260, fill="#fff1f2", stroke="#f43f5e", rx=8)
    svg.text(890, 492, "Не раскрывать на публичной странице", size=20, weight=700, color="#9f1239")
    private_items = [
        "userId, email, phone и внутренние идентификаторы",
        "storageKey, fileHash и служебные данные файла",
        "signatureMetadata без отдельного основания",
        "внутренний AuditLog, IP, userAgent",
        "причины отзыва и комментарии проверяющих",
    ]
    for i, item in enumerate(private_items):
        svg.text(905, 535 + i * 34, "•", size=20, color="#9f1239")
        svg.text(930, 535 + i * 34, item, size=17, color=TEXT)

    svg.rect(80, 760, 1440, 68, fill="#fff7ed", stroke="#ea580c", rx=8)
    svg.text(110, 800, "Ключевой принцип: QR-проверка подтверждает статус записи платформы, но не заменяет подпись, регистрацию и юридически утверждённый порядок выдачи.", size=17, weight=700, color="#9a3412")
    svg.text(1510, 862, "Источник: qr_verification_flow.ipynb и implementation_spec.yaml", size=13, color=MUTED, anchor="end")
    svg.save(OUT_DIR / "qr_verification_flow.svg")


def generate_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    competencies = load_competencies()
    # SPEC_PATH is deliberately read so the script fails if the canonical spec is missing.
    yaml.safe_load(SPEC_PATH.read_text(encoding="utf-8"))
    generate_publication_contour()
    generate_competency_graph(competencies)
    generate_certificate_lifecycle()
    generate_qr_verification_flow()


if __name__ == "__main__":
    generate_all()
    print(f"Generated SVG diagrams in {OUT_DIR}")
