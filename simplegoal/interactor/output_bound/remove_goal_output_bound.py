import dataclasses
from datetime import datetime


@dataclasses.dataclass
class RemoveGoalOutputBound:
    succeed: bool
    removed_goal_id: str
    removed_goal_name: str
    removed_goal_started_at: datetime
