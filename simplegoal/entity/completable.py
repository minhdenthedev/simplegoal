from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Completable(ABC):
    """Interface for completable entity"""

    @abstractmethod
    def get_completed_at(self) -> datetime:
        """Return datetime when completed"""

    @abstractmethod
    def completed_duration(self) -> timedelta:
        """Return the duration (in timedelta) that it takes to be completed"""

    @abstractmethod
    def completed_before_due(self) -> bool:
        """Check whether this entity has been completed before due"""

    @abstractmethod
    def completed_after_due(self) -> bool:
        """Check whether this entity has been completed after due"""
