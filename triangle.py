#!/usr/bin/env python3


def validate_inputs(a, b, c):
    """Validates that inputs are integers.

    Args:
      a: Length of side a
      b: Length of side b
      c: Length of side c

     Returns:
       (bool) True if all sides are integers and/or floats, False if not.
    """
    if (
        not ((isinstance(a, int)) or (isinstance(a, float)))
        or not ((isinstance(b, int)) or (isinstance(b, float)))
        or not ((isinstance(c, int)) or (isinstance(c, float)))
    ):
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
    if (a * a + b * b) == (c * c):
        type += " and Right"

    # Check that sides make a valid triangle
    if not validate_triangle(a, b, c):
        type = "NotATriangle"

    print(f"Triangle type is: {type}")
    return type


if __name__ == "__main__":
    # Examples of running the code
    classify_triangle(1, 2, 3)
    classify_triangle(10, 7, 9)
    classify_triangle(5, 5, 5)
    classify_triangle(5, 5, 8)
    classify_triangle(3, 4, 5)
    # classify_triangle(5, 5, "eight")
    # classify_triangle(5, 5)
