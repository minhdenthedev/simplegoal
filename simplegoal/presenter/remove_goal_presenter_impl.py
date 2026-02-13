import dataclasses

from simplegoal.interactor.output_bound.remove_goal_output_bound import (
    RemoveGoalOutputBound,
)
from simplegoal.interactor.presenter_interface.remove_goal_presenter import (
    RemoveGoalPresenter,
)
from simplegoal.view.remove_goal_view import RemoveGoalView


@dataclasses.dataclass
class RemoveGoalPresenterImpl(RemoveGoalPresenter):
    view: RemoveGoalView

    def present(self, response: RemoveGoalOutputBound):
        if response.succeed:
            self.view.message = "Goal removed!"
            self.view.goal_name = response.removed_goal_name
            self.view.started_at_str = str(response.removed_goal_started_at)
            self.view.text_color = "yellow"
        else:
            self.view.message = "Failed to remove goal! Please try again!"
            self.view.text_color = "red"
            self.view.goal_name = "Failed to fetch"
            self.view.started_at_str = "Failed to fetch"
