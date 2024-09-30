import nicegui
from nicegui import native, ui

ui.label("Hello from PyInstaller")


if __name__ == "__main__":
    ui.run(reload=False, port=native.find_open_port())

    input("Press Enter to exit...")
