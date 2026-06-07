import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(input().rstrip())
    if n > 2:
        for i in range(n):
            if i != 0 and i != n-1:
                if a[i-1] != '1' and a[i+1] != '1':
                    a[i] = '1'
        print(a.count('1'))
    else:
        print(1)