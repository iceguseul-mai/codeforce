import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l,a,b = map(int, input().split())
    ans = 0
    visit = [0 for _ in range(l)]
    while visit[a] == 0:
        visit[a] = 1
        ans = max(ans, a)
        a = (a+b) % l
    print(ans)
