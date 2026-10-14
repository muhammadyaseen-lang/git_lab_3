
from app3 import add_numbers, greet


def test_add_numbers():
    assert add_numbers(5, 3) == 8


def test_greet():
    assert greet("Student") == "Hello, Student!"
