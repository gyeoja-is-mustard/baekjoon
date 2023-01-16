a = input()
while 'c=' in a:
    a = a.replace('c=','1') 
while 'c-' in a:
    a = a.replace('c-','2') 
while 'dz=' in a:
    a = a.replace('dz=','3')
while 'd-' in a:
    a = a.replace('d-','4')
while 'lj' in a:
    a = a.replace('lj','5')
while 'nj' in a:
    a = a.replace('nj','6')
while 's=' in a:
    a = a.replace('s=','7')
while 'z=' in a:
    a = a.replace('z=','8')
print(len(a))