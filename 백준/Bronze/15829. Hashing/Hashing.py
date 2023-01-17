l = int(input())
sum = 0
str = input()
for i in range(l):
    sum += (31**(i)) * (ord(str[i])-96)
print(sum%1234567891)