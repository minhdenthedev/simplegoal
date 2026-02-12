import dataclasses
from datetime import datetime

from simplegoal.interactor.gateway_interface.goal_gateway import GoalGateway
from simplegoal.interactor.input_bound.remove_goal_input_bound import RemoveGoalInputBound
from simplegoal.interactor.interface.remove_goal import RemoveGoal
from simplegoal.interactor.output_bound.remove_goal_output_bound import RemoveGoalOutputBound
from simplegoal.interactor.presenter_interface.remove_goal_presenter import RemoveGoalPresenter


@dataclasses.dataclass
class RemoveGoalImpl(RemoveGoal):
    goal_gateway: GoalGateway
    presenter: RemoveGoalPresenter

    def execute(self, request: RemoveGoalInputBound):
        goal_id = request.goal_id
        try:
            removed_goal = self.goal_gateway.delete(goal_id)
            output_bound = RemoveGoalOutputBound(
                True, goal_id, removed_goal.name, removed_goal.started_at
            )
        except Exception as e:
            output_bound = RemoveGoalOutputBound(
                False, goal_id, "", datetime(0, 0, 0)
            )
        self.presenter.present(output_bound)
