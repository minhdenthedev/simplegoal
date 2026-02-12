import dataclasses
import uuid
from datetime import timedelta

from simplegoal.entity.duration_goal import DurationGoal
from simplegoal.entity.goal import Goal
from simplegoal.interactor.gateway_interface.goal_gateway import GoalGateway
from simplegoal.interactor.input_bound.add_duration_goal_input_bound import AddDurationGoalInputBound
from simplegoal.interactor.interface.add_duration_goal import AddDurationGoal
from simplegoal.interactor.output_bound.add_duration_goal_output_bound import AddDurationGoalOutputBound
from simplegoal.interactor.presenter_interface.add_goal_presenter import AddGoalPresenter


@dataclasses.dataclass
class AddDurationGoalImpl(AddDurationGoal):
    goal_gateway: GoalGateway
    presenter: AddGoalPresenter

    def execute(self, request: AddDurationGoalInputBound):
        goal_id = str(uuid.uuid4())
        goal = DurationGoal(
            goal_id,
            request.started_at,
            request.due,
            request.name,
            [],
            timedelta(milliseconds=0),
            request.target_duration
        )
        self.goal_gateway.save(goal)
        output_bound = AddDurationGoalOutputBound(
            goal_id, goal.name, goal.target_duration
        )
        self.presenter.present(output_bound)
