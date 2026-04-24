import sys
import os
import time

# Add current directory to path to import ui
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.app import PomodoroApp
from ui.tray import PomodoroTray

def main():
    print("Starting Pomodoro Rocks UI Verification...")
    
    app = PomodoroApp()
    
    def on_open_chat():
        print("Tray: Abrir Chat clicked")
        app.set_break_mode()
        app.deiconify()
        app.focus_force()

    def on_exit():
        print("Tray: Salir clicked")
        app.quit()
        sys.exit(0)

    tray = PomodoroTray(on_open_chat=on_open_chat, on_exit=on_exit)
    tray.run()
    
    print("UI is running. Check the system tray and the bottom-right corner.")
    print("Click 'Abrir Chat' in the tray to center the window and make it larger.")
    print("Click 'Salir' in the tray to exit.")
    
    app.run()

if __name__ == "__main__":
    main()
