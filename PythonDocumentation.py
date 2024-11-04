'''
What is Python and why for data science?
Python is high-level object oriented programming interpreted language, this is the most widely used programming language for data science because of its extensive number of libraries.

Python Objects & Data Structures:

1. Integers - Whole numbers both positive and negative. For example, 1,2,and 9.
2. Floating Points - Numbers with decimal points. For example, 5.3, 100.0, 11.2.
3. Strings - Ordered Sequence of characters. For example, "2000", "sammy", "11.234", 'sam'
4. Lists - Ordered sequence of objects. For examplev [1, "sammy", 12.456]
5. Tuples - Ordered immutable sequence of objects. For example, (1,2,'sammy','100.0')
6. Dictionary - Unordered key value pairs. For example, {"Key1":"Sai","Key2":"Harsha"}
7. Set - Unordered collection of unique objects. For example, {'a', 'b'}
8. Boolean - Logical value representation. For example, True, False.

Numbers - 
1. These include both integers and floating points. Now lets see few basic arithmetic operations on numbers.
2. The operations follow (PEDMAS) rule for the operation priority
    Addition - 1+1, 2+3
    Subtraction - 2-1, 99-100
    Multiplication - 2*3, 3*3
    Division - 3/3, 9/10
    Power - 2**3, 4**2
    Modulo - returns the remainder 10%3 (returns 1)

Variable Assignment
1. Variable assugnments are useful in storting the data objects.
    For example, my_num = 9
2. Variable names cannot start with numbers and also cannot have space between them instead use underscores(_).
3. It is considered to use lower case to be the best practice and avoid using keywords.
4. Python allows dynamic typing which means that a variable assigned to one data type value can later be reassigned to any other type of data object as well, which does not work with 
   other languages.
5. We can use type() funnction to know the type of that data object

Strings - 
1. Strings are ordered sequence of characters with the syntax of single quotes and double quotes. For example, "Hello World", 'Hello', "I'm here".
2. A segment of string can be taken using indexing and slicing, where the index starts from 0.
3. Indexing helps us to get one charcater of the string. 
   For example, my_name = "Sammy"
   my_name[0] will result in "S"
4. We can also make use reverse indexing where my_name[-1] results in "y", my_name[2] - "m"
5. Slicing is to get a group of characters from a string with syntax [start:stop:step]
   For example my_name = "Sammy", my_name[0:2] will result in "Sa".
6. len() function is used to know the length of the data object. 
7. Reversing a string using slicing - [::-1].
8. String are immutable. For example say my_name = "Sam" and my_name[0] = "P" results in an error, but can be acheived using concatenation and variable reassignment.
'''