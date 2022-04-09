"""
unittest example with passed parameter
To run from root: python tests/test_param.py qa
"""
import unittest
import sys

ENVIRONMENTS = "qa", "staging", "prod"
ENV_STR = str(ENVIRONMENTS)[1:-1]


class TestExample(unittest.TestCase):
    ENV = None

    def setUp(self) -> None:
        self.env = TestExample.ENV
        print(f"\nSetting up for test in {self.env} ...")

    def tearDown(self) -> None:
        print(f"Cleaning up after test in {self.env} ...")

    def test_1(self):
        print(f"Test test_1 running in {self.env} ...")

    def test_2(self):
        print(f"Test test_2 running in {self.env} ...")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestExample.ENV = sys.argv.pop()
        if TestExample.ENV.lower() not in ENVIRONMENTS:
            sys.exit(f"ERROR: Unknown '{TestExample.ENV}' environment! Must be one of: {ENV_STR}")
    else:
        sys.exit(f"ERROR: Environment variable is required to run tests! Examples: {ENV_STR}")
    unittest.main()
