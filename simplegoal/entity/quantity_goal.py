import dataclasses

from simplegoal.entity.goal import Goal
from simplegoal.entity.measurable_goal import MeasurableGoal


@dataclasses.dataclass
class QuantityGoal(Goal, MeasurableGoal):
    """Goal with quantity target"""

    current_quantity: int
    target_quantity: int

    def progress(self) -> float:
        return self.current_quantity / self.target_quantity
