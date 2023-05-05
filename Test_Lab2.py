import Lab2.Lab2a as temperature
def find_min_max(float_list):
    float(float_list)
    float_list= input()
    minimum=min(float_list)
    maximun=max(float_list)
    print("The minimum value is:", minimum)
    print("The maximum value is:", maximun)

def calc_average(float_list):
    total = sum(float_list)
    count = len(float_list)
    average = total / count
    print("The average is:", average)


def calc_median_temperature(sorted_list):
    list_length = len(sorted_list)
    middle_index = list_length // 2
    if list_length % 2 == 0:
        median = (sorted_list[middle_index-1] + sorted_list[middle_index ]) / 2
    else:
        median = sorted_list[middle_index]
    print("The median is:", median)

