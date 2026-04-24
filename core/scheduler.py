from datetime import datetime, time
from typing import List, Tuple, Optional


class Scheduler:
    """
    Handles scheduling logic, specifically identifying 'hard blocks' where work is not allowed.
    """

    def __init__(self, hard_blocks: Optional[List[Tuple[time, time]]] = None):
        """
        Initializes the Scheduler with a list of hard blocks.

        Args:
            hard_blocks: A list of (start, end) time tuples. 
                         Defaults to predefined blocks if None.
        """
        if hard_blocks is None:
            self.hard_blocks = [
                (time(11, 30), time(11, 45)),  # Hijo
                (time(12, 14), time(12, 29)),  # Hija
                (time(13, 0), time(14, 0)),    # Almuerzo
            ]
        else:
            self.hard_blocks = hard_blocks

    def is_in_hard_block(self, dt: datetime) -> bool:
        """
        Checks if a given datetime falls within any of the hard blocks.

        The start time of a block is inclusive, and the end time is exclusive.
        The input datetime is expected to be in the same timezone as the blocks.

        Args:
            dt: The datetime to check.

        Returns:
            True if dt is within a hard block, False otherwise.
        """
        current_time = dt.time()
        for start, end in self.hard_blocks:
            if start <= current_time < end:
                return True
        return False
