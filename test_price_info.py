import price_info


def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    assert (result == 46.75)

def test_cost_of_fruits_apple():
    quantity = 20
    expected_result = quantity * 1.20
    result = price_info.cost_of_fruits ('apple',quntity)
    assert (expected_result == result)

def test_cost_of_fruits_orange():
    quantity = 20
    expected_result = quantity * 1.40
    result = price_info.cost_of_fruits ('orange',quntity)
    assert (expected_result == result)


def test_cost_of_fruits_watermelon():
    quantity = 20
    expected_result = quantity * 6.50
    result = price_info.cost_of_fruits ('watermelon',quntity)
    assert (expected_result == result)
