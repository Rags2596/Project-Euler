import time
t1 = time.time()
num = 3
rag = 2


def isPrime(x):
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0:
            return False
    return True

while rag < 10001:
    num +=2
    if isPrime(num):
        rag += 1
t2 = time.time()
print(num, t2-t1)
