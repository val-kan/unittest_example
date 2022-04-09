"""
Example of running test suite
Tests collected from two classes based on passed parameter
IMPORTANT: Note that tests in classes named in a specific way
To run from root dir
 - for positive: python suites/test_suite_param.py positive
 - for negative: python suites/test_suite_param.py negative
 - for error: python suites/test_suite_param.py error
 - for all: python suites/test_suite_param.py
"""
import unittest
import sys

tests_location = "tests"
test_types = ("positive", "negative", "error")


def get_suite(test_type=""):
    loader = unittest.TestLoader()
    if test_type in test_types:
        loader.testMethodPrefix = f"test_{test_type}"
    return loader.discover(tests_location)


if len(sys.argv) > 1:
    suite = get_suite(sys.argv[1])
else:
    suite = get_suite()

unittest.TextTestRunner(verbosity=2).run(suite)
