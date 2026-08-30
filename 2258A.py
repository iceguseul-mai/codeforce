import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(math.gcd(a[0], a[n-1]))