# ============================================================
# SIMPLE TEXTUAL PROJECT MANAGER
# ============================================================

# App:
# The main class used to create a Textual application.
#
# ComposeResult:
# Used as the return type of the compose() method.
from textual.app import App, ComposeResult


# Horizontal:
# Places widgets from left to right.
from textual.containers import Horizontal


# Textual widgets used by this application.
from textual.widgets import (
    Static,       # Displays text
    ListView,     # Displays a selectable list
    ListItem,     # One item inside ListView
    Label,        # Displays a label
    Input,        # Allows the user to type text
    Button,       # Creates a clickable button
)


class TerminalProjectManager(App):
    """
    A simple terminal-based project manager.

    Features:
    - Shows a list of projects
    - Allows you to add projects
    - Selecting a project displays its name
    - Allows you to delete the selected project
    - Press q to quit
    """

    # Textual will load CSS from this file if it exists.
    CSS_PATH = "./style.tcss"

    # --------------------------------------------------------
    # COMPOSE
    # --------------------------------------------------------
    def compose(self) -> ComposeResult:
        """
        Creates the user interface.
        """

        # Application title.
        yield Static(
            "TERMINAL PROJECT MANAGER",
            id="title"
        )

        # Main area.
        # Horizontal means the sidebar and content
        # will appear next to each other.
        with Horizontal():

            # Left sidebar containing projects.
            yield ListView(
                ListItem(Label("Website")),
                ListItem(Label("Python App")),
                ListItem(Label("CLI Tool")),
                id="sidebar",
            )

            # Right side content area.
            yield Static(
                "Select a project from the list.",
                id="content"
            )

        # Input box used when adding a project.
        yield Input(
            placeholder="Enter a new project name...",
            id="project_input"
        )

        # Add button.
        yield Button(
            "Add Project",
            id="add"
        )

        # Footer instructions.
        yield Static(
            "Enter = Add Project | q = Quit",
            id="footer"
        )

    # --------------------------------------------------------
    # LIST VIEW SELECTION
    # --------------------------------------------------------
    def on_list_view_selected(
        self,
        event: ListView.Selected,
    ) -> None:
        """
        Runs when the user selects a project.
        """

        # Get the selected ListItem.
        selected_item = event.item

        # Find the Label inside the selected ListItem.
        label = selected_item.query_one(Label)

        # Find the content area.
        content = self.query_one("#content", Static)

        # Display the selected project.
        content.update(
            f"Selected Project: {label.renderable}"
        )

    # --------------------------------------------------------
    # BUTTON EVENT
    # --------------------------------------------------------
    def on_button_pressed(
        self,
        event: Button.Pressed,
    ) -> None:
        """
        Runs when a button is pressed.
        """

        # Check whether the Add Project button was pressed.
        if event.button.id == "add":

            # Find the input box.
            project_input = self.query_one(
                "#project_input",
                Input
            )

            # Get the text entered by the user.
            project_name = project_input.value.strip()

            # Make sure the user entered something.
            if not project_name:
                self.notify(
                    "Please enter a project name.",
                    severity="warning"
                )
                return

            # Find the sidebar.
            sidebar = self.query_one(
                "#sidebar",
                ListView
            )

            # Add the new project.
            sidebar.append(
                ListItem(
                    Label(project_name)
                )
            )

            # Clear the input box.
            project_input.value = ""

            # Show a notification.
            self.notify(
                f"Added project: {project_name}"
            )

    # --------------------------------------------------------
    # KEYBOARD EVENTS
    # --------------------------------------------------------
    def on_key(self, event) -> None:
        """
        Handles keyboard shortcuts.
        """

        # q = quit
        if event.key == "q":
            self.exit()


# ------------------------------------------------------------
# START APPLICATION
# ------------------------------------------------------------

if __name__ == "__main__":
    TerminalProjectManager().run()