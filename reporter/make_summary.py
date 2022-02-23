from pathlib import Path
from markdown2 import markdown
from jinja2 import Template

data = []
for file_path in Path("source/reports").rglob("*.md"):
    row = markdown(file_path.read_text(encoding="utf8"), extras=["metadata"]).metadata
    row["link"] = str(file_path).replace("\\", "/").replace("source/", "")
    data.append(row)


data.sort(
    key=lambda entry: ["blocker", "critical", "major", "minor", "tirvial"].index(
        entry["severity"]
    )
)

template = Template(Path("reporter/templates/bugs_list.md").read_text(encoding="utf8"))

text = template.render(data=data)
Path("source/bugs_list.md").write_text(text, encoding="utf8")
