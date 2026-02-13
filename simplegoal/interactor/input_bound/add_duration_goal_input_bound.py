import dataclasses
from datetime import timedelta

from simplegoal.interactor.input_bound.add_goal_input_bound import (
    AddGoalInputBound,
)


@dataclasses.dataclass
class AddDurationGoalInputBound(AddGoalInputBound):
    target_duration: timedelta
