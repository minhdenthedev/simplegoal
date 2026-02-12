import dataclasses
from typing import List

from simplegoal.interactor.output_bound.view_goal_list_output_bound import ViewGoalListOutputBound
from simplegoal.interactor.presenter_interface.view_goal_list_presenter import ViewGoalListPresenter
from simplegoal.view.view_goal_list_view import ViewGoalListView
from simplegoal.view.view_goal_view import ViewGoalView


@dataclasses.dataclass
class ViewGoalListPresenterImpl(ViewGoalListPresenter):
    view: ViewGoalListView

    def present(self, response: ViewGoalListOutputBound):
        answers: List[ViewGoalView] = [
            ViewGoalView(
                goal.name,
                str(goal.started_at),
                str(goal.due),
                "red" if goal.is_due else "white",
                goal.number_of_steps
            )
            for goal in response.view_goal_output_bounds
        ]
        self.view.view_goal_views = answers
