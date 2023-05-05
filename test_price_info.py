import pytest
from price_info import total_cost_shopping, cost_of_fruits

def test_total_cost_shopping():
    assert total_cost_shopping() == 31.75

def test_cost_of_fruits():
    assert cost_of_fruits('apple', 5) == 6.0
    assert cost_of_fruits('watermelon', 1) == 6.5
    assert cost_of_fruits('pear', 10) == 9.0
