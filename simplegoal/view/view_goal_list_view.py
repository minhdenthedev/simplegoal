import dataclasses
from typing import List

from simplegoal.view.view_goal_view import ViewGoalView


@dataclasses.dataclass
class ViewGoalListView:
    view_goal_views: List[ViewGoalView]
