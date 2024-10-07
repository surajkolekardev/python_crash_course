######### Working with a list


print("************************************  Loping through and entire List & A Closer Look at looping  ***********************")

magicians = ['alice', 'david','carolina']

for magician in magicians:  # ** This line tells python to pull a name from the list magicians, and associate it with the variable magician 
    print(f"{magician.title()}, That was a great trick") #Alice, That was a great trick, Same for the remaining items.
    print(f"I can't wait to see your next trick, {magician.title()}")

print("\nThank you everyone. That was a great magic show.")  

"""
    Output:
        Alice, That was a great trick
        I can't wait to see your next trick, Alice
        David, That was a great trick
        I can't wait to see your next trick, David
        Carolina, That was a great trick
        I can't wait to see your next trick, Carolina

        Thank you everyone. That was a great magic show.
"""
"""set of steps is repeated once for each item in the list
    naming convention:
        for cat in cats:
        for dog in dogs:
        for item in list_of_items:
    Conventions can help you follow the action being done on each item within a for loop

    Note: When you're processing data using a for loop, you'll find that this is a good way to summarize an operation that was performed on an entire data
        set. and write print statement after one line of gap between loop and summarize print.

    Syntax Error:
        If you miss colon after loop or indentation the it will through syntax error:

    Logical error:
        If you write some line outside loop but that lines should be inside loop or vice versa that's the logical error it won't display any error on consol but it diff in output.    
    """


print("************************************ Making Numerical List ***********************")

#Using the range() function --> range(start,stop,step)
# Range() exclude last item. e.g range(1,5) it will print 1,2,3,4 not 5th one, its another example of off byu one.


#Using range make list of numbers

numbers = list(range(1,6))
print(numbers) # [1, 2, 3, 4, 5]
 

print("************************************ Simple statistic with a list of Numbers ***********************")

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

print("************************************ List Comprehension ***********************")

# suppose we have print list then we have to write 4 lines of code instead of that we can write in one line

squ_number = [f"The square of {item} is {item * item}" for item in range(5)]
print("\n".join(squ_number))



print("********************** Slicing a list *********************")
# for indexing you have to give first and last element to start or stop, like range() here python will stop one item before the 2nd index.
#Omit first index like players[:3]
#Omit last index like players[2:]  start from 2nd till last element.
players = ['suraj','kolekar','bob','joy','martin']
print(players[2:4]) #'bob','joy' 4th index is excluded like range() method.

# Negative index: for e.g if we want last three palyer
print(players[-3:])

print("********************** copy list using slicing *********************")

my_food = ['pizza','icecream','carrot cake']

friend_foods = my_food[:] #here my_food copied to this variable if i add one more food in my_food that will not change in friend_foods and vice verce


################### copying list 

friend_foods = my_food # Here it will copy list same as my_food but if you add item in my_food then it will also add in friend_food and same.
#the output of both list are same now.


#################################  TUPLE ##########################################

   
print("********************** Properties of tuple  *********************")
# Sometimes you'll want to create a list of items that cannot change. Tuple allows to do just that. Python refers to values that cannot change 
#as an immutable and immutable list is called tuple.


tuple_item = ('suraj','kolekar')

# Note: If you want to define tuple with one item then you need to include a trailing comma:

# Looping through all the values in tuple

for item in tuple_item:
    print(item)


#### Styling your code

# use 4 space indentation
# Use blank line  two separate two code section or logic.
