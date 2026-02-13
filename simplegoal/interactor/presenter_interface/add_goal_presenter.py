from abc import ABC, abstractmethod

from simplegoal.interactor.output_bound.add_goal_output_bound import (
    AddGoalOutputBound,
)


class AddGoalPresenter(ABC):
    @abstractmethod
    def present(self, response: AddGoalOutputBound):
        pass
