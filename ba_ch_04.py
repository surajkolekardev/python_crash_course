######### Working with a list


print("************************************  Loping through and entire List & A Closer Look at looping  ***********************")

magicians = ['alice', 'david','carolina']

for magician in magicians:  # ** This line tells python to pull a name from the list magicians, and associate it with the variable magician 
    print(f"{magician.title()}, That was a great trick") #Alice, That was a great trick, Same for the remaining items.
    print(f"I can't wait to see your next trick, {magician.title()}")

print("\nThank you everyone. That was a great magic show.\n")  

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


print("************************************  A Closer Look at looping  ***********************")

 