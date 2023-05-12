from price_info import *


def test_total_cost_shopping():
    result = total_cost_shopping()
    assert result == 46.75

def test_cost_of_fruits():
    assert cost_of_fruits('apple', 5) == 6.0
    assert cost_of_fruits('watermelon', 1) == 6.5
    assert cost_of_fruits('pear', 10) == 9.0


if __name__ == '__main__':
    test_total_cost_shopping()
    test_cost_of_fruits()
    print('All tests passed')
