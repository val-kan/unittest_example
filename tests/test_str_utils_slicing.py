import unittest
from parameterized import parameterized
from str_utils.utils import reverse_string_slicing


class TestStrUtilsSlicingParameterized(unittest.TestCase):

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
        ("number", "120", "021")
    ])
    def test_positive_reverse_string_slicing(self, name, string, expected):
        self.assertEqual(reverse_string_slicing(string), expected)

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
    def test_negative_reverse_string_slicing(self, name, value):
        # test errors if no exception raised, or raised unexpected exception
        self.assertRaises(TypeError, reverse_string_slicing, value)

    def test_error_reverse_string_slicing_no_argument(self):
        # test errors if no exception raised, or raised unexpected exception
        with self.assertRaises(TypeError):
            reverse_string_slicing()


if __name__ == '__main__':
    unittest.main(verbosity=2)
