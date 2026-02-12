from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class TimeBound(ABC):
    """Interface for entity with time boundaries"""

    @abstractmethod
    def is_due(self) -> bool:
        """Check if current time has exceed the due"""

    @abstractmethod
    def get_due(self) -> datetime:
        """Get the due datetime"""

    @abstractmethod
    def get_start(self) -> datetime:
        """Get the start datetime"""

    def estimate_duration(self) -> timedelta:
        return self.get_due() - self.get_start()
