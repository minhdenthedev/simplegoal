import tempfile
import unittest
from pathlib import Path

from simplegoal.gateway.sqlite.sqlite_init_gateway import SqliteInitGateway


class TestInitDB(unittest.TestCase):
    def test_init_db(self):
        temp = tempfile.NamedTemporaryFile()
        path = Path(temp.name)
        init_gateway = SqliteInitGateway(path)
        init_gateway.init_db()


if __name__ == '__main__':
    unittest.main()
