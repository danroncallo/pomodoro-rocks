import time
from unittest.mock import patch
import pytest
from core.activity import ActivityMonitor


def test_activity_monitor_idle_time():
    with patch("time.time") as mock_time:
        mock_time.return_value = 1000.0
        monitor = ActivityMonitor()
        
        # Initial idle time should be 0
        assert monitor.get_idle_time() == 0.0

        # Advance time by 5 seconds
        mock_time.return_value = 1005.0
        assert monitor.get_idle_time() == 5.0


def test_activity_monitor_reset_on_activity():
    with patch("time.time") as mock_time:
        mock_time.return_value = 1000.0
        monitor = ActivityMonitor()
        
        # Advance time
        mock_time.return_value = 1010.0
        assert monitor.get_idle_time() == 10.0
        
        # Trigger activity
        mock_time.return_value = 1012.0
        monitor._on_activity()
        
        # Idle time should be reset based on the time of activity
        assert monitor.last_activity == 1012.0
        assert monitor.get_idle_time() == 0.0


def test_activity_monitor_start_stop():
    monitor = ActivityMonitor()
    with patch("pynput.mouse.Listener") as mock_mouse, \
         patch("pynput.keyboard.Listener") as mock_keyboard:
        
        monitor.start()
        assert monitor.mouse_listener is not None
        assert monitor.keyboard_listener is not None
        mock_mouse.assert_called_once()
        mock_keyboard.assert_called_once()
        
        monitor.stop()
        assert monitor.mouse_listener is None
        assert monitor.keyboard_listener is None


def test_activity_monitor_context_manager():
    with patch("pynput.mouse.Listener"), \
         patch("pynput.keyboard.Listener"):
        
        with ActivityMonitor() as monitor:
            assert monitor.mouse_listener is not None
            assert monitor.keyboard_listener is not None
            
        assert monitor.mouse_listener is None
        assert monitor.keyboard_listener is None
