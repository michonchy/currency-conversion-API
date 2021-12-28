import json

import pytest

from ascending_order import app


def test_split_numbers():
    assert app.split_numbers("1,2,3") == [1,2,3]

def test_is_ascending_order():
    assert app.is_ascending_order([1,2,3]) == "OK"
    assert app.is_ascending_order([3,2,1]) == "NG"
