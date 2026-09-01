from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import ListView, Static, ListItem, Label, Footer

from sidebar import Sidebar, SidebarItem
from content import Content


class Todo(App):

    CSS_PATH = "./style.tcss"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("a", "add", "Add"),
        ("d", "delete", "Delete"),
    ]
    
    def compose(self) -> ComposeResult:
        yield Static("Todo App", id="title")
        with Horizontal():
            yield Sidebar(id="sidebar")
            yield Content(id="content")
        yield Footer()

    def on_list_view_selected(
        self,
        event: ListView.Selected,
    ) -> None:

        if isinstance(event.item, SidebarItem):
            category = event.item.category

            content = self.query_one(Content)
            content.show_category(category)






