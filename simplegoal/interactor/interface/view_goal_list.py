from abc import ABC, abstractmethod

from simplegoal.interactor.output_bound.view_goal_list_output_bound import ViewGoalListOutputBound


class ViewGoalList(ABC):
    @abstractmethod
    def execute(self):
        pass
