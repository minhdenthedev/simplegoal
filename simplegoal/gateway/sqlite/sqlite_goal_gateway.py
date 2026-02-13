from typing import List

from simplegoal.entity.completed_goal import CompletedGoal
from simplegoal.entity.goal import Goal
from simplegoal.interactor.gateway_interface.goal_gateway import GoalGateway


class SqliteGoalGateway(GoalGateway):
    """Implementation of goal gateway using SQLite"""

    def get_all(self) -> List[Goal]:
        pass

    def save(self, goal: Goal):
        pass

    def delete(self, goal_id: str) -> Goal:
        pass

    def update(self, goal: Goal) -> None:
        pass

    def get(self, goal_id: str) -> Goal:
        pass

    def save_completed(self, goal: CompletedGoal):
        pass