import json
from pathlib import Path
import sys
from jinja2 import Template

AUTO_PREFIX = "axe_"


def load_template(name: str):
    file = Path(__file__).parent / "templates" / name
    template_text = file.read_text(encoding="utf8")
    template = Template(template_text)
    return template


def save_report(
    report: str, severity: str, report_id: str, bug_name: str = None, prefix=AUTO_PREFIX
):
    severity_dir_path = Path("source/reports") / severity
    if not severity_dir_path.exists():
        severity_dir_path.mkdir()
    if bug_name:
        bug_dir_path = severity_dir_path / bug_name
        if not bug_dir_path.exists():
            bug_dir_path.mkdir()
        report_dir_path = bug_dir_path
    else:
        report_dir_path = bug_dir_path
    fname = f"{prefix}{report_id}.md"
    report_file_path = report_dir_path / fname
    report_file_path.write_text(report, encoding="utf8")


def image_alt(violation):
    severity = "major"
    violation_id = violation["id"].replace("-", "_")
    bug_name = "missing_image_alt"
    template = load_template(f"{violation_id}.md")
    for index, node in enumerate(violation["nodes"], start=1):
        selector = node["target"][0]
        report_id = f"{violation_id}_{index:03d}"
        report = template.render(
            selector=selector,
            report_id=report_id,
            severity=severity,
            bug_name=bug_name,
        )

        save_report(report, severity=severity, report_id=report_id, bug_name=bug_name)
        # break


def link_name(violation):
    severity = "major"
    bug_name = "missing_link_text"
    violation_id = violation["id"].replace("-", "_")
    template = load_template(f"{violation_id}.md")
    for index, node in enumerate(violation["nodes"], start=1):
        selector = node["target"][0]
        report_id = f"{violation_id}_{index:03d}"
        report = template.render(
            selector=selector,
            report_id=report_id,
            severity=severity,
            bug_name=bug_name,
        )

        save_report(
            report,
            severity=severity,
            report_id=report_id,
            bug_name=bug_name,
        )
        # break


file = Path(__file__).parent / "results.json"
text = file.read_text()
data = json.loads(text)
for f in Path("source/reports").rglob(f"{AUTO_PREFIX}*.md"):
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
