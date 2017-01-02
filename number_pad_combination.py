number_pad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def letters_combination(letter_list):
    len_list = len(letter_list)
    for num in range(1,len_list):
        combination_list = []
        for x in range(len(letter_list[0])):
            for y in range(len(letter_list[num])):
                combination_list.append(letter_list[0][x]+letter_list[num][y])
        letter_list[0] = combination_list

    return letter_list[0]


if __name__ == "__main__":
    number_entry = input("please enter the numbers on the number pad:")
    number_entry = list(number_entry)
    associated_letters = []
    for i in number_entry:
        associated_letters.append(list(number_pad[i]))
    combination_list = letters_combination(letter_list=associated_letters)
    print("The number of combinations are:", len(combination_list))
    print(combination_list)
