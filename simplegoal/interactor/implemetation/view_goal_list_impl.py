import dataclasses
from typing import List

from simplegoal.interactor.gateway_interface.goal_gateway import GoalGateway
from simplegoal.interactor.interface.view_goal_list import ViewGoalList
from simplegoal.interactor.output_bound.view_goal_list_output_bound import (
    ViewGoalListOutputBound,
)
from simplegoal.interactor.output_bound.view_goal_output_bound import (
    ViewGoalOutputBound,
)
from simplegoal.interactor.presenter_interface\
    .view_goal_list_presenter import (
    ViewGoalListPresenter,
)


@dataclasses.dataclass
class ViewGoalListImpl(ViewGoalList):
    goal_gateway: GoalGateway
    presenter: ViewGoalListPresenter

    def execute(self):
        goals = self.goal_gateway.get_all()
        answers: List[ViewGoalOutputBound] = [
            ViewGoalOutputBound(
                goal.goal_id,
                goal.name,
                goal.started_at,
                goal.due,
                goal.num_steps(),
                goal.is_due(),
            )
            for goal in goals
        ]
        output_bound = ViewGoalListOutputBound(answers)
        self.presenter.present(output_bound)
