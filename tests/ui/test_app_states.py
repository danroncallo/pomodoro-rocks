import pytest
from unittest.mock import MagicMock
from ui.app import PomodoroApp
from core.timer import TimerState

@pytest.fixture
def mock_timer():
    timer = MagicMock()
    timer.state = TimerState.WORKING
    timer.remaining = 1500
    return timer

def test_app_initialization(mock_timer):
    app = PomodoroApp(mock_timer)
    app.update()
    assert app.timer == mock_timer
    # Initial remaining is 1500 -> 25:00
    assert app.timer_label.cget("text") == "25:00"
    app.destroy()

def test_transition_to_break_mode(mock_timer):
    app = PomodoroApp(mock_timer)
    app.update()
    
    # Initial state is WORKING, geometry should be widget mode
    assert "200x60" in app.geometry()
    
    # Mock tick to transition to BREAK
    def side_effect():
        mock_timer.state = TimerState.BREAK
        mock_timer.remaining = 300
    
    mock_timer.tick.side_effect = side_effect
    
    # Call update_loop manually to trigger transition logic
    app.update_loop()
    app.update()
    
    # Check geometry for break mode (400x300)
    assert "400x300" in app.geometry()
    assert app.activity_label.cget("text") == "Break Activity"
    app.destroy()

def test_transition_to_working_mode(mock_timer):
    # Start in BREAK state
    mock_timer.state = TimerState.BREAK
    mock_timer.remaining = 300
    app = PomodoroApp(mock_timer)
    app.set_break_mode()
    app.update()
    
    assert "400x300" in app.geometry()
    
    # Mock tick to transition to WORKING
    def side_effect():
        mock_timer.state = TimerState.WORKING
        mock_timer.remaining = 1500
    
    mock_timer.tick.side_effect = side_effect
    
    app.update_loop()
    app.update()
    
    # Check geometry for widget mode (200x60)
    assert "200x60" in app.geometry()
    app.destroy()

def test_transition_to_idle_mode(mock_timer):
    # Start in BREAK state
    mock_timer.state = TimerState.BREAK
    mock_timer.remaining = 300
    app = PomodoroApp(mock_timer)
    app.set_break_mode()
    app.update()
    
    assert "400x300" in app.geometry()
    
    # Mock tick to transition to IDLE
    def side_effect():
        mock_timer.state = TimerState.IDLE
        mock_timer.remaining = 0
    
    mock_timer.tick.side_effect = side_effect
    
    app.update_loop()
    app.update()
    
    # Check geometry for widget mode (200x60)
    assert "200x60" in app.geometry()
    app.destroy()

def test_done_button_click_instant_feedback(mock_timer):
    # Start in BREAK state
    mock_timer.state = TimerState.BREAK
    mock_timer.remaining = 300
    app = PomodoroApp(mock_timer)
    app.set_break_mode()
    app.update()
    
    assert "400x300" in app.geometry()
    
    # Simulate clicking the button
    app.done_button.invoke()
    app.update()
    
    # Check that it immediately switched to widget mode
    assert "200x60" in app.geometry()
    mock_timer.next_state.assert_called_once()
    mock_timer.start.assert_called_once()
    app.destroy()
