import dataclasses


@dataclasses.dataclass
class RemoveGoalView:
    message: str
    goal_name: str
    started_at_str: str
    text_color: str
