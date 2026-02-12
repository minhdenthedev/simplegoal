import dataclasses
from abc import ABC

from simplegoal.interactor.output_bound.add_goal_output_bound import AddGoalOutputBound


@dataclasses.dataclass
class AddQuantityGoalOutputBound(AddGoalOutputBound):
    target_quantity: int
