import os
import nbformat.v4
from pathlib import Path
from datetime import datetime


def starts_with(text: str, options):
    for opt in options:
        if text.startswith(opt):
            return True


class NotebookBuilder:
    def __init__(self, nb=nbformat.v4.new_notebook()) -> None:
        self._nb = nb
        self._nb_name = ""
        self._output_directory = "output/"

    @property
    def name(self) -> str:
        return self._nb_name

    def _set_notebook_name(self, prefix: str) -> str:
        if prefix:
            prefix += "-"
        now = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        self._nb_name = self._output_directory + prefix + now + ".ipynb"

    def _add_cell(self, text: str, markdown=False):
        if text:
            self._nb.cells.append(
                nbformat.v4.new_markdown_cell(text.strip())
                if markdown
                else nbformat.v4.new_code_cell(text.strip())
            )
        return ""

    def create_notebook(self, file: str, name: str = "") -> None:
        Path(self._output_directory).mkdir(parents=True, exist_ok=True)
        self._set_notebook_name(prefix=name)
        with open(file) as f:
            code = ""
            comments = ""
            for ln in f:
                if starts_with(ln, ["*-", "**"]):
                    code = self._add_cell(code)
                    comments += (
                        ln[ln.index("-") + 1 :]
                        if ln.startswith("*-")
                        else self._add_cell(comments, markdown=True)
                    )
                else:
                    comments = self._add_cell(comments, markdown=True)
                    code += ln
            self._add_cell(comments, markdown=True)
            self._add_cell(code)
            nbformat.write(self._nb, self._nb_name)


if __name__ == "__main__":
    notebook_name = os.environ["NOTEBOOK_NAME"].strip()
    template = os.environ["TEMPLATE"].strip()
    notebook = NotebookBuilder()
    notebook.create_notebook(template, notebook_name)
    print(notebook.name)
