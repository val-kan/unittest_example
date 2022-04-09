"""
Example of running test suite
Tests collected from two classes (all tests)
"""
import unittest
from tests.test_str_utils_slicing import TestStrUtilsSlicingParameterized as SL
from tests.test_str_utils_swap import TestStrUtilsSwapParameterized as SW

suite = unittest.TestSuite()
suite.addTests([
    unittest.TestLoader().loadTestsFromTestCase(SL),
    unittest.TestLoader().loadTestsFromTestCase(SW)
])

unittest.TextTestRunner(verbosity=2).run(suite)
