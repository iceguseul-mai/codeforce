import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = list(input())
    stk = 0
    for i in range(len(a)):
        if a[i] == '3' or a[i] == '1':
            stk += 1
        elif a[i] == '4':
            a[i] = '0'
        elif a[i] == '2' and stk != 0:
            stk -= 1
            a[i] = '0'
    print(a.count('0'))

# 12
# 32

# 3000103