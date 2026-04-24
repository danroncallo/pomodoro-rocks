from datetime import datetime, time


class Scheduler:
    HARD_BLOCKS = [
        (time(11, 30), time(11, 45)),  # Hijo
        (time(12, 14), time(12, 29)),  # Hija
        (time(13, 0), time(14, 0)),    # Almuerzo
    ]

    def is_in_hard_block(self, dt: datetime) -> bool:
        current_time = dt.time()
        for start, end in self.HARD_BLOCKS:
            if start <= current_time < end:
                return True
        return False
