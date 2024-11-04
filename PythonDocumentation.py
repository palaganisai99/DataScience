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

String Interpolation - 
We have two methods .format() and f-string literals method to use strings with in the print function or concatenation.

1. .format() method - 
   For example, print("A {} {} {}.".format("quick","brown","fox")) will result in "A quick brown fox."
                print("A {1} {0} {2}.".format("brown","quick","fox")) will result in "A quick brown fox."
                print("A {2} {2} {2}.".format("brown","quick","fox")) will result in " A fox fox fox."
                print("A {q} {b} {f}.".format(b="brown",q="quick",f"fox")) will result "A quick brown fox."
         
2. f-string literal -
   For example, my_name = "Sammy"; 
                print(f'My name is {my_name}') will result in "My name is Sammy"
   Secondly, We can make use of f-strings for rounding the number as well.
   For example, my_price = 123.82314576819
                print(f'My price is {my_price:.2f}') will result in "My price is 123.82" 

Lists - 
1. Lists are ordered sequence of data objects of different types and they are mutable.
2. Lists also support indexing and slicing.
   my_list = [1,"hello",[1,2,3], 12.345]
   len(my_list) will return 4 for the number of data objects in it.
3. Lists can be concatenated but it is not inplace which means say,
   For example, my_list = [1,2,3]; another_list = [4,5]
   my_list + another_list will result in [1,2,3,4,5] but does not change my_list and another_list but if you want it to overwrite my_list
   my_list = my_list + another_list will result in my_list = [1,2,3,4,5] and another_list stays same.
4. .append() will add the respective data object at the end of the list.
   For example my_list = [1,2,3]
               my_list.append(4) will result in [1,2,3,4]
5. .pop() by default removes the last object from the list, but giving an index removes particular object from the list.
   For example, my_list - [1,2,3]; my_list.pop() will remove 3 from the list.
6. .sort() can be used to sort the objects in the list but it is not inplace which means say,
   For example, my_list = ['a','x','c'];
                sorted_list = my_list.sort()
                print(sorted_list); will result in None
                print(my_list); will result in ['a','x','c'] which is unsorted.

Dictionaries - 
1. Dictionaries are unordered sequence of key value pairs. We can retreive yje value using the resepective key.
   For example, my_dict = {'key1':'Sam','key2':'Sammy','key3':[0,1,2]}
   my_dict['key1'] will result in 'Sam';
   my_dict['key3'][1] will result in 1;
2. Adding an element to dictionary. For example my_dict = {'key1':'Sam','key2':'Sammy','key3':[0,1,2]};
   my_dict['key4'] = 123.4;
   print(my_dict) will result in {'key1':'Sam','key2':'Sammy','key3':[0,1,2],'key4':123.4}
   my_dict['key1'] = 'NEW VALUE';
   print(my_dict) will result in {'key1':'NEW VALUE','key2':'Sammy','key3':[0,1,2],'key4':123.4}
3. my_dict.keys() will give me a list of all keys ['key1','key2','key3','key4']
   my_dict.values() will produce a list of all values of my_dict ['NEW VALUE', 'Sammy', [0,1,2],123.4]
   my_dict.items() will give me a list of tuples of my_dict [('key1','NEW VALUE'),('key2','Sammy'),('key3',[0,1,2]),('key4',123.4)]

Tuples - 
1. Tuples ordered sequence of immutable data objects, which means the data objects cannot be reassigned.
   For example, (1,2,3,4), (1,'hello',123.456)
2. For example, my_tup = ('a','a','b');
                my_tup.count('a') will result as 2
                my_tup.index('a') will result 0, it will produce the index of first occurence.

Sets - 
1. Sets are unordered collection of unique data objects. 
   For example set{'a','b','c','b','a'} will produce {'a','b','c'}
2. .add('a') will append the data object to the set.

Booleans - 
Booleans are just logical values to convey True or False of statements. True and False both are case-sensitive.


Python Comparison Operators - 
The comparison operators are similar to the mathematical operators for comparison.

1. == returns True if both values are equal.
2. != returns True if both values are not equal.
3. > returns True if value on LHS is greater than value on RHS
4. < returns True if value on LHS is lesser than value on RHS
5. >= returns True if value on LHS is greater than or equal to the value on RHS
6. <= returns True if value on LHS is lesser than or eual to the value on RHS

Logical Operators - 
Logical Operators are used to define the truthfulness of statements using and, or and not keywords.

1. and - 
   The and operated returns True only if all the statements are True.
   For example, (1==1) and (2==2) return True; (1==2) and ('sam'=='sam') returns False
2. or - 
   The or operator returns True even if one of the statements is True.
   For example, (1==2) or ('sam'=='sam') returns True; (1>2) or (5<4) returns False
3. not - 
   The not operator is used to reverse the logical value.
   For example not(True) returns False; not(3>4) returns True
'''