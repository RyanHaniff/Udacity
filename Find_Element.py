

def find_element(list, match):

    count = 0

    for e in list:

        if e == match:
            return count

        count += 1

        return -1 #If e doesnt equal match then return -1






print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1