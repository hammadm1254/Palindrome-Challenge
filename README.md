This is a toy project used to generate the list of the first 1000 integers greater than zero
and the base number system in which each integer is palindrome.

To run the program simply execute the "palindrome.py" file with a python 3.5+ interpreter.
The output will be a "palindromeList.csv" file in the same directory from which the
program is executed.

"testCases.csv" file is necessary for running the "test_palindrome.py" file which tests
the important functions in the "palindrome.py file" The HTML output of the test results
is in "Test Results - Unittests_in_test_palindrome_py.html" file.

Overview:

Palindrome number is defined as a number having a property in which the digits of the number
when written LSB(Least significant bit) to MSB(Most significant bit) are identical to the number
being written MSB to LSB.

Based on the definition we derive the following axioms:
1.) Any single digit number is palindrome.
2.) Any base-n integer is palindrome in a base-n+1 i.e. system whose numerical value
  is one greater than the numerical value of the number:
  Ex:
    111 in base-10 will be a single digit number in base 112

Solution Overview:
The program is split into multiple functions, two of which are crucial: to_Base and is_Pal.


The Function to_Base takes into input two integers. One is a base value and the other is
the number in base-10. It recursively performs division of the number by the base until the
number is zero. With each division the remainder is saved into a list. The result of this
recursive division is a list of digit values in base-10 which represents the number in a given
base. Note, in some cases the digit values in the list may exceed base-10 single digit values.

For Example:
  13 in base-16 is the letter D, but the function will return the list: [13]
  this is because in base-16 system the LSB has values from 0 to 15. Thus, 13
  is in the "ones" place of the base-16 system. Since hex is somewhat common
  system in CS field the digit representation has been developed by utilizing
  the English alphabet to represent single digit numbers in base-16 whose value
  exceed decimal or base-10 value of 9.

For the program the digit representation is composed of a list of positive decimal integers
which is returned by the to_Base function and passed to the is_Pal function.


The is_Pal function determines if the list of digit is a valid palindrome and returns a boolean
value. Commonly, this verification can be done by creating a copy of the list and reversing
it then comparing it with the original. Python language has implemented methods to allow this
with a single line of code. However, due to a midnight, caffeine induced, euphoria the author
felt it would be fruitful to devise a more efficient way of doing the verification on the list.
Thus, the is_Pal method checks the first and last elements of the list to see if they are identical
then it checks the second to last and second element and so on until all the elements are checked
and the list is exhausted. This is true for lists with even number of elements, which result
in length(n)/2 pairs of elements, where n is the list. For lists with odd number of elements
there is one element remaining in middle which represents a single digit which is a palindrome
on its own according to the first axiom. If all the pairs have identical elements then the list
is palindrome and the function returns True. If any pair has non-matching elements the loop breaks
and the function returns false. This eliminates the need to create a copy of the list thus reducing
memory consumption. Also, the need to reverse the list is eliminated. The iteration of the loop
takes O(n/2) time as the elements are checked in pairs. This whole process can be visualized by
thinking of chopping the list in half and folding it over itself then comparing the elements.

For Example:
    |------------|
    [1,  0,  0,  1]
         ^---^


The minimum_Base function takes a given integer and checks if the given number is a palindrome in
base-2 successively up to base value of the number plus 1. The upper limit is set to number+1
as a result of axiom 2. The function returns the base in which the number is a palindrome.


The Main function  uses an iterator function to generate integers from 1 to the integer value
stored in limit variable and passes each integer to the minimum_Base function which returns the
integer value of the base in which the integer is a palindrome. The result is stored in a dictionary.
at the end of the iteration the Main function passes the dictionary to the writeToCSV function which
uses python's csv writer module to write the results into a CSV file.
