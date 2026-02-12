import dataclasses


@dataclasses.dataclass
class ViewGoalView:
    name: str
    started_at: str
    due: str
    color: str
    number_of_step: int
