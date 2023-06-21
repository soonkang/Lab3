import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = []
    test_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 22, 90, 100, 23, 99]
    test_arr = [100, 99, 90, 64, 34, 25, 23, 22,]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, "Not a function")

    assert (result == result)