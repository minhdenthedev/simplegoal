from abc import ABC, abstractmethod


class InitGateway(ABC):
    """Interface for database initiator"""

    @abstractmethod
    def init_db(self):
        """Initiate the database"""
