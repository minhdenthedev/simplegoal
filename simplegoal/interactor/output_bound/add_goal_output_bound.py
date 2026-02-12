import dataclasses
from datetime import datetime


@dataclasses.dataclass
class AddGoalOutputBound:
    added_goal_id: str
    added_goal_name: str
    added_goal_due: datetime
    added_goal_started_at: datetime
