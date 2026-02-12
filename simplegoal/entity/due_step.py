import dataclasses
from datetime import datetime

from simplegoal.entity.step import Step
from simplegoal.entity.timebound import TimeBound


@dataclasses.dataclass
class DueStep(Step, TimeBound):
    """Class for step with due date and time

    This class represent a step that has due date and time.
    For example: "Finish ML tutorial by 2pm Friday"
    :param started_at: when the step is created
    :type started_at: datetime
    :param due: due date and time for this step
    :type due: datetime
    """

    started_at: datetime
    due: datetime

    def is_due(self) -> bool:
        return (datetime.now() - self.due).total_seconds() > 0

    def get_due(self) -> datetime:
        return self.due

    def get_start(self) -> datetime:
        return self.started_at
