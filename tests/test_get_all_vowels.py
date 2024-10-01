from lib.get_all_vowels import *

def test_get_all_vowels_1():
    actual = get_all_vowels("Its an amazing day")

    expected = "Iaaaia"

    assert actual == expected

def test_get_all_vowels_2():
    actual = get_all_vowels("I love life")

    expected = "Ioeie"

    assert actual == expected