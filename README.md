#RandomProblemCodes
##Matrix Problem - matrix_problem.py
* Description: 
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

## FIND LONGEST PALINDROME IN A WORD - find_longest_palindrome.py
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

