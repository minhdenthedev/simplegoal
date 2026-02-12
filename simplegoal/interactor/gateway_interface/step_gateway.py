from abc import ABC, abstractmethod

from simplegoal.entity.completed_due_step import CompletedDueStep
from simplegoal.entity.step import Step


class StepGateway(ABC):
    """Interface for step gateway"""

    @abstractmethod
    def save(self, step: Step):
        """Insert step"""

    @abstractmethod
    def delete(self, step_id: str):
        """Delete a step"""

    @abstractmethod
    def update(self, step: Step):
        """Update a step"""

    @abstractmethod
    def get(self, step_id: str) -> Step:
        """Get a step by its ID"""

    @abstractmethod
    def save_completed(self, step: CompletedDueStep):
        """Save a due step that is completed"""
