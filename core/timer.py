from enum import Enum


class TimerState(Enum):
    IDLE = "IDLE"
    WORKING = "WORKING"
    BREAK = "BREAK"


class PomodoroTimer:
    def __init__(self, work_duration=1800, break_duration=480):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.state = TimerState.IDLE
        self.remaining = 0

    def start(self):
        if self.state == TimerState.IDLE:
            self.state = TimerState.WORKING
            self.remaining = self.work_duration

    def tick(self, seconds=1):
        if self.state == TimerState.IDLE:
            return

        self.remaining -= seconds
        if self.remaining <= 0:
            self.remaining = 0
            self.next_state()

    def next_state(self):
        if self.state == TimerState.WORKING:
            self.state = TimerState.BREAK
            self.remaining = self.break_duration
        elif self.state == TimerState.BREAK:
            self.state = TimerState.IDLE
            self.remaining = 0
        else:
            # If IDLE, maybe start? But the prompt says next_state transitions.
            # "When remaining reaches 0 during WORKING, it transitions to BREAK."
            # "When remaining reaches 0 during BREAK, it transitions to IDLE."
            pass
