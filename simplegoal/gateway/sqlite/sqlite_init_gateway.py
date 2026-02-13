import dataclasses
from pathlib import Path
import sqlite3
from importlib import resources

from simplegoal.interactor.gateway_interface.init_gateway import InitGateway


@dataclasses.dataclass
class SqliteInitGateway(InitGateway):
    """Implementation of init gateway using SQLite"""

    data_path: Path

    def init_db(self):
        conn = sqlite3.connect(self.data_path)
        with resources.files("simplegoal.resources.sqlite").joinpath(
            "init_db.sql"
        ).open() as f:
            sql = f.read()

        conn.executescript(sql)
        conn.commit()
        conn.close()
