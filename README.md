#RandomProblemCodes
##Matrix Problem - matrix_problem.py
Random generate a NxN matrix with only four types of element: 1,2,3,4. 
However, no column or row can have same type of element appears 3 times or above continuously (three same type of elements are connected)

ex: 

valid, below: 
> 1 2 1 1

> 3 1 4 2 

> 1 2 4 2 

> 3 1 2 3 

invalid, below: 
> 1 2 1 3 

> 1 3 4 2 

> 1 2 4 4 

> 2 3 2 2

because the first column has element 1 appears three times and all 1s are connected to each other.

## Find palindrome/mirrors in a given word - find_longest_palindrome.py
Return the length of longest possible chunked palindrome string. 

Examples : 

> Input : VOLVO 

> Output : 3 

Explanation : 
(VO)L(VO) 


> Input : merchant 

> Output : 1 

Explanation : 
No chunks possible. 

> Input : ghiabcdefhelloadamhelloabcdefghi 

> Output : 7 

Explanation : 
(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)

## Find matching pattern in a given word sequence - find_pattern.py

Given a pattern and a string - find if the string follows the same pattern 

Eg: Pattern : [a b b a], String : cat dog dog cat

## Number pad combination - number_pad_combination.py

Given a digit string, return all possible letter combinations that the number could represent. Mapping of digit to letters (just like on the telephone buttons or even your new touch-key pads).

> Input:Digit string "23"

> Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
