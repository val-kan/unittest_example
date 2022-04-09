"""
Example of running test suite and generating single html report
Test suite made from collected tests from two files
To run from root: python tests/test_suite_report.py
"""
import unittest
import HtmlTestRunner
from tests.test_str_utils_slicing import TestStrUtilsSlicingParameterized as SL
from tests.test_str_utils_swap import TestStrUtilsSwapParameterized as SW

REPORT_LOCATION = "reports"
REPORT_NAME = "suite_report_demo"
REPORT_TITLE = "TestResults for reverse string test suite"

# Suite of TestCases
test_suite = unittest.TestSuite()
test_suite.addTests([
    unittest.TestLoader().loadTestsFromTestCase(SL),
    unittest.TestLoader().loadTestsFromTestCase(SW)
])

# Invoke TestRunner
runner = HtmlTestRunner.HTMLTestRunner(
    output=REPORT_LOCATION,
    report_name=REPORT_NAME,
    report_title=REPORT_TITLE,
    combine_reports=True)
runner.run(test_suite)
