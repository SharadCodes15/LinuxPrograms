import json

from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Label, ListItem, ListView


class SidebarItem(ListItem):
    def __init__(self, category: str, **kwargs):
        super().__init__(**kwargs)
        self.category = category

    def compose(self) -> ComposeResult:
        yield Label(self.category)


class Sidebar(Container):

    def compose(self) -> ComposeResult:
        with open("todo.json", "r", encoding="utf-8") as data:
            sidebar_data = json.load(data)

        categories = sorted({
            todo["category"]
            for todo in sidebar_data["todos"]
        })

        yield ListView(
            *[
                SidebarItem(category)
                for category in categories
            ],
            id="category-list",
        )