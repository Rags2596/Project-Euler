import time
t1 = time.time()

file = open('D:/Project Management/Py Projects/100 Numbers.txt', 'r')
total = 0
for x in range(52, 5201, 52):

        num = file.read(11)
        file.seek(x, 0)
        total += int(num)
t2 = time.time()
print(total, t2-t1)
