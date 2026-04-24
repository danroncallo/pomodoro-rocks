import sys
from core.activity import ActivityMonitor
from core.timer import PomodoroTimer
from ui.app import PomodoroApp
from ui.tray import PomodoroTray

def setup_autostart():
    """Placeholder for autostart configuration."""
    print("Setup Autostart: To enable start with Windows, add a registry key to "
          "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run "
          "or a shortcut to the Startup folder.")

def main():
    # Initialize core components
    activity_monitor = ActivityMonitor()
    timer = PomodoroTimer()
    
    # Initialize UI components
    app = PomodoroApp(timer)
    
    def on_exit_callback():
        """Handle exit from tray icon."""
        app.quit()

    tray = PomodoroTray(
        on_show_clicked=lambda: app.after(0, lambda: (app.deiconify(), app.focus_force())),
        on_exit=on_exit_callback
    )
    
    # Start background processes
    setup_autostart()
    activity_monitor.start()
    tray.run()
    
    # Start main application loop
    try:
        app.run()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        # Ensure cleanup on exit
        activity_monitor.stop()
        tray.stop()

if __name__ == "__main__":
    main()
