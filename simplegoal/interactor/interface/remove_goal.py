from abc import ABC, abstractmethod

from simplegoal.interactor.input_bound.remove_goal_input_bound import (
    RemoveGoalInputBound,
)
from simplegoal.interactor.output_bound.remove_goal_output_bound import (
    RemoveGoalOutputBound,
)


class RemoveGoal(ABC):
    @abstractmethod
    def execute(self, request: RemoveGoalInputBound):
        pass
