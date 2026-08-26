import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = list(str(input()).rstrip())
    print(min([int(x) for x in n]))