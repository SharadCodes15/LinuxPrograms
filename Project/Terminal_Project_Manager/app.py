from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import ListView, Statics,Listview, Static, ListItem, Label

class TerminalProjectManager(App):

    CSS_PATH = "./style.tcss"

    def compose(self) -> ComposeResult:
        yield Static("Terminal Project Manager", id="title")
        with Horizontal():
            yield ListView(id="sidebar")
            yield Static("Content Area", id="content")
        yield Static("q Quit | a Add | d Delete", id="footer")

    def on_list_view_selected(
        self,
        event: ListView.Selected,
    ) -> None:
        # Handle selection events from the sidebar
        pass