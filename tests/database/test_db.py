import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Base
from database.models import Task, Event
from datetime import datetime, timezone

# Use a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_pomodoro.db"

@pytest.fixture
def db_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

def test_create_task(db_session):
    new_task = Task(title="Test Task")
    db_session.add(new_task)
    db_session.commit()
    db_session.refresh(new_task)
    
    assert new_task.id is not None
    assert new_task.title == "Test Task"
    assert new_task.status == "pending"
    assert isinstance(new_task.created_at, datetime)

def test_create_event(db_session):
    start = datetime(2026, 4, 24, 10, 0, tzinfo=timezone.utc)
    end = datetime(2026, 4, 24, 11, 0, tzinfo=timezone.utc)
    new_event = Event(
        title="Test Event",
        start_time=start,
        end_time=end,
        is_hard_block=True
    )
    db_session.add(new_event)
    db_session.commit()
    db_session.refresh(new_event)
    
    assert new_event.id is not None
    assert new_event.title == "Test Event"
    assert new_event.is_hard_block is True
