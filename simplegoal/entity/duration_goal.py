import dataclasses
from datetime import timedelta

from simplegoal.entity.goal import Goal
from simplegoal.entity.measurable_goal import MeasurableGoal


@dataclasses.dataclass
class DurationGoal(Goal, MeasurableGoal):
    """Goal with duration target"""

    current_duration: timedelta
    target_duration: timedelta

    def progress(self) -> float:
        return self.current_duration / self.target_duration
