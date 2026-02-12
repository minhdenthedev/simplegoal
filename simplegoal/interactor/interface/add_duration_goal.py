from abc import ABC, abstractmethod

from simplegoal.interactor.input_bound.add_duration_goal_input_bound import AddDurationGoalInputBound
from simplegoal.interactor.output_bound.add_duration_goal_output_bound import AddDurationGoalOutputBound


class AddDurationGoal(ABC):

    @abstractmethod
    def execute(self,
                request: AddDurationGoalInputBound):
        pass
