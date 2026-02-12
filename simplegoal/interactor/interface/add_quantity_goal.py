from abc import ABC, abstractmethod

from simplegoal.interactor.input_bound.add_quantity_goal_input_bound import AddQuantityGoalInputBound
from simplegoal.interactor.output_bound.add_quantity_goal_output_bound import AddQuantityGoalOutputBound


class AddQuantityGoal(ABC):
    @abstractmethod
    def execute(self,
                request: AddQuantityGoalInputBound):
        pass
