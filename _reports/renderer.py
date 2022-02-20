from datetime import datetime
from enum import Enum
from pathlib import Path

import click
import jinja2
import markdown2
import pypugjs

BOOTSTRAP5 = """<!doctype html>
<html lang="{{lang}}">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>{{title}}</title>
  </head>
  <body>
    <div class="container">
      {{rendered_content}}
    </div>
    <!-- Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
  </body>
</html>"""


class CONTENT_TYPE(Enum):
    markdown = "markdown"
    pug = "pug"
    jinja2 = "jinja2"


class Renderer:
    def __init__(
        self,
        content: str,
        content_type: CONTENT_TYPE = CONTENT_TYPE.jinja2,
        name: str = None,
    ):
        self.content = content
        self.name = name or datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        self.content_type = content_type


        self.metadata = {"title": self.name, "lang": "en"}
        self.rendered_content = None
        self.html = None

    @classmethod
    def from_file(cls, filename: str, content_type: CONTENT_TYPE = None):
        input_file_path = Path(filename)
        content = input_file_path.read_text(encoding="utf8")
        name = input_file_path.stem
        if content_type is None:
            input_file_suffix = input_file_path.suffix.lower()
            if input_file_suffix in (".md",):
                content_type = CONTENT_TYPE.markdown
            elif input_file_suffix in (".pug",):
                content_type = CONTENT_TYPE.pug
            else:
                content_type = CONTENT_TYPE.jinja2
        return cls(content=content, content_type=content_type, name=name)

    def render(self, **kwargs):
        if self.content_type == CONTENT_TYPE.pug:
            self.render_pug(**kwargs)
        elif self.content_type == CONTENT_TYPE.markdown:
            classes = {"table": "table"}
            self.rendered_content = markdown2.markdown(
                self.content,
                extras={
                    "metadata": None,
                    "tables": None,
                    "fenced-code-blocks": None,
                    "html-classes": classes,
                },
            )
            self.metadata.update(self.rendered_content.metadata)
        else:
            self.render_jinja2(**kwargs)
        return self.rendered_content

    def render_jinja2(self, **kwargs):
        env = jinja2.Environment(
            loader=jinja2.DictLoader({"jinja2": self.content}),
            extensions=["pypugjs.ext.jinja.PyPugJSExtension"],
        )
        template = env.get_template("jinja2")
        params = self.metadata | kwargs
        self.rendered_content = template.render(**params)

    def render_pug(self, **kwargs):
        env = jinja2.Environment(
            loader=jinja2.DictLoader({"pug": self.content}),
            extensions=["pypugjs.ext.jinja.PyPugJSExtension"],
        )
        template = env.get_template("pug")
        params = self.metadata | kwargs
        self.rendered_content = template.render(**params)

    def render_html(self, **kwargs):
        env = jinja2.Environment(
            loader=jinja2.DictLoader({"jinja2": BOOTSTRAP5}),
        )
        template = env.get_template("jinja2")
        params = self.metadata | kwargs
        self.html = template.render(rendered_content=self.rendered_content, **params)

    def save_html(self, output_file: str = None, **kwargs):
        if output_file:
            output_file_path = Path(output_file)
        else:
            output_file_path = Path(f"{self.name}.html")
        self.render(**kwargs)
        self.render_html(**kwargs)
        output_file_path.write_text(self.html, encoding="utf8")
        return self.html


@click.command()
@click.option("--file", prompt="input file", help="File to convert.")
def run(file):
    Renderer.from_file(filename=file).save_html()


if __name__ == "__main__":
    run()
