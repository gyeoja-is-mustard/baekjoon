N = int(input())
num = 0
for i in range(N//2+2):
    num += i
    if N <= num:
        a = i+1 
        break
n = N-(a-2)*(a-1)/2
if a%2 == 0:
    print('%d/%d' %(a-n, n))
else:
    print('%d/%d' %(n, a-n))