import pytest
from core.timer import PomodoroTimer, TimerState


def test_initial_state():
    timer = PomodoroTimer()
    assert timer.state == TimerState.IDLE
    assert timer.remaining == 0


def test_start_transitions_to_working():
    timer = PomodoroTimer(work_duration=10)
    timer.start()
    assert timer.state == TimerState.WORKING
    assert timer.remaining == 10


def test_working_to_break_transition():
    timer = PomodoroTimer(work_duration=10, break_duration=5)
    timer.start()
    timer.tick(10)
    assert timer.state == TimerState.BREAK
    assert timer.remaining == 5


def test_break_to_idle_transition():
    timer = PomodoroTimer(work_duration=10, break_duration=5)
    timer.start()
    timer.tick(10)  # Transition to BREAK
    assert timer.state == TimerState.BREAK
    timer.tick(5)   # Transition to IDLE
    assert timer.state == TimerState.IDLE
    assert timer.remaining == 0


def test_tick_in_idle_does_nothing():
    timer = PomodoroTimer()
    timer.tick(10)
    assert timer.state == TimerState.IDLE
    assert timer.remaining == 0


def test_timer_overshoot():
    timer = PomodoroTimer(work_duration=10, break_duration=5)
    timer.start()
    # 10s remaining in WORKING. tick(12) should transition to BREAK and have 5 - (12-10) = 3s remaining.
    timer.tick(12)
    assert timer.state == TimerState.BREAK
    assert timer.remaining == 3


def test_tick_invalid_input():
    timer = PomodoroTimer()
    with pytest.raises(ValueError, match="Seconds must be a positive number"):
        timer.tick(0)
    with pytest.raises(ValueError, match="Seconds must be a positive number"):
        timer.tick(-1)
