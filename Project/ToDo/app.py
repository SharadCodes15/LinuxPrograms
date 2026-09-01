import json
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import ListView, Static, ListItem, Label, Footer

from sidebar import Sidebar, SidebarItem
from content import Content, ContentItem


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

    def action_delete(self) -> None:
        """Delete the selected todo item"""
        task_list = self.query_one("#task-list", ListView)
        selected_index = task_list.index
        
        if selected_index is None:
            return
        
        # Get the selected item
        selected_item = task_list.children[selected_index]
        
        if isinstance(selected_item, ContentItem):
            # Load the todo data
            with open("todo.json", "r", encoding="utf-8") as data:
                todo_data = json.load(data)
            
            # Remove the todo from the data
            task_text = selected_item.task_text
            todo_data["todos"] = [
                todo for todo in todo_data["todos"]
                if todo["title"] != task_text
            ]
            
            # Save back to file
            with open("todo.json", "w", encoding="utf-8") as data:
                json.dump(todo_data, data, indent=2)
            
            # Remove from UI
            task_list.remove(selected_item)






