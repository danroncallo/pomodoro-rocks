import time
from pynput import mouse, keyboard


class ActivityMonitor:
    def __init__(self):
        self.last_activity = time.time()
        self.mouse_listener = None
        self.keyboard_listener = None

    def _on_activity(self, *args, **kwargs):
        self.last_activity = time.time()

    def start(self):
        if self.mouse_listener is None:
            self.mouse_listener = mouse.Listener(
                on_move=self._on_activity,
                on_click=self._on_activity,
                on_scroll=self._on_activity
            )
            self.mouse_listener.start()

        if self.keyboard_listener is None:
            self.keyboard_listener = keyboard.Listener(
                on_press=self._on_activity
            )
            self.keyboard_listener.start()

    def stop(self):
        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_listener = None

        if self.keyboard_listener:
            self.keyboard_listener.stop()
            self.keyboard_listener = None

    def get_idle_time(self) -> float:
        return time.time() - self.last_activity
