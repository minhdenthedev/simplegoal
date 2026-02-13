import dataclasses
from datetime import datetime


@dataclasses.dataclass
class AddGoalInputBound:
    name: str
    started_at: datetime
    due: datetime
