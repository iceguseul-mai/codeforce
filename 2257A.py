import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    allow = set()
    for _ in range(n):
        allow.add( list(input())[0].upper() )
    flag = True
    for _ in range(m):
        ab = list(input().rstrip())
        for i in range(len(ab)):
            if ab[i] not in allow:
                flag = False
                break
    if flag: print("YES")
    else: print("NO")