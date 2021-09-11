#!/usr/bin/env python3
from math import sqrt


def validate_inputs(a, b, c):
    """Validates that inputs are integers.

    Args:
      a: Length of side a
      b: Length of side b
      c: Length of side c

     Returns:
       (bool) True if all sides are integers and/or floats, False if not.
    """
    if not ((isinstance(a, int)) or (isinstance(a, float))):
        return False
    elif not ((isinstance(b, int)) or (isinstance(b, float))):
        return False
    elif not ((isinstance(c, int)) or (isinstance(c, float))):
        return False
    else:
        return True


def validate_triangle(a, b, c):
    """Validates that the side lengths make a triangle.

    Args:
      a: Length of side a
      b: Length of side b
      c: Length of side c

    Returns:
      (bool) True if valid triangle, False if invalid triangle.
    """
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False


def classify_triangle(a, b, c):
    """Classifies the type of triangle given
    side lengths.

    Args:
      a: Length of side a
      b: Length of side b
      c: Length of side c

    Returns:
      (str) The type of triangle
    """
    type = "Unknown"

    # Validate inputs
    if not validate_inputs(a, b, c):
        raise ValueError("Inputs not valid")

    # Classify triangle type
    if a == b and b == c:
        type = "Equilateral"
    elif a == b or b == c or a == c:
        type = "Isosceles"
    elif a != b and b != c and a != c:
        type = "Scalene"
    if round((a ** 2) + (b ** 2), 4) == round((c ** 2), 4):
        type += " and Right"

    # Check that sides make a valid triangle
    if not validate_triangle(a, b, c):
        type = "NotATriangle"

    return type


if __name__ == "__main__":
    # Examples of running the code
    print(classify_triangle(1, 2, 3))
    print(classify_triangle(10, 7, 9))
    print(classify_triangle(5, 5, 5))
    print(classify_triangle(5, 5, 8))
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(1, 1, sqrt(2)))
    # print(classify_triangle(5, 5, "eight"))
    # print(classify_triangle(5, 5))
