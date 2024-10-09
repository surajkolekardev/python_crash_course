"""
# Case 1:
inputs:
    "pikachu", "togepi"
output:
    ["p", "i"]
 
# Case 2:
inputs:
    "arbitrary", "lemon"
output:
    []
 
# Case 3:
inputs:
    "testimonial", "ants"
output:
    ["a","n","t","s"]
 
"""
 
def get_common_chars(str1, str2):
    common_items = set(str1).intersection(str2)


    return list(common_items)

str1 = "pikachu"
str2 = "togepi"
result = get_common_chars("testimonial", "ants")
print(result)


"""
select * from table1 inner join table1 user_id = purchase_id

"""