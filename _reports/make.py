import json
from pathlib import Path
import sys


def load_template(name: str):
    file = Path(__file__).parent / "templates" / name
    template = file.read_text(encoding="utf8")
    return template


def save_report1(file_name: str, report: str):
    file = Path(__file__).parent / "reports" / file_name
    file.write_text(report, encoding="utf8")


def save_report(report: str, severity: str, report_id: str):
    severity_path = Path("source/reports") / severity
    if not severity_path.exists():
        severity_path.mkdir()
    fname = f"auto_{report_id}.md"
    report_file_path = severity_path / fname
    report_file_path.write_text(report, encoding="utf8")


def image_alt(violation):
    severity = "major"
    violation_id = violation["id"].replace("-", "_")
    template = load_template(f"{violation_id}.md")
    for index, node in enumerate(violation["nodes"], start=1):
        selector = node["target"][0]
        report_id = f"{violation_id}_{index:03d}"
        report = template.format(
            selector=selector,
            report_id=report_id,
            severity=severity,
            summary="{summary}",
        )

        save_report(report, severity=severity, report_id=report_id)
        # break


file = Path(__file__).parent / "results.json"
text = file.read_text()
data = json.loads(text)
for f in Path("source/reports").rglob("auto_*.md"):
    f.unlink()

for violation in data["violations"]:
    id: str = violation["id"]
    func_name = id.replace("-", "_")
    func = getattr(sys.modules[__name__], func_name, None)
    if func is None:
        print(f"make manual: {id}")
        continue
        # break
    func(violation)
else:
    print("All tasks completed!")
