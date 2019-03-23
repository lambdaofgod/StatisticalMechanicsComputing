m = 134456
n = 8121
k = 28411
idum = 1000
numbers = list(range(m))
for x in range(m): numbers[x] = 0
for iteration in range(200000):
    idum = (idum *  n + k) % m
    ran = idum / float(m)
    numbers[idum] += 1
    #print idum, ran, iteration
print([x for x in numbers if x!=0])
print(sum(numbers[x] for x in range(m)))
