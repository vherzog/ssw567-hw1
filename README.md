# SSW567 HW01
## Deliverables

### Source code
Python source code lives in `triangle.py`.

### Test code
Python test code lives in `test_triangle.py`.
```
python -m unittest -v
```

## Acceptance Test Cases
1. Function takes 3 parameters.
2. Function inputs represent the sides of a triangle.
3. Function returns a string.
4. Function returns whether triangle is `scalene`, `isosceles`, or `equilateral`.
5. Function returns whether triangle is `right`.

## Missing requirements/Assumptions
* Input types can be type `int` or `float`.
* Sides must equal a *valid* triangle.
* If sides make a `right` triangle, function returns `"<type> and Right"`
* If requirements are not met, function raises a `ValueError`.
* `Right` triangles are calculated with precision to the fourth decimal.

## Issues
I had difficulty testing for the case of `Isosceles and Right`. This would be triangles with sides of value `X`, `X`, `X*sqrt(2)`. Without rounding to a specific decimal, the `classify_triangle` function would not classify those side lengths as a `Right` triangle, only `Isosceles`. For this reason, I added an assumption that `Right` triangles would be calculated with precision to the fourth decimal.

### Author: Veronica Herzog

[![Build Status](https://app.travis-ci.com/vherzog/ssw567-hw1.svg?branch=main)](https://app.travis-ci.com/vherzog/ssw567-hw1)
