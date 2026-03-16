import pytest
import math
from calculator import hypotenuse, circleArea, average, squareNums, triNums, lazyCaterer, magicSquares

@pytest.mark.parametrize("a, b, expected",[
        (3,4, 5.0),
        (5, 12, 13.0),
        (8, 15, 17.0),
    ])
def test_hypotenuse(a, b, expected):
    assert hypotenuse(a,b) == pytest.approx(expected)

@pytest.mark.parametrize("radius, expected", [
    (1, math.pi),
    (2, math.pi * 4),
    (3, math.pi * 9),
    
])
def test_circleArea(radius, expected):
    assert circleArea(radius) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (10, 20, 15.0),
    (0, 0, 0.0),
    (-4, 4, 0.0),
])
def test_average(a, b, expected):
    assert average(a, b) == expected

@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (3, 6),
    (5, 15),
])
def test_triNums(n, expected):
    assert triNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (2, 4),
    (3, 7),
])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 15),
])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected

