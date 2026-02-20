# import pyjokes

# joke=pyjokes.get_joke()
# print(joke)

import random #this is a random lib imported

def get_choices():
    # player_choice='rock' #this is a constant choice so for user input we use neeche wala code
    player_choice=input("Enter a choice (rock,paper,scissors)")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    # computer_choice="paper" #variable declare
    choices={"player":player_choice,"computer":computer_choice}
    # return player_choice 
    return choices

choices= get_choices()
print(choices) #now this will give whole dictionary as output, to access only the elements of a dictionary see dict dictionary

# in python we define functions with def and to indentate the function(indentate mtlb scope define krna ab c/c++ mai curly brackets se hota hai isme different hota hai) we will select the content of the function and click tab button

# dictionaries: in python it is used to store data values in key value pairs 
dict={"name":"kans","color":"blue","option":choices}
ele=dict["name"]#this will access the value assigned to name in dictionary

# libraries:python libraries are a set of useful functions so we do not need to write a code from scratch when we import any lib to our prgrm we get access to more features without writing any additional code. We need to import these lib before writing our code using import statement

# lists:used to store multiple items in a single variable eg.
# arrays Stores same type only whereas lists Can hold mixed types
food=["pizza","carrots","eggs"]
# now using random library we can pick random food item from food list as
dinner=random.choice(food)

# now by using this random choice feature we can also make computer choice variable in rps

def check_win(player,computer):#funct argument
    print(f"you chose {player}, computer chose {computer}")
    if player==computer:
        return "it's a tie!"
    # elif player=="rock" and computer=="scissors":
    #     return "rock smashes scissors! you win!"
    # elif player=="rock" and computer=="paper":
    #     return "paper covers rock! you lose!"

    # refactoring👇
    elif player=="rock":
        if computer=="scissors" :
            return "rock smashes scissors! you win!"
        else:
            return "paper covers rock! you lose!"
    
    elif player=="paper":
        if computer=="rock" :
            return "paper covers rock! you win!"
        else:
            return "scissors cuts paper! you lose!"

    elif player=="scissors":
        if computer=="rock" :
            return "rock smashes scissors! you lose!"
        else:
            return "scissors cuts paper! you win!"

# concatenating: this means to add two strings or one string and variable now this has two ways:
# 1)using + : print("hi my name is"+name) here name is a variable containing some string which is concatenated with hi my name is
# 2)f string: this concatenate the string in easier way as age=21 print(f"my age is {age})

# refactoring:process of restructing the code wile keeping the original functionality. refactor mtlb code ko or simpler bna dena like elif baar baar likhna pdega hame har ek situation ke liye uski bjaye refactoring kr denge

# in python space in the begining of any line indicates indentation

# DATA TYPES:
# to check the data type of any variablle we use type function 
name="bhupeshdii"
print(type(name))
print(type(name)==str) #here we check if the given variable is a str or not this can be achieved through isinstance which tells if the given variable is an instance of the provided data type for eg
print(isinstance(name,str))

# class constructor:we can convert one data type to another data type using class constructor, this conversion is known as casting. string can't be casted to int similarly not all dtata types can be converted or casted
age=2
print (isinstance(age,float))#this line will throw false as 2 is not a float value...but we can make it a float as
age=float(2)
print (isinstance(age,float))#this will now give true...similarly we can do this for integers or strings or other data types
# more data types:complex for complex nos.,bool,list,tuple,range,dict,set

# OPERATORS:
# 4**2->4power2; 4//2 (floor division)-it divides the no. and round off to the nearest whole no.
# boolean operators:&(AND),|(OR),^(XOR),~(NOT),<<(LEFT SHIFT),>>(RIGHT SHIFT)
# other kind of operator:is(identity operator=identify if both objects are similar or not), in(membership operator=it tells if a value is contained in a list or sequence)
name="goluba"
print("lu" in name)#this in will throw true if lu together is present in name otherwise false
# ternary operator: 
def is_adult(age):
    return True if age>18 else False

# STRINGS:
# if we need to print multi lines together we can do so by using three double/single inverted commas together like
print("""I lovee my goluu
he is my bholu bandarrrr
i will protect him from everyy evil in his lyf 
ohhh i am blushingg thinking abt him
he is mineeee""")
# .upper() converts a string into uper case,.lower to lower case,.title make first letter capital of each word
print("world".upper())
# .islower() checks if string is in lower case,isupper() upper case
# isalpha() checks if a strng cntns chars and is not empty
# isalnum() checks if a strng cntns chars  or digits and is not empty
# isdecimal() checks if a strng cntns digits and is not empty
# startsswitch()checks if a strng strts with a specific substring
# endsswitch()checks if a strng ends with a specific substring
# replace()replace a part of a string
# split() to split a string on a specific char seperator
# strip() to trim whitespacefrom strng
# join()append new letters to a strng
# find()fnd the position of a substring
# note: all the above functions doesnt affect the main string
print(len("kansuu"))#len give length of the string
# escaping charachters: this is used to add special caharacters inside a string likewise double inverted commas between a string,so this is done by escaping quote inside the string with backslash charachter
name="go\"lu"
print(name)
# backslash is also used in formatting for eg. if we need new line between characters of string then
name="be\nau"
print(name)
# now if we want to access particular letter from a string we can do by providing its index
name="beau"
print(name[3])
print(name[-2])
# slicing:by using this we can get all letters present between give index period
print(name[0:3])
print(name[:3])#this will return all the charachters till 3 strting from strt it can vise versa also setting a strt index and leaving end blank will return all the charachters from strt index till last

# BOOLEAN
done=True 
if done: print("yes")
else: print("no")
# any no. other then 0 is considered as true
# strings if empty are considered as false else true same for list tuple set dictionaries
done="True"
print(type(done)==bool) 
# any:it returns true if any value in the list or anything is true
book1=True
book2=False
print(any([book1,book2]))
# all: it return true if all values are true
print(all([book1,book2]))

# COMPLEX NUMBERS
# imaginary numbers along with real nos. are complex no. in maths its represented as i and in engineering its represented as j
num=2+3j 
# OR
num2=complex(2,3)
print (type(num))
print(num2.real,num2.imag)

# BUILT-IN FUNCTIONS
# abs:this function returns absolute value of a no. means modulus value of any no. |x|
print(abs(-4.9))
# round:rounds off the value to nearest whole no.
print(round(-4.49))
print(round(4.49,1))#this is one will not round it to whole no. but it will round to nearest tenths place or one decimal point

# ENUMS:these are readable names that are bound to a constant value so to use a noms we're going to have to import nums from the enum standard library module
# In Python, enum (short for enumeration) is a special data type that allows you to define a set of named constant values. 
# It helps make code more readable, organized, and less error-prone by giving meaningful names to fixed values
from enum import Enum
# now initialising new enum after importiong
class State(Enum):
    INACTIVE=0
    ACTIVE=1
# this state is a variable we have declared. we can use any name instead of state here
# now we have declared state.inactive=0 and state.active=1
print(State.ACTIVE)#this will only print State.active to access the valyue of this attribute we need to add .value
print(State.ACTIVE.value)
print(State(1))#this will give state.active as o/p
print(State.ACTIVE.name)
print(State['ACTIVE'])#apn ese bhi access kr skte hai State ke attributes or dot se bhi
print(list(State))#this will list all the values of state
print(len(State))#this will give length of state i.e 2

# USER INPUT:
# print("whats ur age?") # now instead of writing it like this on upper side of input we can write it in input bracket also
age=input("whats your age? ")
print("your age is: " + age)

# CONTROL STATEMENTS
condition=True

if condition==True:
    print("the condition")
    print("was true")
elif condiion==False:
    print("false")
else:
    print("nothing")

# LISTS:
# it allows us to group together multiple values and reference them all with a common name. we can store different data types value together
dogs=["roggy","tuffy","pluto","brownie",3]
# to check whether something belongs to the list we use in operator
print("kanika" in dogs)
# we can also declare an empty list like human=[]
# we can access the elements by their indexes as
print(dogs[0])
dogs[2]="beau" #this will update the particular index value
print(dogs)
# now we can also access these elements using negative index such that -1 indicates last index i.e 3
print(dogs[-1])
# we can also extract part of a list by using slicing method 
print(dogs[2:4]) #this will give 2nd and 3rd index element
print(dogs[:3])
print(dogs[3:])
print(dogs[::2])#this will skip every second element and give alternate element
print(len(dogs))
# to add items to the list we use append method
dogs.append("bhura")# we can add one element at a time
print(dogs)
# append mai puri list ek nyi add kr skte hai but ek he list like dogs.append(["doggy",1,3,"poki"])
# we can also use extend instead of append
# we can also add elements using += operator like dogs+=["judah",5]; here if we don't use square brackets and directly write dog+="judah"
# then it will add each letter as an element as "j" "u" "d" "a" "h" like this
dogs.remove("bhura")
print(dogs)
print(dogs.pop())#this will pop and return the last inserted element
# how to add items/elements in the middle of the list or at specific location
dogs.insert(3,"quincy")#so at index 3 quincy is inserted
print(dogs)
# to add multiple item at a specific location we need to use slices
dogs[1:1]=["abc","def"]#this means 1st index se lekr 1st index tk he abc def likh do
# dogs[1:2] this will replace second index with the elements given in this
print(dogs)
# we can also sort the list but the list should contain same data type elements
human=["bholu","daku","aaryan","bhupesh","Tiu","kansu"] #elements starting with capital letters come first in sorted order like b/w Ab and ab Ab>ab
# i.e in sorting uppercase letters are sorted first and then lowercase to avoid this we can write human.sort(key=str.lower)
human.sort()
print(human)
# since sorting affects the original list so we need to copy our original list in another list this can be done using slicing
humancopy=human[:]
# we can also sort our list without affecting the original list by using sorted function sorted(list_name,way to sort the list)
print(sorted(human,key=str.lower))
dog1,dog2,dog3,dog4,dog5,dog6,dog7=dogs#this is unpacking-> assigning each value together to diff variables of a lsit
print(dog1)
print(dog2)
print(dog3)
# now if we want ki 1st element ek variable mai aaye or rest saare dusre mai we can write this as
dog1, *dog2=dogs
print(dog1)
print(dog2)

# TUPLES
# A Tuple is a collection in Python, similar to a list.But it is immutable → meaning once created, you cannot change, add, or remove its elements.
names=("roger","syd")
names[0]
names[-1]
names.index("roger")
len(names)
print("roger" in names)
names[0:2]
print(sorted(names))#this will not manipulate original tuple
newTuple=names+("tina","quincy")
tup=("x","y")
tup2=("z","a")
tup+=tup2
print(tup)
# initial tup and this alterd tup doesn't have same id location cz tuples are immutable while if here in place of tuple,list was present then id would have been same cz list is mutable
tuple(range(5))#this will o/p counting from 0 to 4 cz this is an iterable tuple
tuple(range(1,101,2))#this will print every odd no. between 1 to 101 cz we added 2 so it will jump 2 times so after 1 2jumpes =3

# DICTIONARIES
# it allows us to create key value pair unlike lists which is collection of values
dog={"name":"Tuffy","age":5}
print(dog["name"])
dog["name"]="brony"
print(dog)
# another method to access specific element is by using get
print(dog.get("name"))
'''in previous way of accessing, if by any chance we give any key which is not present in the dictionary
then it will give error whereas using get if we entered any unknown key it will give none as output. We can also set any default value for any unknown key that means if the key is not present in the dictionary then it will give that default value as the output but if the key is present then in place of default key it will give the key value as output'''
print(dog.get("color"))
print(dog.get("color","brown"))
print(dog.pop("name"))
print(dog)
# print(dog.popitem())#this will pop the last item inserted into the dictionary
print("color" in dog)#if this key exist it returns true werna false
print(dog.keys())#shows all the keys of the dictionary
# this uper keys will be in a list called dict_keys to get only keys we can add these keys in a list
print(list(dog.keys()))
#same we can do for values
print(dog.values())
print(list(dog.values()))
print(list(dog.items()))#this will return all the items of a dictionary in a list
len(dog)
dog["fav food"]="meat"#this adds new key value pair to the dict
print(dog)
del dog["fav food"]
dogCopy=dog.copy()#this will copy one dict to another

# SET
# kind of work like tuples but they're not ordered and immutable
names1={"roger","syd","roger"}
names2={"roger"}
# these sets work like maths sets 
intersect=names1 & names2 
print(intersect)#intersect is a variable 
union=names1|names2
print(union)
diff=names1 - names2
print(diff)
# we can also check if a set is a superset of another or a set is a subset of another
sup=names1>names2
print(sup)
sub=names1<names2
print(sub)
print(len(names1))
print(list(names1))#getting a list from set
# we can also check if an element is contained in a set using in operator
print("roger" in names1)
# a set cannot have two of the same item like if we have 2 roger it will print only once
print(names1)

# FUNCTIONS
# set of instructions that we can run when needed
def hello(name="roger"):#function definition with parameter
    print('hello!'+name)

hello('beau') 
hello()#here we didn't pass any argument so we will pass a defalt parameter which will show if we don't pass the argument

def change(value):
    value=2

val=1
change(val)
print(val)#here value of val will be 1 cz its immutable
# but if we pass a dictionary in place of a no. it will be muttable
def dicti(value):
    value["name"]="syd"

val={"name":"beau"}
dicti(val)
print (val)
# function can also return a value
def hello(name):
    print('hello '+name+" !")
    return name

hello("beau")
def hello(name):
    if not name:
        return
    print('hello ' + name +' !')

hello(False)
def hello(name):
    print('hello' +name)
    return name, "beau",8 #multiple return
print(hello("syd"))

# VARIABLE SCOPE
age=8 #global variable now we can access it inside and outside the function
def test():
    # but if we declare any variable here inside the function then we can't access it outside
    print (age)
print(age)
test()

# NESTED FUNCTIONS
def talk(phrase):
    def say(word):
        print(word)
    words=phrase.split(' ') #split splits each word of the phrase in print them individually basically it makes list of each word out of the phrase 
    for word in words: #loop
        say(word)

talk('I am going to buy the milk') 
# nonlocal: if we want to access a variable from outer function to inner function we use nonlocal it refers to the neareest defined variable
def count():
    count=0
    def increment():
        nonlocal count
        count+=1
        print(count)

    increment()
count()

# CLOSURES
# special way of doing a function if we return a nested funct from a funct that nested function has access to the variable defined in that function even if that funct is not active anymore
def counter():
    count=0
    def increment():
        nonlocal count
        count=count+1
        return count
    return increment
increment=counter()
print(increment())
print(increment())
print(increment())
# in the above function count will not reinitialise to 0 every time we call it, so increment function will still have access to variable even after counter funct has ended

# .bit_length() gives no. of bits required to represent a no. or used by a no.

# OBJECTS- everything in python is obj data type, variable,sets,list etc.
age=8
print(id(age)) #id gives the location 
age=age+1
print(id(age))
# in this age=8 is stored at different id and age=9 is stored at diff becoz int is immutable obj so at id of age=8 it cannot chnge its value so it assigns new id to age=9
# int,float,str,bool,tuple,frozenset are immutable | list,dict,set are muttable

#LOOPS:1)while 2)for
count=0
while count<10:
    print(count)
    count+=1
print("break")
items=[1,2,3,4,5]
for item in items:
    print(item)
    # this item written can be given any name as a variable cz its a variable
# we can also iterate without a list using range
for item in range(10):
    print(item)
# now if we want to access the index then we need to wrap the sequence in enum funct
for index, item in enumerate(items):
    print (index, item)
    # if we don't print index here then also it will display the index

# BREAK AND CONTINUE:continue stops the current iteration and tells python to execute the next one and break stops the loop altogether and goes on with next instruction after the loop ends
for item in items:
    if item==2:
        continue
    print(item)
for item in items:
    if item==2:
        break
    print(item)

# CLASSES
# an obj is an instance of a class and a class is the type of an obj
class dog:
    def __init__(self,name,age):#this is a constructor. A constructor is a special method called init here we have defined self,name,age self is roger so everywhere roger object will be called in place of self
        self.name=name
        self.age=age
    def bark(self):#method: it is a function defined under a class
        print("woof!")
    
# creating an object
roger=dog("lebra",3)
print(roger.name)
print(roger.age)
roger.bark()
# due to writing print the terminal is showing none 
# inheritance->
class Animal:
    def walk(self):
        print("walking...")

class cow(Animal):#inherited from Animal class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sound(self):
        print("muuuuuu!!")

nandi=cow("nandi",4)

print(nandi.name)
print(nandi.age)
nandi.sound()
nandi.walk()
# inside a class in order to access a variable in multiple functions also called methods the variable has to strt with self dot

# MODULES
# every python file is a module. we can import modules from other files
# import main #this main.py is imported here and the function written there works here...this way I am importing the whole file
# main.bark()
# we can also just import the function using from
# from main import bark
# bark()
# now if this main.py is inside a subfolder then to access it we need to make an empty file in that subfolder named __init__.py and then we can import any file using the below command
# since we have a python version>3.3 installed on our device therefore we don't need an empty init file to import the existing file we can import that file without init file also
# this init files tells python that folder contains modules 
# from exam import main
# main.bark()
# or we can reference the main module specific function from subfoldername.main
# from exam.main import bark
# bark()
# python has a lot of built in libraries which need to be imported it has bunch of codes which can be directly used it provides lots of functionalities some libraries are
import math # math for math utilities
print(math.sqrt(4))
from math import sqrt
print(sqrt(4))
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage urls

# ACCEPTING ARGUMENTS FROM COMMAND LINE
# ye sb main2.py mai likha hai

# LAMBDA FUNCTION
# also called anonymous function are tiny funct that has no name nd only 1 expression as their body they are defined using lambda keyword
lambda num:num*2
# lmbda keywrd argument=expression
# difference btw expression and statement is exp returns a value and statement doesnot
multiply= lambda a,b: a*b
print(multiply(2,4))
# so utility of lambda function comes with combination of map filter reduce etc

# MAP, FILTER, REDUCE
# map()->used to run a function upon each item in an iterable item like a list and create a new list with same number of item but the values of each item can be changed
nums=[1,2,3,4]
# def double(a):
#     return a*2
    #now in place of the above function we can use a lambda function
double=lambda a:a*2 #also in place of assigning this lambda function to double we can directly write this lambda function in map parenthesis, there will be no use of double variable
result=map(double,nums)
print(list(result))
# filter()->it takes an iterable and returns a filter object
# def isEven(n):
#     return n%2==0
# isEven=lambda a:a%2==0
result=filter(lambda a: a%2 == 0,nums)
# If isEven(n) returns True, that element is included in the result. If it returns False, the element is skipped.
print(list(result))
# In short: filter() only keeps the elements for which the function returns True.
# reduce() -> used to calculate value out of sequence like a list
expenses=[#this is a list stored as tuple
    ('dinner',80),
    ('car repair',200),
    ('electricity',100)
]
# suppose we need to calculate sum of expense so here is the long way without reduce
# sum=0
# for expense in expenses:
#     sum+=expense[1]
# print(sum)
# for reduce we need to import lib
from functools import reduce
sum=reduce(lambda a, b: a + b[1], expenses,0)
# here reduce(reduction function, iterable) here 0 at the end initialise a=0
# reduction funct contains 2 arguments a-accumulated value(total value) b-updated value from the iterable
print(sum)

# RECURSION:funct calling itself
# factorial
def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)
print(factorial(3))

# DECORATORS
# way to change, enhance, alter in any way how a function works. decorator is defined with at the rate symbol followed by decorator name jst before the function definition
def logtime(func):#decorator defined with another function func passed in it
    def wrapper():#this decorator has another function inside it
        print("before")
        val=func()#the func function passed as an argument is called.this func actually calls hello() function thats why hello is printed in between
        print("after")
        return val
    return wrapper
@logtime #this line represents hello=logtime(hello) hello is passed as an argument to logtime which is passed to func
def hello():
    print("hello")
hello()  
# Flow in plain English. You define hello. @logtime wraps hello by passing it into logtime. So now func = hello. logtime returns wrapper. Now hello actually points to wrapper. When you call hello(), it runs wrapper(). Inside wrapper(), the line func() calls the original hello.  

# DOCSTRINGS
# jaise mai comments likhti hu jst to understand the code afterwards so another way to do so is docstring
class dog:
    """class of dog"""
    def __init__(self,name,age):
        """constructor"""
        self.name=name
        self.age=age
    def bark(self):
        print("woof!")

# print(help(dog)) #this will print its documentation i.e everything along with matter written between """"

# ANNOTATIONS
# python is dynamically typed so we don't have to specify type of variable or function parameter or its return value, Annotations allow us to optionally do that
def increment(n:int)->int:
    return n
# n:int means argument passed should be int and ->int means function return should also be int
count :int=0#we are specifying that this variable is going to be an integer

# EXCEPTIONS
# its imp to handle errors nd python gives us exception handling to do so. we wrap our code in try blcok and error will be in except block
# try:
    # some line of code
# except <ERROR1>:    this block handles particular errors specified in their block to handle all the errors we use only except   
    # handler <ERROR1>
# except <ERROR2>:
    # handler <ERROR2>   
# except:
    # errors if any
# or we can add else block that will run if no exceptions are found
# and then we have finally block which runs at the end whether ther are exceptions or there are no exceptions

# result=2/0
# print(result) this alone will give error so...
try:
    result=2/0
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    result=1
print(result)
# we can raise error on our own intentionally
# raise Exception('O|O !!')
try: 
    raise Exception('O|O !!')
except Exception as error:
    print(error)
# we can also define our own exception class extending from exception
class DogNotFoundException(Exception):#pass is written when a class is defined without method or a function without code
    pass
try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found")

# WITH:in exception handling working with 'with' becomes easy like when we open a file we must remember to close it with makes the process more transparent
filename='C:/Users/HP/python/projects/RPS.py'
# try:
#     file =open(filename,'r') 
#     content=file.read()
#     print(content)
# finally:
#     file.close()
# this above is the manual way to do so but using with we don't manually needs to cloase the file it automatically closes the file

with open(filename , 'r') as file:
    content=file.read()
    print(content)

# INSTALLING PACKAGES:python standard library cntains a huge no. of utilities that simplify our python development needs but nthng can satisfy evertrhing
# thats why companies or individuals create packages and make them available as open source s/w for entire community so the modules are all collected in a single place called python package index(pip) which is available at pypi.org and they can be installed using pip
# pip-> on terminal we will install request package it's an http library
# pip install -U packagename for latest version of package
# pip show packagename for details of package

# LIST COMPRESSION:way to create a list in a very concise way
nos=[1,2,3,4,5]
# for eg we need a list with all the nos power 2
# num_pow2=[]
# for nums in nos:
#     num_pow2.append(nums**2)
# print(num_pow2)
# using list compression
num_pow2=[nums**2 for nums in nos]
print(num_pow2)
# we can do so by map but compression is more easier then map also

# POLYMORPHISM: it generalises a functionality so it can wrk on diff types
class dog:
    def eat(self):
        print("the dog eats")
class cat:
    def eat(self):
        print("the cat eats")
Animal1 =dog()
Animal2 =cat()

Animal1.eat()
Animal2.eat()

# OPERATOR OVERLOADING:advance technique we can use to make classes comparable and to make them wrk with python operators
# doubt


#Some Basic Concepts:
job1="Data Analyst"
job2=job1
print(id(job1),id (job2))
# if we assign one variable value to another they both have same location/id

my_func=print
my_func("hii") #this line will print hii cz my_func=print function
# these data types like int,str are kind of classes and when we define variables they become the objs of these classes

salary=100
# help(int)
print(salary.__add__(2))

role="data analyst"
skill='python'
print("role {}".format(role)) #.format will print the value of variable inside() in {}

# if we need to  get binary value of a no. we use bin function
print(bin(4))

salaries=[1000,300,2000,15,570]
print(min(salaries))
# print(sum(salaries)) ye isliye error hai shyd kyuki sum khi upr define kr rkha hoga ye usko call kr rha hai or error de rha hai
print(max(salaries))
print(sorted(salaries))