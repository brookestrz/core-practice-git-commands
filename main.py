import pytest


def always_returns_true():
    return False
    print("Hi I'm Lee, I made this change :D")


def test_always_returns_true():
    assert always_returns_true()
