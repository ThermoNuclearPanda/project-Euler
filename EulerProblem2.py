
def euler2():
    i = 1
    i2 = 1
    sum = 0

    while(i2 < 4000001):
        itemp = i2
        i2 += i
        i = itemp
        if(i2 % 2 == 0):
            sum = sum + i2
    print(sum)
