import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = ['0' for _ in range(n)]
    prf_max = 0
    prf_min = 10**6+1
    for i in range(n):
        if min(prf_min, a[i]) == a[i]:
            ans[i] = '1'
            prf_min = a[i]
    for i in range(n-1, -1, -1):
        if max(prf_max, a[i]) == a[i]:
            ans[i] = '1'
            prf_max = a[i]
    print(*ans, sep='')