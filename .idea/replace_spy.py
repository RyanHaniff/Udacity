

spy = [0, 0, 7]

def replaceSpy(list):
    list[2] = list[2] + 1

replaceSpy(spy)

def listLength(p):
    i = 0

    while i < len(p):
        print (p[i])
        i = i + 1


print (spy)

print ("length of lists:")
print (len(spy))

print("-----------")

listLength(spy)