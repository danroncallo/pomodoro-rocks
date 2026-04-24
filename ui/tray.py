import threading
import pystray
from PIL import Image
import os

class PomodoroTray:
    def __init__(self, on_open_chat=None, on_exit=None):
        self.on_open_chat = on_open_chat
        self.on_exit = on_exit
        self.icon = None
        self._setup_tray()

    def _setup_tray(self):
        # Load icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'icon.png')
        image = Image.open(icon_path)
        
        # Create menu
        menu = pystray.Menu(
            pystray.MenuItem("Abrir Chat", self._handle_open_chat),
            pystray.MenuItem("Salir", self._handle_exit)
        )
        
        self.icon = pystray.Icon("Pomodoro Rocks", image, "Pomodoro Rocks", menu)

    def _handle_open_chat(self, icon, item):
        if self.on_open_chat:
            self.on_open_chat()

    def _handle_exit(self, icon, item):
        if self.on_exit:
            self.on_exit()
        self.icon.stop()

    def run(self):
        """Runs the tray icon in a detached thread."""
        threading.Thread(target=self.icon.run, daemon=True).start()

    def stop(self):
        if self.icon:
            self.icon.stop()
