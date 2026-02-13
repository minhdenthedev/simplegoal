import dataclasses

from simplegoal.interactor.output_bound.add_goal_output_bound import (
    AddGoalOutputBound,
)
from simplegoal.interactor.presenter_interface.add_goal_presenter import (
    AddGoalPresenter,
)
from simplegoal.view.add_goal_view import AddGoalView


@dataclasses.dataclass
class AddGoalPresenterImpl(AddGoalPresenter):
    view: AddGoalView

    def present(self, response: AddGoalOutputBound):
        self.view.goal_name = response.added_goal_name
        self.view.due_str = str(response.added_goal_due)
        if response.succeed:
            self.view.message = "Goal added successfully!"
            self.view.text_color = "green"
        else:
            self.view.message = "Failed to add goal. Please try again!"
            self.view.text_color = "red"
