result = set()
for i in range(10):
    A_i = int(input())
    result.add(A_i%42)
print(len(list(result)))