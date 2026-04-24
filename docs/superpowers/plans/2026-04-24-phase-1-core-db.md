# Pomodoro Rocks - Phase 1: Core & Database Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish the foundational backend of Pomodoro Rocks, including database persistence, the Pomodoro state machine, activity monitoring, and hard-break scheduling.

**Architecture:** A modular backend where a SQLite database tracks state, a `Timer` class manages the Pomodoro logic, and a `Scheduler` handles fixed daily constraints. Activity monitoring runs as a background thread.

**Tech Stack:** Python 3.11, SQLite, SQLAlchemy, pynput, pytest.

---

### Task 1: Environment and Dependencies

**Files:**
- Create: `requirements.txt`

- [ ] **Step 1: Create requirements.txt**

```text
sqlalchemy
pynput
win11toast
google-generativeai
openai
requests
customtkinter
pystray
pytest
pytest-asyncio
```

- [ ] **Step 2: Commit**

```bash
git add requirements.txt
git commit -m "chore: initial dependencies"
```

---

### Task 2: Database Layer Setup

**Files:**
- Create: `database/models.py`
- Create: `database/database.py`
- Test: `tests/database/test_db.py`

- [ ] **Step 1: Write database connection logic**

Create `database/database.py`:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./pomodoro_rocks.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

- [ ] **Step 2: Define Models**

Create `database/models.py`:
```python
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base
import datetime

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String, default="pending") # pending, completed
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    is_hard_block = Column(Boolean, default=False)
```

- [ ] **Step 3: Write test to verify DB creation**

Create `tests/database/test_db.py`:
```python
from database.database import Base, engine, SessionLocal
from database.models import Task

def test_db_creation():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    new_task = Task(title="Test Task")
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    assert new_task.id is not None
    db.close()
```

- [ ] **Step 4: Run test**

Run: `pytest tests/database/test_db.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add database/ tests/database/
git commit -m "feat: database layer with task model"
```

---

### Task 3: Pomodoro Timer Engine

**Files:**
- Create: `core/timer.py`
- Test: `tests/core/test_timer.py`

- [ ] **Step 1: Write the Timer state machine test**

Create `tests/core/test_timer.py`:
```python
from core.timer import PomodoroTimer

def test_timer_initial_state():
    timer = PomodoroTimer(work_min=30, break_min=8)
    assert timer.state == "IDLE"

def test_timer_start():
    timer = PomodoroTimer(work_min=30, break_min=8)
    timer.start()
    assert timer.state == "WORKING"
```

- [ ] **Step 2: Implement minimal PomodoroTimer**

Create `core/timer.py`:
```python
class PomodoroTimer:
    def __init__(self, work_min=30, break_min=8):
        self.work_min = work_min
        self.break_min = break_min
        self.state = "IDLE" # IDLE, WORKING, BREAK, PAUSED

    def start(self):
        self.state = "WORKING"
```

- [ ] **Step 3: Run test**

Run: `pytest tests/core/test_timer.py`
Expected: PASS

- [ ] **Step 4: Add tick and transition logic to test**

Modify `tests/core/test_timer.py`:
```python
def test_timer_transition_to_break():
    timer = PomodoroTimer(work_min=0.01, break_min=8) # very short for testing
    timer.start()
    timer.tick(seconds=1) # simulate time passing
    assert timer.state == "BREAK"
```

- [ ] **Step 5: Implement tick logic**

Modify `core/timer.py`:
```python
class PomodoroTimer:
    def __init__(self, work_min=30, break_min=8):
        self.work_min = work_min * 60
        self.break_min = break_min * 60
        self.remaining = self.work_min
        self.state = "IDLE"

    def start(self):
        self.state = "WORKING"
        self.remaining = self.work_min

    def tick(self, seconds=1):
        if self.state in ["WORKING", "BREAK"]:
            self.remaining -= seconds
            if self.remaining <= 0:
                self.next_state()

    def next_state(self):
        if self.state == "WORKING":
            self.state = "BREAK"
            self.remaining = self.break_min
        elif self.state == "BREAK":
            self.state = "IDLE"
            self.remaining = 0
```

- [ ] **Step 6: Run tests**

Run: `pytest tests/core/test_timer.py`
Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add core/timer.py tests/core/test_timer.py
git commit -m "feat: pomodoro timer engine"
```

---

### Task 4: Scheduler for Hard Blocks

**Files:**
- Create: `core/scheduler.py`
- Test: `tests/core/test_scheduler.py`

- [ ] **Step 1: Write test for hard block detection**

Create `tests/core/test_scheduler.py`:
```python
from core.scheduler import Scheduler
from datetime import datetime, time

def test_is_hard_block_time():
    sched = Scheduler()
    # 11:35 AM is inside the 11:30 - 11:45 block
    test_time = datetime.combine(datetime.today(), time(11, 35))
    assert sched.is_in_hard_block(test_time) is True

    # 10:00 AM is not
    test_time = datetime.combine(datetime.today(), time(10, 0))
    assert sched.is_in_hard_block(test_time) is False
```

- [ ] **Step 2: Implement Scheduler with fixed blocks**

Create `core/scheduler.py`:
```python
from datetime import time

class Scheduler:
    HARD_BLOCKS = [
        (time(11, 30), time(11, 45)), # Hijo
        (time(12, 14), time(12, 29)), # Hija
        (time(13, 0), time(14, 0)),   # Almuerzo
    ]

    def is_in_hard_block(self, dt):
        current_time = dt.time()
        for start, end in self.HARD_BLOCKS:
            if start <= current_time <= end:
                return True
        return False
```

- [ ] **Step 3: Run test**

Run: `pytest tests/core/test_scheduler.py`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add core/scheduler.py tests/core/test_scheduler.py
git commit -m "feat: scheduler with fixed hard blocks"
```

---

### Task 5: Activity Monitor

**Files:**
- Create: `core/activity.py`
- Test: `tests/core/test_activity.py`

- [ ] **Step 1: Implement Activity Monitor using pynput**

Create `core/activity.py`:
```python
from pynput import mouse, keyboard
import time
import threading

class ActivityMonitor:
    def __init__(self):
        self.last_activity = time.time()
        self._stop_event = threading.Event()

    def _on_activity(self, *args):
        self.last_activity = time.time()

    def start(self):
        self.mouse_listener = mouse.Listener(on_move=self._on_activity, on_click=self._on_activity, on_scroll=self._on_activity)
        self.kb_listener = keyboard.Listener(on_press=self._on_activity)
        self.mouse_listener.start()
        self.kb_listener.start()

    def stop(self):
        self.mouse_listener.stop()
        self.kb_listener.stop()

    def get_idle_time(self):
        return time.time() - self.last_activity
```

- [ ] **Step 2: Write basic test for ActivityMonitor**

Create `tests/core/test_activity.py`:
```python
from core.activity import ActivityMonitor
import time

def test_activity_initial_idle():
    monitor = ActivityMonitor()
    time.sleep(0.1)
    assert monitor.get_idle_time() > 0
```

- [ ] **Step 3: Run test**

Run: `pytest tests/core/test_activity.py`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add core/activity.py tests/core/test_activity.py
git commit -m "feat: activity monitor using pynput"
```
