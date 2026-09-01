import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,a,b = map(int, input().split())
    ans = (n // 3) * min(3 * a, b)
    ans += min((n % 3) * a, b)
    print(ans)