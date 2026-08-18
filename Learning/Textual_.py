from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label, Static, Widget

# 1. Custom item subclass to cleanly manage task text and labels
class TodoItem(ListItem):
    def __init__(self, task_text: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.task_text = task_text

    def compose(self) -> ComposeResult:
        yield Label(self.task_text)


class TodoApp(App):

    BINDINGS = [
        ("a", "add_task", "Add Task"),
        ("d", "delete_task", "Delete Task"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Static("Todo App (Press 'a' to Add, 'd' to Delete)", id="title")
        # Give the ListView an ID so we can target it in actions
        yield ListView(
            TodoItem("Learn Python"),
            TodoItem("Learn Textual"),
            TodoItem("Build Todo App"),
            id="todo_list"
        )

    def action_add_task(self) -> None:
        # Target the ListView
        todo_list = self.query_one("#todo_list", ListView)
        
        # Create a new item dynamically
        new_item = TodoItem(f"New Task {len(todo_list) + 1}")
        
        # Append it to the list container
        todo_list.mount(new_item)
        
        # Automatically scroll to highlight the newly added item
        todo_list.index = len(todo_list) - 1

    def action_delete_task(self) -> None:
        todo_list = self.query_one("#todo_list", ListView)
        
        # Ensure there is an active row highlighted before trying to delete
        if todo_list.index is not None and len(todo_list) > 0:
            # Get the highlighted item object
            current_item = todo_list.children[todo_list.index]
            
            # Remove the widget directly from the layout interface
            current_item.remove()

class StatsWidget(Widget):

    def compose(self):
        yield Static(id="progress")

    def update_stats(self, completed: int, total: int):
        percentage = int((completed / total) * 100)

        filled = int(15 * percentage / 100)
        empty = 15 - filled

        bar = "█" * filled + "░" * empty

        self.query_one("#progress", Static).update(
            f"{bar}  {percentage}%\n\n"
            f"{completed} / {total} completed"
        )

if __name__ == "__main__":
    TodoApp().run()
