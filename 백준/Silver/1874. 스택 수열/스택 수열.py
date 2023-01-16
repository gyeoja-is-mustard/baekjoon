n = int(input())
seq = [int(input()) for i in range(n)]
stack = []
stack_seq = []
num = 1
oper = []
for i in range(n):
    while True:
        if num <= seq[i]:
            stack.append(num)
            oper.append('+')
            num += 1
  
        else:
            a = stack.pop()
            stack_seq.append(a)
            oper.append('-')
            break
if stack_seq != seq:
    print('NO')
else:
    for j in range(len(oper)):
        print(oper[j])