import Lab2.Lab2
import Lab2.Lab2 as bmi

def test_bmi_normal_weight():
    result= Lab2.Lab2.calculate_bmi(1.73, 65)
    assert(result==0)
def test_bmi_over_weight():
    result = Lab2.Lab2.calculate_bmi(1.73, 85)
    assert (result == 1)

def test_bmi_under_weight():
    result = Lab2.Lab2.calculate_bmi(1.73, 45)
    assert (result == -1)

