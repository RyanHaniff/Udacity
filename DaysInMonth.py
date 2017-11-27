

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def howManyDays(monthNumber):
    return days_in_month[monthNumber - 1]

print (howManyDays(1))