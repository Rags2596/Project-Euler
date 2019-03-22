import time
t1 = time.time()


def even(num):
    if num%2 == 0:
        num /= 2
    else:
        num = num*3 +1
    return num
x=3
temp = 0
coll_dict = {}
numx = 0
while x <= 1000000:
    i = x
    count = 1
    while i != 1:
        if i in coll_dict:
            count += (coll_dict[i]-1)
            break
        else:
            count += 1
        i = even(i)
    coll_dict[x] = count
    if count >= temp:
        temp = count
        numx = x
    x += 1

t2 = time.time()
print(numx, temp, t2-t1)










