import Lab2.Lab2 as bmi

def test_bmi_normal_weight():
    expected_result = 0
    result = bmi.calculate_bmi(1.73, 65)
    assert(result == expected_result)
def test_bmi_over_weight():
    expected_result = 1
    result = bmi.calculate_bmi(1.73, 85)
    assert (result == expected_result)
def test_bmi_under_weight():
    expected_result = -1
    result = bmi.calculate_bmi(1.73, 45)
    assert (result == expected_result)
