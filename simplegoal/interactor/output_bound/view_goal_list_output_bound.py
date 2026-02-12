import dataclasses
from abc import ABC
from typing import List

from simplegoal.interactor.output_bound.presenter import Presenter
from simplegoal.interactor.output_bound.view_goal_output_bound import ViewGoalOutputBound


@dataclasses.dataclass
class ViewGoalListOutputBound:
    view_goal_output_bounds: List[ViewGoalOutputBound]
