import customtkinter as ctk

class PomodoroApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Basic configuration
        self.title("Pomodoro Rocks")
        self.overrideredirect(True)  # Borderless
        self.attributes("-topmost", True)
        
        # Initial mode
        self.set_widget_mode()

        # Dragging support
        self.bind("<Button-1>", self._start_drag)
        self.bind("<B1-Motion>", self._do_drag)

    def _start_drag(self, event):
        self._drag_x = event.x
        self._drag_y = event.y

    def _do_drag(self, event):
        x = self.winfo_x() - self._drag_x + event.x
        y = self.winfo_y() - self._drag_y + event.y
        self.geometry(f"+{x}+{y}")

    def set_widget_mode(self):
        """Small (200x60), bottom-right corner, 80% alpha, topmost."""
        width = 200
        height = 60
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate position (bottom-right with some margin)
        margin = 20
        x = screen_width - width - margin
        y = screen_height - height - margin - 40  # Extra margin for taskbar
        
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.attributes("-alpha", 0.8)
        self.attributes("-topmost", True)

    def set_break_mode(self):
        """Large (400x300), centered, 100% alpha, topmost."""
        width = 400
        height = 300
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate position (centered)
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.attributes("-alpha", 1.0)
        self.attributes("-topmost", True)

    def run(self):
        self.mainloop()
