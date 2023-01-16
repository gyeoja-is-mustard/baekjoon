m, n = map(int, input().split())
multiple_m = m
multiple_n = n
cd_list = [i for i in range(1, min(m,n)+123) if (m%i == 0 and n%i == 0)]
gcd = cd_list[-1]
while multiple_m != multiple_n:
    if multiple_m > multiple_n:
        multiple_n += n
    else:
        multiple_m += m
lcm = multiple_m
print(gcd)
print(lcm)