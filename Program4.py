x = 10

while x < 100:
    y = x/10
    z = x%10
    #print y, z debug print
    if abs(y-z) == 1:
        print "---",x,"---"
    x += 1