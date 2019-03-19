import time
t1 = time.time()
def factors(triangle):
    prime_dict = {}
    while triangle%2 == 0:
        triangle /= 2
        try:
            prime_dict[2] += 1
        except KeyError:
            prime_dict[2] = 1
    for i in range(3, int((triangle+1)**0.5)+1, 2):
        while triangle%i == 0 and i != triangle:
            triangle /= i
            try:
                prime_dict[i] += 1
            except KeyError:
                prime_dict[i] = 1
    prime_dict[triangle] = 1
    count = 1
    for key, value in prime_dict.items():
        count = count*(value+1)
    return count
z = 0
i = 1
while z<500:
    z = factors((i*(i+1))/2)
    i+=1
t2 = time.time()
print(sum(range(i)), t2-t1)

