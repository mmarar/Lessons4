x = 1

def func(x):
    y = 2
    while y <= x / 2:
        if x%y == 0:
            return False
        y += 1

while x != 0:
    x = input("Input x ")
    if func(x) == False:
        print "Prime number"
    else:
        print "Composite number"
