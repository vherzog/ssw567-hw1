# SSW567 HW01
## Source code
Python source code lives in [triangle.py](./triangle.py).

## Test code
Python test code lives in [test_triangle.py](./test_triangle.py).
```
python -m unittest -v
```

## Acceptance Criteria
1. Function takes 3 inputs.
2. Inputs represent the sides of a triangle.
3. Function returns a string.
4. Function returns whether triangle is `scalene`, `isosceles`, or `equilateral` and whether triangle is `right`.

## Assumptions (Missing Requirements)
* Input types can be type `int` or `float`.
* If sides do not equal a valid triangle, output `NotATriangle`.
* Output string should capitalize only the first letter.
* If sides make a `right` triangle, function returns `"<type> and Right"`
* If requirements are not met, function raises a `ValueError`.
* `Right` triangles are calculated with precision to the fourth decimal.

## Challenges
I had difficulty testing for the case of `Isosceles and Right`. This would be triangles with sides of value `X`, `X`, `X*sqrt(2)`. Without rounding to a specific decimal, the `classify_triangle` function would not classify those side lengths as a `Right` triangle, only `Isosceles`. When I debugged my code a bit, I found that python calculates `sqrt(2) * sqrt(2)` as `2.0000000000000004`, rather than `2`. For this reason, I added an assumption that `Right` triangles would be calculated with precision to the fourth decimal.

## Testing Complete
I determined my testing was considered `"Complete"` when my test cases met the provided acceptance criteria (see the four criteria listed in `Acceptance Criteria`). Each test case in [test_triangle.py](./test_triangle.py) matches one of those criteria. I took these criteria from the Requirements Specification provided:
```
“Write a function classify_triangle() that takes three  parameters: a, b, and c. The three parameters represent the lengths of the sides of a triangle. The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral, and whether it is a right triangle as well.”
```

### Author: Veronica Herzog

[![Build Status](https://app.travis-ci.com/vherzog/ssw567-hw1.svg?branch=main)](https://app.travis-ci.com/vherzog/ssw567-hw1)
