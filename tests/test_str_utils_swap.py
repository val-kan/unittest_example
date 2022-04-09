import unittest
from parameterized import parameterized
from str_utils.utils import reverse_string_swap


class TestStrUtilsSwapParameterized(unittest.TestCase):
    """All tests have detailed error message"""

    @parameterized.expand([
        ("lower_case", "something", "gnihtemos"),
        ("upper_case", "SOMETHING", "GNIHTEMOS"),
        ("capitalized", "Something", "gnihtemoS"),
        ("text",
         "Python testing framework provides the following assertion methods to check that exceptions are raised.",
         ".desiar era snoitpecxe taht kcehc ot sdohtem noitressa gniwollof eht sedivorp krowemarf gnitset nohtyP"),
        ("empty", "", ""),
        ("space", " ", " "),
        ("space_before", " something", "gnihtemos "),
        ("space_after", "something ", " gnihtemos"),
        ("character", "a", "a"),
        ("number", "120", "201")
    ])
    def test_positive_reverse_string_swap(self, name, string, expected):
        self.assertEqual(reverse_string_swap(string), expected,
                         f"{reverse_string_swap.__name__}('{string}') "
                         f"returned '{reverse_string_swap(string)}', expected: '{expected}'")

    @parameterized.expand([
        ("boolean", True),
        ("none", None),
        ("number", 1),
        ("float", 0.1),
        ("list", [0, 1]),
        ("tuple", (0, 1)),
        ("set", {0, 1}),
        ("dict", {0: 0, 1: 1}),
        ("object", unittest.TestCase)
    ])
    def test_negative_reverse_string_swap(self, name, value):
        # test fails if no exception raised, or raised unexpected exception
        e = None
        try:
            reverse_string_swap(value)
        except Exception as e:
            self.assertIsInstance(e, TypeError,
                                  f"{reverse_string_swap.__name__}({value}) raised {e.__class__}, expected TypeError")
        else:
            if e is None:
                self.fail(f"{reverse_string_swap.__name__}({value}) did not raise TypeError")

    def test_error_reverse_string_swap_no_argument(self):
        # test fails if no exception raised, or raised unexpected exception
        e = None
        try:
            reverse_string_swap()
        except Exception as e:
            self.assertIsInstance(e, TypeError,
                                  f"{reverse_string_swap.__name__}() raised {e.__class__}, expected TypeError")
        else:
            if e is None:
                self.fail(f"{reverse_string_swap.__name__}() did not raise TypeError")


if __name__ == '__main__':
    unittest.main(verbosity=2)
