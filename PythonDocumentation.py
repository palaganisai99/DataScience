'''
Python Basics for Data Science

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


Python Statements -

Control Flow Statements(if-elif-else):
Control flow statements are used to execute a piece of code when some conditions are met.
For example, my_name = 'Sammy'
             if my_name == 'Sammy':
               print("Hello, Sammy")
             elif my_name == 'Frankie':
               print("Hello, Frankie")
             else:
               print("What is your name?")
The above example prints "Hello, Sammy" if the value in my_name variable is 'Sammy' and 'Hello, Frankie' if its 'Frankie' else it will say 'What is your name?'.

For loops - 
For loops are used iterate a particular piece of code over the data objects like every character in a string. every elements in the list etc.

1. my_list = [1,2,3,4,5]
   for num in my_list:
      print(num) # will result in 1 2 3 4 5
2. print even number in my_list
   for num in my_list:
      if num%2 ==0:
         print(num) # will result in 2 4
3. my_list = [(1,2),(2,3),(3,4)]
   for (a,b) in my_list:
      print(a) # will result in 1 2 3
4. my_dict = {'k1':1,'k2':2,'k3':3}
   for key,value in my_dict.items():
      print(value) # will result in 1 2 3
   for i in d:
      print(i) # will result in k1, k2, k3 (by default it prints keys)
   for key,value in my_dict.items():
      print(key) # will result in k1, k2, k3

While Loops -
While Loops execute a piece of code until the consition is False.
For example my_num = 0
            while my_num < 5:
               my_num += 1
               print(my_num) # will result 1 2 3 4 5
            else:
               print('my_num is not less than 5.')

We have 3 keyword that will be helpful in loops (Works with both for and while loops):
1. pass - which does nothing
   For example, i = 0
                while i < 5: 

   if we run the above code will result in an error, instead we can pass it to avoid the error doing nothing
                i = 0
                while i < 5:
                  pass
2. continue - It will go to the top of nearest enclosing loop.
   For example, my_name = 'Sammy'
                for i in my_name:
                  if i == 'a'
                  continue # will result S m m y
   So here the loop when the character is equal to a will not go futher in the loop and goes to start of the loop to iterate with next character.
3. break - It will break the nearest enclosing loop.
   For example, my_name = 'Sammy'
                for i in my_name:
                  if i == 'a':
                     break
                  print(i) # will result in S
   So here when the i is equal to a then the loops break and comes out also not iterating the other characters further.

List Comprehensions -
List comprehensions are best for creating lists using for loops along with append function.
For example, 1. my_list = [x for x in range(0,6)]
                my_list # will result in [0,1,2,3,4,5]
             2. my_list = [x**2 for x in range(0,6) if x%2==0]
                my_list # will result in [0,4,8]
             3. my_list = [x**2 if x%2 == 0 else 'ODD' for x in range(0,6)]
                my_list # will result in [0,'ODD',4,'ODD',8,'ODD']
             4. my_list = [x*y for x in range(0,2) for y in range(0,2)]
                my_list # will result [0,0,0,1]


Functions -
Functions are helpful in creating a code of block to be reusable without rewriting the code again and again. The syntax of function is as follows:

def name_of_function():
   #code

name_of_function() # just calling the function by its name will execute the function.

We mostly use the return keyword to get the output of the function as it helps us to assign the output to a variable, where as a print does not allow it.

def num_add(a,b):
   return a+b

mysum = num_add(2,3) # will store the result in variable

num_add(5) # will result in an error stating that missing 1 required positional argument(b), So it is must to have all the argument values when you call a function or can have
a default value at the time of defining a function.
For example, def num_add(b, a=2): # parameter with default value should be mentioned after the parameters without default
               return a+b

             num_add(3) # will result in 5 as we already a=2 set as default, if it was not set then it would result in error.

*args and **kwargs - 
Lets discuss about *args and **kwargs using an example,

def num_add(a,b):
   return a,b 

It will return the sum of parameters and what if we want to have the sum of arbitary number of arguments, else we have to define the parameters in the function with defaults or we
can make use *args

def num_add(*args):
   return sum(args)

num_add(2,3,10,22) # will result in 37
num_add(2,5) # will result in 7

The **kwargs are helpful if we want to define arbitary number of keyword arguments, they will stored in form a dictionary. For example,

def myfunc(*args, **kwargs):
   return f"I would like to have {args[0]} {kwargs['food']}."

myfunc(10,20,30,fruit='apple'.food='eggs') # will result in "I would like to have 10 eggs." 

Map & Filter -
Lets understand about map and filter functions using an example,

def square(n):
   return n**2

Syntax of map function map(function,list of values to be mapped to), It maps the function to every object in the list, iterates over like a for loop
mylist = [1,2,3]
list(map(square,mylist)) #will return [1,4,9]

Syntax of filer function filter(function, list of values to be mapped to), It returns only the values that are True other will be filtered out

def evenodd(n):
   if n%2 == 0:
      return n
   else:
      pass

mylist = [1,2,3]
list(filter(evenodd, mylist)) # will return [2]

Object Oriented Programming - 

Object Oriented Programming is used to create our own objects and its methods and function in python. Sometimes functions are also not ideal enough for repeatable tasks,
so we can make use of OOPs to create them. 

The OOPs is an object that takes in the information like parameters of the object and will return the results or changes the current objects make use of methods of class.

Syntax of creating a object - 

class NameOfClass():

   def __init__(self,param1,param2):
      self.param1 = param1
      self.param2 = param2

   def mymethod(self):
      print("Hello")

We make use of class keyword to create a class followed by its name and a colon. Then we define a __init__ function which is called constructor of the class, it creates the class
instance and self keyword is used to make the parameters used in the class to not be global variables but the parameters assigned within the object class, and every function followed
will have self as its first parameter to avoid using global variables and letting the object know that it is using the parameters of its own class.

Lets understand the class by an example:

class Dog():

   species = 'mammal'

   def __init__(self,name, breed):
      self.name = name
      self.breed = breed

   def bark(self,number):
      print("My name is {} and the number is {}.".format(self.name,number))   

So, we created a dog class using class keyboard then the first method in every class would be __init__ which is called a constructor class to initialize the instance. The self keyword
is a reference to the instance of that class. The parameters name, breed are then assigned to the instance attributes using self.attribute syntax.

We can assign something as below:

my_dog = Dog(name='Sammy',breed = 'Lab')
my_dog.breed() # will result in 'Lab'

1. some attributes are defined before the __ini__ method and are called class object attributes and those attributes will remain same across the class in all instances.
2. Attributes are just the characteristics of the objects where as the methods are functions that take in the object itself and perform the actions.

In the above example, bark is a method which takes self and number as its arguments, self is used to reference the instance of the class and number is the argument that can be explicitly
given to bark method which cannot be used in other methods.

Now, lets define class for circle

class Circle():

   def __init__(self, radius = 1):

      self.radius = radius
      self.area = radius * radius * Circle.pi

   def circumference():

      return self.radius * 2 * self.pi

1. In the above example, in the __init__ method we have given radius = 1 as an argument, so even if the argument is not given during the object call it still takes 1 as default value.
2. self.area is defined with formula produced by the attributes and class object attribute, which means the attributes can be defined from other attributes as well.
3. Class object attribute can be called us self.attribute or class_name.attribute.

Inheritance - 

We can make use of classes already defined in our new classes. Lets understand this with an example.

class Animal():

   def __init__(self):
      print("Animal Created")
   
   def who_am_i(self):
      print("I am an animal")
   
   def eat(self):
      print("I am eating")


class Dog(Animal): # the base class will be given within the parantheses

   def __init__(self):
      Animal.__init__(self) # To initialize the base class animal in the derived class dog
      print("Dog Created")

   def who_am_i(self):
      print("I am a dog") # this will over write the who_am_i method derived from the base class

my_dog = Dog()

my_dog.who_am_i() # will print "I am a dog", if the function is not wriiten in derived class it would result in "I am an animal"

'''