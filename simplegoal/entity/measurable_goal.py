from abc import ABC, abstractmethod


class MeasurableGoal(ABC):
    """Interface for measurable goal"""

    @abstractmethod
    def progress(self) -> float:
        """Return the progress of this goal"""
