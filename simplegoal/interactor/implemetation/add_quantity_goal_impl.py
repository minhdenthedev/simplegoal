import dataclasses
import uuid

from simplegoal.entity.quantity_goal import QuantityGoal
from simplegoal.interactor.gateway_interface.goal_gateway import GoalGateway
from simplegoal.interactor.input_bound.add_quantity_goal_input_bound import (
    AddQuantityGoalInputBound,
)
from simplegoal.interactor.interface.add_quantity_goal import AddQuantityGoal
from simplegoal.interactor.output_bound.add_quantity_goal_output_bound import (
    AddQuantityGoalOutputBound,
)
from simplegoal.interactor.presenter_interface.add_goal_presenter import (
    AddGoalPresenter,
)


@dataclasses.dataclass
class AddQuantityGoalImpl(AddQuantityGoal):
    goal_gateway: GoalGateway
    presenter: AddGoalPresenter

    def execute(self, request: AddQuantityGoalInputBound):
        goal_id = str(uuid.uuid4())
        goal = QuantityGoal(
            goal_id,
            request.started_at,
            request.due,
            request.name,
            [],
            0,
            request.target_quantity,
        )
        self.goal_gateway.save(goal)
        output_bound = AddQuantityGoalOutputBound(
            goal_id,
            goal.name,
            request.due,
            request.started_at,
            goal.target_quantity,
        )
        self.presenter.present(output_bound)
