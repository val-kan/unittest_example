"""
unittest example with setUpClass and tearDownClass
"""
import unittest


class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nSetting up before all tests ...")
        cls.db = DummyDB("10.10.10.10", "qe1", "0123")

    @classmethod
    def tearDownClass(cls):
        print("\nCleaning up after all tests ...")
        cls.db.disconnect_from_db()

    def setUp(self):
        print(f"\nSetting up for test ...")
        self.db.create()

    def tearDown(self):
        print("Cleaning up after test ...")
        self.db.delete()

    def test_1(self):
        print("Test test_1 started")
        print("Do something")
        self.db.get()
        print("Test test_1 finished")

    def test_2(self):
        print("Test test_2 started")
        print("Do something")
        self.db.get()
        print("Test test_2 finished")


class DummyDB:
    def __init__(self, host, username, password):
        print(f"Connecting to db: {host}, {username}, {password}")

    def get(self):
        print("Retrieving data from db")

    def delete(self):
        print("Deleting data from db")

    def create(self):
        print("Creating data in db")

    def disconnect_from_db(self):
        print("Closing connection to db")


if __name__ == '__main__':
    unittest.main()
