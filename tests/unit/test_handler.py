import json

import pytest

from currency_conversion import app


def test_split_numbers():
    assert app.split_numbers("1,2,3") == [1,2,3]

def test_is_currency_conversion():
    assert app.is_currency_conversion([1,6,8]) == "２つの異なる実数解"
    assert app.is_currency_conversion([1,6,9]) == "重解"
    assert app.is_currency_conversion([1,2,3]) == "虚数解"
