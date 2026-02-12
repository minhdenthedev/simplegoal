import dataclasses
from datetime import datetime, timedelta

from simplegoal.entity.completable import Completable
from simplegoal.entity.goal import Goal


@dataclasses.dataclass
class CompletedGoal(Completable):
    """Decorator for completed goals"""

    goal: Goal
    completed_at: datetime

    def get_completed_at(self) -> datetime:
        return self.completed_at

    def completed_duration(self) -> timedelta:
        return self.completed_at - self.goal.started_at

    def completed_before_due(self) -> bool:
        return (self.completed_at - self.goal.due).total_seconds() <= 0

    def completed_after_due(self) -> bool:
        return (self.completed_at - self.goal.due).total_seconds() > 0
