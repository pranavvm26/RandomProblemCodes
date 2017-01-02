import copy
import numpy as np


def match_pattern(num_pattern, user_pattern):
    result_list = []
    num_pattern = np.asarray(num_pattern)
    for i in num_pattern:
        index_values = np.where(num_pattern == i)[0]
        index_values = list(index_values)
        for i, value in enumerate(index_values):
            if i == 0:
                temp = user_pattern[value]
            else:
                if temp == user_pattern[value]:
                    pass
                else:
                    result_list.append(False)
    return result_list


def find_pattern(pattern):
    dup_pattern = copy.deepcopy(pattern)
    for i, n in enumerate(pattern):
        letter = n
        for num, val in enumerate(dup_pattern):
            if val == letter:
                dup_pattern[num]= i
    return dup_pattern


if __name__ == "__main__":
    pattern = input("please enter the pattern in comma seperated format, example-a,b,b,a:")
    user_pattern = input("please enter the list to find the pattern in, comma seperated format, example-dog,cat,cat,dog:")
    pattern = pattern.split(",")
    user_pattern = user_pattern.split(",")
    num_pattern = find_pattern(pattern)
    ret = match_pattern(num_pattern, user_pattern)
    if len(ret) == 0:
        print("Pattern matches")
    else:
        print("Pattern does NOT match")
