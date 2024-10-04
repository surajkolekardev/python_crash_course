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

#list_items.remove("suraj") # removed suraj from the list. remove() deletes only 1st occurance of value which we have dele


########################## Sort  Note: While sorting make sure all values will be in lowercase or uppercase. no upper lower.

#sort() method change order of the list permanently cannot store or create new list sort() apply on original variable of list., for reverse order use sort(reverse = True)

list_of_cars = ['bmw','audi','mercedeze','innova']
list_of_cars.sort()
print("###",list_of_cars) #['audi', 'bmw', 'innova', 'mercedeze']


list_of_cars = ['bmw','audi','mercedeze','innova']
list_of_cars.sort(reverse= True)
print(list_of_cars) #['mercedeze', 'innova', 'bmw', 'audi']



# Sort a list temporarily with the sorted function.
list_of_cars = ['bmw','audi','mercedeze','innova']

print("sorted list ", sorted(list_of_cars)) #sorted list  ['audi', 'bmw', 'innova', 'mercedeze']

print("original list", list_of_cars) #original list ['bmw', 'audi', 'mercedeze', 'innova']

 
sort_upper = ["BMW",'AUDI']

print(sorted(sort_upper )) #,reverse=True)) ['AUDI', 'BMW']


############# Printing a list in Reverse order reverse() --> here it will not sort just it will print in reverse order.

list_of_cars = ['bmw','audi','mercedeze','innova']

list_of_cars.reverse()
print("Reverse order", list_of_cars) #['innova', 'mercedeze', 'audi', 'bmw']


############ Finding lenght of list:


list_of_cars = ['bmw','audi','mercedeze','innova']
print("length of list", len(list_of_cars))

#Note: Python counts the items in a list starting with one, so you shouldn't run into any off-by-one errors when determining the length of list.



#Avoiding index error when working with an string

"""
Let's say you have three items, and you ask for the fourth item.

Index error means python can't find an item at the index you requested.

Keep in mind that whenever you want to access last item in a list you use the index-1, This will always work, even if your list has changed in size since the last time
you accessed.

"""
