
def euler1():
    sum = 0
    for i in range(3,1000):
        if(i%5 == 0 or i%3 == 0):
            sum = sum + i
    print (sum)
