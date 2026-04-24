import customtkinter as ctk
from core.timer import TimerState

class PomodoroApp(ctk.CTk):
    def __init__(self, timer):
        super().__init__()
        self.timer = timer
        
        # Basic configuration
        self.title("Pomodoro Rocks")
        self.overrideredirect(True)  # Borderless
        self.attributes("-topmost", True)
        
        # Widgets
        self.timer_label = ctk.CTkLabel(self, text="00:00", font=("Arial", 24))
        self.timer_label.pack(pady=10)
        
        self.activity_label = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.done_button = ctk.CTkButton(self, text="Hecho", command=self._on_done_clicked)
        
        # Initial mode
        self.set_widget_mode()

        # Dragging support
        self.bind("<Button-1>", self._start_drag)
        self.bind("<B1-Motion>", self._do_drag)
        
        # Start update loop
        self.update_loop()

    def _on_done_clicked(self):
        if self.timer.state == TimerState.BREAK:
            self.timer.next_state()
            self.timer.start()
            self.set_widget_mode()

    def update_loop(self):
        old_state = self.timer.state
        self.timer.tick()
        new_state = self.timer.state
        
        # Update timer display
        minutes = self.timer.remaining // 60
        seconds = self.timer.remaining % 60
        self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
        
        if old_state != new_state:
            if new_state == TimerState.BREAK:
                self.set_break_mode()
                self.activity_label.configure(text="Break Activity")
            elif new_state in [TimerState.WORKING, TimerState.IDLE]:
                self.set_widget_mode()
        
        self.after(1000, self.update_loop)

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
        
        # Hide break widgets
        self.activity_label.pack_forget()
        self.done_button.pack_forget()
        
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
        
        # Show break widgets
        self.activity_label.pack(pady=10)
        self.done_button.pack(pady=10)
        
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
