import json

import pytest

from quadratic_equation import app


def test_split_numbers():
    assert app.split_numbers("1,2,3") == [1,2,3]

def test_is_quadratic_equation():
    assert app.is_quadratic_equation([1,6,8]) == "２つの異なる実数解"
    assert app.is_quadratic_equation([1,6,9]) == "重解"
    assert app.is_quadratic_equation([1,2,3]) == "虚数解"
