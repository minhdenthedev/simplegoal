import dataclasses
from datetime import datetime


@dataclasses.dataclass
class ViewGoalOutputBound:
    goal_id: str
    name: str
    started_at: datetime
    due: datetime
    number_of_steps: int
    is_due: bool
