import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = list(input().rstrip())
    ans = 0
    while n[len(n)-1] == '0':
        ans += 1
        n.pop()
    for i in range(len(n)-1):
        if n[i] != '0':
            ans += 1
    print(ans)