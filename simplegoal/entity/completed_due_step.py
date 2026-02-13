from dataclasses import dataclass
from datetime import datetime, timedelta

from simplegoal.entity.due_step import DueStep
from simplegoal.entity.completable import Completable


@dataclass
class CompletedDueStep(Completable):
    """Decorator for completed due step"""

    due_step: DueStep
    completed_at: datetime

    def get_completed_at(self) -> datetime:
        return self.completed_at

    def completed_duration(self) -> timedelta:
        return self.completed_at - self.due_step.started_at

    def completed_before_due(self) -> bool:
        tdelta = self.completed_at - self.due_step.due
        return tdelta.seconds <= 0

    def completed_after_due(self) -> bool:
        tdelta = self.completed_at - self.due_step.due
        return tdelta.seconds > 0
