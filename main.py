"""A small typing game named "Typing Skirmish" using a TUI (Text User Interface)."""

from rich.layout import Layout

from textual.app import App
from textual.widgets import Placeholder

def create_layout() -> Layout:
    """Define and create layout of application."""
    
    root = Layout(name="root")
    root.split_row(
        Layout(name="info-bar", size=6),
        Layout(name="main"),
        Layout(name="footer", size=5)
    )

    root["info-bar"].split_column(
        Layout(name="player"),
        Layout(name="middle"),
        Layout(name="opponent")
    )

    return root

class Game(App):
    """Class for handling game state and Textual App / TUI rendering."""

    async def on_mount(self) -> None:
        """Handle and Render Layouts."""
        await self.view.dock(Placeholder())

    async def on_key(self, event) -> None:
        """Handle Key Proccessing here."""
        print(event.key)

def main() -> None:
    """Initilize main logic and "Typing Skirmish" app."""


    Game.run()


if __name__ == "__main__":
    main()
