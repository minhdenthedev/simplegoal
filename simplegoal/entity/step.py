import dataclasses


@dataclasses.dataclass
class Step:
    """Class for basic step

    :param step_id: ID of this step
    :type step_id: str
    :param name: step's description
    :type name: str
    """

    step_id: str
    name: str
