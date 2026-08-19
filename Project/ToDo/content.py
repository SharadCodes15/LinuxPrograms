import json

from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Label, ListItem, ListView


class ContentItem(ListItem):
    def __init__(self, task_text: str, **kwargs):
        super().__init__(**kwargs)
        self.task_text = task_text

    def compose(self) -> ComposeResult:
        yield Label(self.task_text)


class Content(Container):

    def __init__(self, *children, **kwargs):
        super().__init__(*children, **kwargs)

        self.content_data = {}

    def compose(self) -> ComposeResult:
        with open("todo.json", "r", encoding="utf-8") as data:
            self.content_data = json.load(data)

        yield ListView(id="task-list")

    def show_category(self, category: str) -> None:
        task_list = self.query_one("#task-list", ListView)

        task_list.clear()

        for todo in self.content_data["todos"]:
            if todo["category"] == category:
                task_list.append(
                    ContentItem(todo["title"])
                )