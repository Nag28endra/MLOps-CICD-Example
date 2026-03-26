import pytest

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def fifth_power(x):
    return x ** 5

def test_square():
    assert square(2) == 4, "Test Failed: square(2) should be 4"
    assert square(-3) == 9, "Test Failed: square(-3) should be 9"
    assert square(0) == 0, "Test Failed: square(0) should be 0"

def test_cube():
    assert cube(2) == 8, "Test Failed: cube(2) should be 8"
    assert cube(-3) == -27, "Test Failed: cube(-3) should be -27"
    assert cube(0) == 0, "Test Failed: cube(0) should be 0"

def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: fifth_power(2) should be 32"
    assert fifth_power(-3) == -243, "Test Failed: fifth_power(-3) should be -243"
    assert fifth_power(0) == 0, "Test Failed: fifth_power(0) should be 0"


def test_invalid_input():
    with pytest.raises(TypeError):
        square("a string")
    with pytest.raises(TypeError):
        cube("a string")
    with pytest.raises(TypeError):
        fifth_power("a string")
