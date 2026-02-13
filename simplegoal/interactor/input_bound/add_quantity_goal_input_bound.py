import dataclasses

from simplegoal.interactor.input_bound.add_goal_input_bound import (
    AddGoalInputBound,
)


@dataclasses.dataclass
class AddQuantityGoalInputBound(AddGoalInputBound):
    target_quantity: int
