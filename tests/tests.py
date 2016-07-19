import unittest
import os

from pyArango.connection import Connection


class pythonTests(unittest.TestCase):

    def setUp(self):
        ARANGODB_ROOT_USERNAME = os.getenv('ARANGODB_ROOT_USERNAME', 'root')
        ARANGODB_ROOT_PASSWORD = os.getenv('ARANGODB_ROOT_PASSWORD', 'root')
        self.conn = Connection(username=ARANGODB_ROOT_USERNAME, password=ARANGODB_ROOT_PASSWORD)

    def tearDown(self):
        # TODO: disconnect session and delete db
        pass

    def test_create_database(self):
        self.conn.createDatabase(name = "test_db")
        self.db = self.conn["test_db"]
        # TODO: assert something


if __name__ == "__main__" :
    unittest.main()
