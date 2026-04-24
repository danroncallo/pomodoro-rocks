from datetime import datetime
from core.scheduler import Scheduler


def test_is_in_hard_block_hijo():
    scheduler = Scheduler()
    # 11:35 AM is inside 11:30 - 11:45
    dt = datetime(2024, 1, 1, 11, 35)
    assert scheduler.is_in_hard_block(dt) is True


def test_is_not_in_hard_block_morning():
    scheduler = Scheduler()
    # 10:00 AM is NOT inside any block
    dt = datetime(2024, 1, 1, 10, 0)
    assert scheduler.is_in_hard_block(dt) is False


def test_is_in_hard_block_almuerzo():
    scheduler = Scheduler()
    # 1:30 PM is inside 1:00 - 2:00
    dt = datetime(2024, 1, 1, 13, 30)
    assert scheduler.is_in_hard_block(dt) is True


def test_is_in_hard_block_hija():
    scheduler = Scheduler()
    # 12:20 PM is inside 12:14 - 12:29
    dt = datetime(2024, 1, 1, 12, 20)
    assert scheduler.is_in_hard_block(dt) is True


def test_boundary_conditions():
    scheduler = Scheduler()
    # Exactly at start of block
    assert scheduler.is_in_hard_block(datetime(2024, 1, 1, 11, 30)) is True
    # Exactly at end of block (exclusive)
    assert scheduler.is_in_hard_block(datetime(2024, 1, 1, 11, 45)) is False
