import time
import pytest
from core.activity import ActivityMonitor


def test_activity_monitor_idle_time():
    monitor = ActivityMonitor()
    # Initial idle time should be close to 0
    assert monitor.get_idle_time() < 0.1

    time.sleep(0.2)
    # After 0.2s, idle time should be at least 0.2s
    assert monitor.get_idle_time() >= 0.2


def test_activity_monitor_start_stop():
    monitor = ActivityMonitor()
    monitor.start()
    try:
        assert monitor.mouse_listener is not None
        assert monitor.keyboard_listener is not None
    finally:
        monitor.stop()

    assert monitor.mouse_listener is None
    assert monitor.keyboard_listener is None
