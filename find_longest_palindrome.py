import copy

palindrome_list = []

def find_palindrome(palindrome_string):
    longest_current_palin = 0
    list_p = list(palindrome_string)
    for i in range(2, len(list_p), 1):
        duplicate_string = copy.deepcopy(list_p)
        del duplicate_string[0:i]
        _set = list_p[0:i]
        res = "".join(_set) in "".join(duplicate_string)
        if res:
            longest_current_palin = _set
            #print(res, " with word ", "".join(_set))
    if longest_current_palin != 0:
        print("The longest palindrome word in the current session is ", "".join(longest_current_palin))
        return palindrome_string.replace("".join(longest_current_palin), ""), "".join(longest_current_palin)
    else:
        return "", ""


if __name__ == "__main__":
    palindrome_string = input("Enter the string to find the palindrome from:")
    palindrome_string_modified, longest_palindrome_word = find_palindrome(palindrome_string)
    palindrome_list.append(longest_palindrome_word)
    while True:
        palindrome_string_modified, longest_palindrome_word = find_palindrome(palindrome_string_modified)
        palindrome_list.append(longest_palindrome_word)
        if len(list(palindrome_string_modified)) == 0:
            break

    if palindrome_list[0] != "":
        print("The longest palindrome words in the string are as follows :")
        for strings in palindrome_list:
            print(strings)
    else:
        print("No palindrome words in the given string")
