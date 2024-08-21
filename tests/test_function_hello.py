# TODO: Check TDD method
from app.function import hello_guys


def test_hello_guys():
    output = hello_guys()
    expected = "hello!"
    assert output == expected
