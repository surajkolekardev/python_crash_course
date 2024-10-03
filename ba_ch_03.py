"""
List is a collection of items in a particular order
We can store anything inside list like list of plurals, digits, letters, or names.
In python, Square brackets ([]) indicate a list. and individual element in a list separated by comma.
"""

########## Accessing Element in a List

# Lists are ordered collections, so you can access any element in a list by telling python the position or index.
# Write name of the list followed by index.

list_items = ["suraj","kolekar","pune"]
print(list_items[1]) # kolekar





################# Index postitions start at 0 not 1
 
# Reason --> How the list operations are implemented at a lower level.

# Negative index --> index -1 means python will return last element in a list.


############## Using individual values from a list.

# append() --> add element to the end of the list

list_items.append("elpro")

# insert() --> add element wherever you want in the list its just you need to know the index first.

list_items.insert(2,'bullet') # it will add bullet at 2nd index and this operation shifts every other value in the list one position to the right.
print(list_items)

# Removing an item using the del statement:

#if you know the position of item you want to remove from a list, you can use the del statement.
#['suraj', 'kolekar', 'bullet', 'pune', 'elpro']
del list_items[2] # bullet will delete.


#Removing item using pop() method:

# for pop() method removed last element from the list, and it will return removed element so you can work with it.


poped_item = list_items.pop()  # last element removed and stored in poped_item variable

list_items.pop(0) # --> 0th index element is removed.

list_items.remove("suraj") # removed suraj from the list. remove() deletes only 1st occurance of value which we have deleted.
