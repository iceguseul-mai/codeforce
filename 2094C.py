import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = [0 for _ in range(n*2)]
    to_add = set([n for n in range(1, n*2+1)])
    for i in range(n):
        for j in range(n):
            ans[i+j+1] = a[i][j]
            to_add.discard(a[i][j])
    print(*(list(to_add) + ans[1:]))