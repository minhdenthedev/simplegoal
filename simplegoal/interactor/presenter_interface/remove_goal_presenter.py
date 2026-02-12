from abc import ABC, abstractmethod

from simplegoal.interactor.output_bound.remove_goal_output_bound import RemoveGoalOutputBound


class RemoveGoalPresenter(ABC):
    @abstractmethod
    def present(self, response: RemoveGoalOutputBound):
        pass
