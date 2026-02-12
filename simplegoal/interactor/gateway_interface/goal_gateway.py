from abc import ABC, abstractmethod

from simplegoal.entity.completed_goal import CompletedGoal
from simplegoal.entity.goal import Goal


class GoalGateway(ABC):
    """Interface for basic goal gateway"""

    @abstractmethod
    def save(self, goal: Goal):
        """Insert goal"""

    @abstractmethod
    def delete(self, goal_id: str) -> Goal:
        """Delete goal"""

    @abstractmethod
    def update(self, goal: Goal) -> None:
        """Update a goal"""

    @abstractmethod
    def get(self, goal_id: str) -> Goal:
        """Get goal by id"""

    @abstractmethod
    def save_completed(self, goal: CompletedGoal):
        """Save a completed goal"""
