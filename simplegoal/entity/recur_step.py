import dataclasses
from datetime import timedelta

from simplegoal.entity.step import Step


@dataclasses.dataclass
class RecurStep(Step):
    """Step with recurrence

    This class represent the step that has recurrent nature.
    For example: "Read 3 papers every day"
    :param recur_gap: the gap between recurrence.
        For example, "everyday" is equivalent to recur_gap = 1 day.
    :type recur_gap: timedelta
    """

    recur_gap: timedelta
