import dataclasses
from datetime import datetime


@dataclasses.dataclass
class AddGoalInputBound:
    name: str
    due: datetime
    