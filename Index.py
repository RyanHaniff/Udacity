
# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(list, match):

    if match not in list:
        return -1
    return list.index(match)



print find_element([4,5,6], 6)


print (find_element([1,2,3],3))
#>>> 2

print (find_element(['alpha','beta'],'gamma'))
#>>> -1