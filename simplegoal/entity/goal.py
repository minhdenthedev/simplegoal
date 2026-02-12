import dataclasses
from datetime import datetime
from typing import List

from simplegoal.entity.step import Step
from simplegoal.entity.timebound import TimeBound


@dataclasses.dataclass
class Goal(TimeBound):
    """Class for basic goal"""

    goal_id: str
    started_at: datetime
    due: datetime
    name: str
    steps: List[Step]

    def add_steps(self, steps: List[Step]):
        """Add a list of steps to this goal"""
        self.steps.extend(steps)

    def remove_steps(self, step_ids: List[str]):
        """Remove a list of steps from this goal"""
        for step in self.steps:
            if step.step_id in step_ids:
                self.steps.remove(step)

    def get_steps(self) -> List[Step]:
        """Return list of steps in this goal"""
        return self.steps

    def num_steps(self) -> int:
        """Return number of steps"""
        return len(self.steps)

    def is_due(self) -> bool:
        return (datetime.now() - self.due).total_seconds() > 0

    def get_due(self) -> datetime:
        return self.due

    def get_start(self) -> datetime:
        return self.started_at
