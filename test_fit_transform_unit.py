from one_hot_encoder import fit_transform
import unittest


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        actual = fit_transform(["Hello", "world", "Hello"])
        expected = [
            ("Hello", [0, 1]),
            ("world", [1, 0]),
            ("Hello", [0, 1])
        ]
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        actual = fit_transform('')
        expected = [("", [1])]
        self.assertEqual(actual, expected)

    def test_not_iterable(self):
        with self.assertRaises(TypeError) as context:
            fit_transform(123)
        self.assertTrue("'int' object is not iterable" in
                        str(context.exception))

    def test_without_arguments(self):
        with self.assertRaises(TypeError) as context:
            fit_transform()
        self.assertTrue("expected at least 1 arguments, got 0" in
                        str(context.exception))


if __name__ == "__main__":
    pass
