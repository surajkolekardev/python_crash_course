########### Variables ########

pune_address = "elpro city square pune"
print(pune_address)


########## Strings ############
"""
String is datatype
String is series of characters, anything inside a quotes considered a string in python.
e.g
    "This is a string"
    'this is a string'

    ' I told my friend, "Python is my favorite language" '
    
"""

####### Changing case in a string with methods:

name = "suraj kolekar"

print(name.title()) # title method convert each words first letter in capital. --> Suraj Kolekar
print(name.upper()) # All string convert into uppercase. --> SURAJ KOLEKAR
print(name.lower()) # All string convert into lowercase. -->suraj kolekar

# The lower() methodd is perticularly userful for storing data. Many times you won't want to use the capitalization that your users provide, so you will
#convert strings to lowercase before storing them. Then when you want to display the information, you will use the case that makes the most sense for each string.



########## Adding whitespace to strings with tabs or newlines

# tab       ----> \t  print("\tSuraj") -->  Suraj
# new line  ----> \n  print("languages:\npython\njava\nC")  --->languages:
                                                                #python
                                                                #java
                                                                #C

######### Stripping whitespaces

str = "suraj "
print(str.rstrip()) # "suraj" removed right side space of the string.

str = "     suraj"
print(str.lstrip()) # "suraj" removed left side space of the string.

 



###### Numbers

#Integers

print(2+4)
print(2**2) #4
print(3**3) #27

#Float

print(0.2 + 0.2) #0.4

########## Integer and float
#When you divide any two numbers, even if they are integers that result in a whole number, you will always get a float:

# 4/2   --> 2.0

#Note: If you mix integer and float in any other operation, you'll get a float as well.

print(1 + 2.0) # 3.0


########## Underscores in numbers:

#When you're writing long numbers, you can group digits using underscores to make large numbers more readable:
universal_age = 14_00_00_00
print(universal_age) # 14000000
#Python ignores the underscore when storing these kind of values.


######### Multiple assignments:
x, y, z = 0, 0, 0  #Here python will assign each value to its respectively positioned variables..

######## Constants
MAX_CONNECTIONS = 5000 # Make the name of the variable all capital letters.


#Comments:

#Say hello to everyone



###################################### Summary ############################################

#str.capitalize()
s = "hello world"
print(s.capitalize())  # Output: "Hello world"

# str.lower()
s = "Hello World"
print(s.lower())  # Output: "hello world"

# str.upper()

s = "hello world"
print(s.upper())  # Output: "HELLO WORLD"


str.title()

s = "hello world"
print(s.title())  # Output: "Hello World"


# str.strip()

s = "   hello   "
print(s.strip())  # Output: "hello"
str.lstrip() / str.rstrip()

s = "   hello   "
print(s.lstrip())  # Output: "hello   "
print(s.rstrip())  # Output: "   hello"


# str.replace(old, new)

s = "hello world"
print(s.replace("world", "Python"))  # Output: "hello Python"


# str.split(separator)

s = "apple,banana,grape"
print(s.split(","))  # Output: ["apple", "banana", "grape"]

# str.join(iterable)

fruits = ["apple", "banana", "grape"]
print(", ".join(fruits))  # Output: "apple, banana, grape"


# str.find(substring)
s = "hello world"
print(s.find("world"))  # Output: 6


# str.index(substring)
s = "hello world"
print(s.index("world"))  # Output: 6


# str.count(substring)
s = "hello world hello"
print(s.count("hello"))  # Output: 2


# str.startswith(prefix)
s = "hello world"
print(s.startswith("hello"))  # Output: True


# str.endswith(suffix)
s = "hello world"
print(s.endswith("world"))  # Output: True


# str.isdigit() / str.isalpha() / str.isalnum()
s1 = "12345"
s2 = "hello"
s3 = "hello123"
print(s1.isdigit())  # Output: True
print(s2.isalpha())  # Output: True
print(s3.isalnum())  # Output: True


# str.islower() / str.isupper()
s1 = "hello"
s2 = "HELLO"
print(s1.islower())  # Output: True
print(s2.isupper())  # Output: True


# str.center(width)
s = "hello"
print(s.center(10))  # Output: "  hello   "


# str.zfill(width)
s = "42"
print(s.zfill(5))  # Output: "00042"

# str.format()
name = "Alice"
age = 25
print("My name is {} and I am {} years old".format(name, age))
# Output: "My name is Alice and I am 25 years old"