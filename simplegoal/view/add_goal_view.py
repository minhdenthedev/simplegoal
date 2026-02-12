import dataclasses


@dataclasses.dataclass
class AddGoalView:
    message: str
    goal_name: str
    due_str: str
    target_str: str
    text_color: str
