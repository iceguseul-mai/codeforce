import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    c = list(map(int, input().split()))
    ans = 1
    for x in range(1, m+1):
        cnt = 0
        for i in c:
            if i == x*2:
                cnt += 1
            if x <= i:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)