import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    frosting = list(map(int,input().split()))
    prefix = 0
    ans = []
    cur = 10**18

    for i,x in enumerate(frosting, 1):
        prefix += x
        cur = min(prefix // i, cur)
        ans.append(cur)
    
    print(*ans)
        