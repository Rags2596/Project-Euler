import math
import time
t1 = time.time()
p_list = []
for i in range(4,1000):
    for j in range(3,i):
        x = math.sqrt(i ** 2 + j ** 2)
        if int(x) == x:
            p_list = [j, i, int(x)]
            break
    if p_list[0] + p_list[1] + p_list[2] == 1000:
        break

t2= time.time()
print(p_list, t2-t1)
