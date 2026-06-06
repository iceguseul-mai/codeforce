import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(input().rstrip())
    blank = a.count('?')

    if blank != n:
        while blank > 0:
            for i in range(n):
                if a[i] == 'R':
                    if i != 0 and a[i-1] == '?':
                        a[i-1] = 'B'
                        blank -= 1
                    if i != n-1 and a[i+1] == '?':
                        a[i+1] = 'B'
                        blank -= 1
                elif a[i] == 'B':
                    if i != 0 and a[i-1] == '?':
                        a[i-1] = 'R'
                        blank -= 1
                    if i != n-1 and a[i+1] == '?':
                        a[i+1] = 'R'
                        blank -= 1
        print(*a, sep='')         
    else:
        print('BR'*(n//2)+'B'*(n%2), sep='')