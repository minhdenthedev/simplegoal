import dataclasses
from abc import ABC
from datetime import timedelta

from simplegoal.interactor.output_bound.add_goal_output_bound import (
    AddGoalOutputBound,
)


@dataclasses.dataclass
class AddDurationGoalOutputBound(AddGoalOutputBound):
    target_duration: timedelta
