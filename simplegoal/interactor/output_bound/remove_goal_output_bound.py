import dataclasses
from abc import ABC

from simplegoal.interactor.output_bound.presenter import Presenter


@dataclasses.dataclass
class RemoveGoalOutputBound:
    removed_goal_id: str
    removed_goal_name: str
