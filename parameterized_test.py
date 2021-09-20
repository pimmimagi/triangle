import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):
    # The list of values for your tests can be defined:
    # - outside the class (global variable)
    # - as a class variable (like this)
    # - as a local variable inside the test method.
    # Use which ever is most readable.
    valid_triangles = [
            (1, 1, 1),
            (3, 4, 5),
            (3, 4, 6),
            (8, 10, 12),
            (100, 101, 102)
            ]
    invalid_triangles = [
        (21, 10, 10),
        (2, 1, 1),
        (6, 10, 4),
        (6, 20, 4),
        (6, 20, 27)
    ]
    invalid_value_triangles = [
        (1, 2, -1),
        (1, 2, 0),
        (-1, -1, -1),
        (0, 0, 0),
        (-1, 2, 2),
        (1, 0, 2),
        (1, 0, 2),
    ]

    def test_valid_triangle(self):
        for a,b,c in self.valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertTrue( is_triangle(a, b, c), msg)

    def test_not_triangle(self):
        for a, b, c in self.invalid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertFalse( is_triangle(a, b, c), msg)

    def test_invalid_argument_raises_exception(self):
        for a, b, c in self.invalid_value_triangles:
            with self.subTest():
                self.assertRaises( ValueError, is_triangle, a, b, c)
