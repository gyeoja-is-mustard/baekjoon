M, N = input().split()
sieve = [True]*(int(N)+1)
sieve[0] = False
sieve[1] = False
for i in range(2, int(N)+1):
    if sieve[i] == True:
        j = 2
        while i * j <= int(N):
            sieve[i*j] = False
            j += 1

for j in range(int(M), int(N)+1):
    if sieve[j] == True:
        print(j)