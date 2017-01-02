import copy

def generate_limit_list(limits):
    lim_list = []
    for i in range(limits[0],limits[1]):
        lim_list.append(i)
    return lim_list


def compress_list(uncompressed_list):
    compress_limit_list = []
    for indx, value in enumerate(uncompressed_list):
        next_value = value + 1
        if indx == 0:
            starting_value = value
        else:
            if next_value in uncompressed_list:
                pass
            elif next_value not in uncompressed_list:
                ending_value = value
                diff = ending_value-starting_value
                if diff != 0:
                    compress_limit_list.append(str(starting_value)+"-"+str(ending_value))
                elif diff == 0:
                    compress_limit_list.append(str(starting_value))
                if indx+1 < len(uncompressed_list):
                    starting_value = uncompressed_list[indx+1]
                    ending_value = 0
    return compress_limit_list


def find_missing_numbers(list_numbers,limits):
    orginal_limits_list = generate_limit_list(limits=limits)
    limits_list = copy.deepcopy(orginal_limits_list)
    for ind, value in enumerate(list_numbers):
        for ind2, value2 in enumerate(limits_list):
            if value2 == value:
                del limits_list[ind2]
                break

    compress_limit_list = compress_list(limits_list)
    return compress_limit_list


if __name__ == "__main__":
    _list_numbers = input("list of numbers in comma seperated format:")
    _lower_upper_limit = input("enter the lower and upper limit of numbers in comma seperated format:")
    _list_numbers = _list_numbers.split(",")
    _lower_upper_limit = _lower_upper_limit.split(",")
    for index, numbers in enumerate(_list_numbers):
        _list_numbers[index] = int(numbers)
    for index, numbers in enumerate(_lower_upper_limit):
        _lower_upper_limit[index] = int(numbers)
    compress_limit_list_ = find_missing_numbers(list_numbers=_list_numbers, limits=_lower_upper_limit)
    print("Missing values are :", compress_limit_list_)


