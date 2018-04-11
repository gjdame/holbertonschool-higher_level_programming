
*0.*

This program assigns a random signed number to the variable number each time it is executed. 
*1.*

This program assigns a random signed number to the variable number each time it is executed.

*2.*
Program that prints the alphabet, in lowercase, not followed by a new line.
You can only use one print function with string format 
You can only use one loop in your code 
You are not allowed to store characters in a variable 
You are not allowed to import any module

*3.*
Program that prints the alphabet, in lowercase, not followed by a new line.
Print all the letters except q and e 
You can only use one print function with string format 
You can only use one loop in your code 
You are not allowed to store characters in a variable 
You are not allowed to import any module

*4. Hexadecimal printing* 
Program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)
You can only use one print function with string format 
You can only use one loop in your code 
You are not allowed to store numbers or strings in a variable 
You are not allowed to import any module

*5.*
Program that prints numbers from 0 to 99.
Numbers must be separated by ,, followed by a space 
Numbers should be printed in ascending order, with two digits 
The last number should be followed by a new line 
You can only use no more than 2 print functions with string format 
You can only use one loop in your code 
You are not allowed to store numbers or strings in a variable 
You are not allowed to import any module

*6.* 
Program that prints all possible different combinations of two digits.
Numbers must be separated by ,, followed by a space 
The two digits must be different 
01 and 10 are considered the same combination of the two digits 0 and 1 
Print only the smallest combination of two digits 
Numbers should be printed in ascending order, with two digits 
The last number should be followed by a new line 
You can only use no more than 3 print functions with string format 
You can only use no more than 2 loops in your code 
You are not allowed to store numbers or strings in a variable 
You are not allowed to import any module

*7. islower *
Function that checks for lowercase character. 
Prototype: def islower(c): 
Returns True if c is lowercase 
Returns False otherwise 
You are not allowed to import any module 
You are not allowed to use str.upper() and str.isupper()

*8. To uppercase* 
Function that print a string in uppercase followed by a new line.
Prototype: def uppercase(str): 
You can only use no more than 2 print functions with string format 
You can only use one loop in your code 
You are not allowed to import any module 
You are not allowed to use str.upper() and str.isupper()

*9.* 
Function that prints the last digit of a number.
Prototype: def print_last_digit(number): 
Returns the value of the last digit 
You are not allowed to import any module

*10. a + b* 
Function that adds two integers and returns the result.
Prototype: def add(a, b): 
Returns the value of a + b 
You are not allowed to import any module

*11. a ^ b* 
Function that computes a to the power of b and return the value.
Prototype: def pow(a, b): 
Returns the value of a ^ b 
You are not allowed to import any module

*12. Fizz Buzz* 
Function that prints the numbers from 1 to 100 separated by a space. 
For multiples of three print Fizz instead of the number and for multiples of five print Buzz. 
For numbers which are multiples of both three and five print FizzBuzz. 
Prototype: def fizzbuzz(): 
Each element should be followed by a space 
You are not allowed to import any module

*13. Insert in sorted linked list*  
Function in C that inserts a number into a sorted singly linked list.
Prototype: listint_t *insert_node(listint_t **head, int number); 
Return: the address of the new node, or NULL if it failed

*100.*  
Program that prints the alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
You can only use one print function with string format 
You can only use one loop in your code 
You are not allowed to store characters in a variable 
You are not allowed to import any module

*101. Remove at position*  
Function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
Prototype: def remove_char_at(str, n): 
You are not allowed to import any module

*102. ByteCode*  
Function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE