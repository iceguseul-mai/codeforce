import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if max(a[i],a[i+1]) - min(a[i],a[i+1]) == math.gcd(a[i],a[i+1]):
            ans+=1
    print(ans)