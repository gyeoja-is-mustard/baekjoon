import math

n = int(input())
print(int(2*(n - 2**(math.ceil(math.log2(n))-1))))