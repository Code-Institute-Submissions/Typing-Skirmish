"""A small typing game named "Typing Skirmish" using a TUI (Text User Interface)."""

from textual.app import App
from textual.widgets import Placeholder

class Game(App):
    """Class for handling game state and Textual App / TUI rendering."""

    async def on_mount(self) -> None:
        """Handle and Render Layouts."""
        await self.view.dock(Placeholder())

def main() -> None:
    """Initilize main logic and "Typing Skirmish" app."""


    Game.run()


if __name__ == "__main__":
    main()
    