import math, random

beta = 1.0
N = 8
sigma = math.sqrt(beta / N)
xend = 1.0
Upsilon = [0.0]
for k in range(N):
	#Generate the random walk path
    Upsilon.append(random.gauss(Upsilon[-1], sigma))
#Pull back to the xend position
x = [0.0] + [Upsilon[k] + (xend - Upsilon[-1]) * \
             k / float(N) for k in range(1, N + 1)]
print(x)
