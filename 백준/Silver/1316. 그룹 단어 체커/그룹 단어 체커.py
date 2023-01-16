def group(b):
    for j in range(97,123):
        if chr(j) in b:
            if b.count(chr(j)) != len(b) - b.find(chr(j)) - b[::-1].find(chr(j)):
                return False
    return True
a = int(input())
result = 0
for i in range(a):
    b = input()
    if group(b):
        result += 1
print(result)