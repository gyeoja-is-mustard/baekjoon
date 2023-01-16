a = input().upper()
result = []
for i in range(65,91):
    result.append(a.count(chr(i)))
if result.count(max(result)) >= 2:
    print("?")
else:
    print(chr(65+result.index(max(result))))