import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    for i in range(1, n):
        if i < a[i]:
            a[i+1] += a[i]-i
            a[i] -= (a[i]-i)
    flag = True
    for i in range(2, n+1):
        if a[i] <= a[i-1]:
            flag = False
            break
    print("YES" if flag else "NO")