from lib.add_number_to_another_number import *

def test_add_number_2_to_number6():
    actual = add_number_to_another_number(2, 6)
    expected = 8

    assert actual == expected

def test_add_number_4_to_number5():
    actual = add_number_to_another_number(4, 5)
    expected = 9

    assert actual == expected