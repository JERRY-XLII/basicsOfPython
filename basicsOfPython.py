### This is a list of basic python functions

# Note: Comments in Python
# A comment is used to explain the Program. Anything included in the comment is not read as part of the program by the 
# interpreter. 
# is used for a comment
""" can be used for a 
multiline comment """
''' similarly these can also 
be used '''
# though only # will be used here, because quotation comments are cringe.  

# The print() function is used to print an output.  
print ("Hello, World!");
# Note: Separate print() functions will output in different lines. In order to include two print functions, you must 
# use end = " " 
print("Hello,", end = " ");
print("there"); 

## A variable is a named location used to store data in the memory.
# Variables are user-defined, and may change as the program runs.
# Here, a is a variable.
# Literal is a raw data given in a variable or constant.
# Here, 5 is a numeric literal, and "High five" is a string literal.
a = 5
print ("a =", a);
a = "High five"
print ("a =", a);

## Arithmetic operators are used to perform mathematical operations.
# This is a list of some basic arithmetic operators in python.
# They are, in order, addition, substraction, multiplaction, division, 
# floor division (quotient), modulus (remainder) and exponentiation 
x = 3
y = 2
print ("x + y =", x + y);
print ("x - y =", x - y);
print ("x * y =", x * y);
print ("x / y =", x / y);
print ("x // y =", x // y);
print ("x % y =", x % y);
print ("x ** y =", x ** y);

## Assignment operators are used to assign values to variables.
# This is a list of some basic assignment operators in python.
# = is the basic assignment operator, it assigns a literal to a variable. 
x = 5
print ("x = ", x);
# x += 5 ----> x = x + 5
x += 5
print ("x = ", x);
# x -= 5 ----> x = x - 5
x -= 5
print ("x = ", x);
# Similarly, the other assignment operators are related to specific arithmetic operators, and are listed in the same 
# order as above. 
x *= 5
print ("x = ", x);
x /= 5
print ("x = ", x);
x //= 5
print ("x = ", x);
x %= 5
print ("x = ", x);
x **= 5
print ("x = ", x);
# Another assignment operator is ==, which is used with logical operators for comparing two or more statements. 
# Its use shall be explained with logical operators.

## The input() function is used to allow the user to enter an input.
inputString = input("Enter a sentence:");
print("The inputted string is:", inputString);
# Defining a variable is necessary, the following doesnt work.
# print('The inputted string is:', input('Enter a sentence:'))

## Type conversion is used to convert one datatype to another.
# Implicit conversion doesn't need any user involvement.
# integer type 
num_int = 123 
# float type 
num_flo = 1.23
num_new = num_int + num_flo
# The first of the following commands prints the value of the variable num_new, the second command prints the datatype 
# of the variable. 
# (note the type() function).
print("Value of num_new:", num_new);
print("Datatype of num_new:", type(num_new));
# Here, num_new has float data type because Python always converts smaller data type to larger data type to avoid the 
# loss of data.
# Here is an example where the Python interpreter cannot implicitly type convert.
# num_int = 123     # int type
# num_str = "456"   # str type
# print(num_int+num_str)
# Running this will give an error.
# Explicit conversion is necessary in such cases.
# In explicit conversion the datatype of an object is converted through pre-defined function like int(), str(), float(),
# etc. to the required data type.
# int type
num_int = 123  
# str type
num_str = "456" 
# explicitly converted to int type
num_str = int(num_str); 
print("The sum is", num_int + num_str);
# Explicit conversion is important when using input() because by default the input is stored as a string
a = int(input("Enter a number:"));

# A list is created by placing all the items (elements) inside a square bracket [] separated by commas.
# It can have any number of items and they may be of different types (integer, float, string etc.)
# empty list
empty_list = []
# list of integers
int_list = [1, 2, 3]
# list with mixed data types
mixed_list = [1, "Hello", 3.4]
# List(); function can also be used to create lists, though it only takes single elements.
f_list = list("6");
# List elements must be accesed for the list to be useful.
# Lists are indexed left to right starting from 0.
# They are also indexed right to left, starting from -1 and going in decreasing order.
language = ["French", "German", "English", "Polish"]
# Accessing first element
print(language[0]);
# Accessing fourth element
print(language[3]);
# Tuples are similar to lists, but may not be modified after the fact. 
language = ("French", "German", "English", "Polish")
print(language);
# They may be deleted after the fact though
del language

# A string is a sequence of characters.
# All of the following are equivalent.
string1 = 'Hello'
print(string1);
string2 = "Hello"
print(string2);
string3 = '''Hello'''
print(string3);
# Triple quotes string can extend multiple lines.
my_string = """Hello, welcome to
           the world of Python"""
print(my_string);
# You can access individual characters of a string using indexing (in a similar manner like lists and tuples).
str = 'Monseiur'
print('str = ', str)
# Prints first character; Output: M
print('str[0] = ', str[0]) 
# Prints last character; Output: r
print('str[-1] = ', str[-1]) 
#slicing 2nd to 5th character; Output: onse
print('str[1:5] = ', str[1:5]) 
#slicing 5th to 2nd last character; Output: ei
print('str[5:-2] = ', str[4:-2]) 
# Strings are immutable. You cannot change elements of a string once it is assigned. However, you can assign one string
# to another, or delete them using the del operator.

# Concatenation is a very useful string operation. You essentially "add" strings using concatenation.
# The + operator is used for concatenation.
str1 = "Hallo, "
str2 = "Welt! "
str3 = str1 + str2
print(str3);
# Similarly, the * operator is used to repeat strings.
print(str3 * 3);