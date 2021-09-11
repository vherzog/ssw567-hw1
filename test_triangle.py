#!/usr/bin/env python3
from triangle import classify_triangle
import unittest


class TestTriangles(unittest.TestCase):
    def testInputQuantity(self):
        with self.assertRaises(TypeError):
            classify_triangle(1,2)

    def testInputValues(self):
        with self.assertRaises(ValueError):
            classify_triangle("one", "two", "three")
        with self.assertRaises(ValueError):
            classify_triangle(1.5, 7, 9)
            
    def testValidTriangles(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right", "3,4,5 should be right")
        self.assertEqual(
            classify_triangle(1, 1, 1), "Equilateral", "1,1,1 should be equilateral"
        )
        self.assertEqual(
            classify_triangle(5, 5, 8), "Isosceles", "5,5,8 should be isosceles"
        )
        self.assertEqual(
            classify_triangle(10, 7, 9), "Scalene", "10,7,9 should be scalene"
        )

    def testInvalidTriangles(self):
        self.assertEqual(
            classify_triangle(3, 4, 8), "NotATriangle", "3,4,8 is not a triangle"
        )


if __name__ == "__main__":
    unittest.main()
