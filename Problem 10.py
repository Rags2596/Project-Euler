import time
t1 = time.time()
total = 5
x = 3

def isPrime(x):
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0:
            return False
    return True

for i in range(5,2000000,2):
    if isPrime(i):
        total += i


t2 = time.time()
print(total, t2-t1)
