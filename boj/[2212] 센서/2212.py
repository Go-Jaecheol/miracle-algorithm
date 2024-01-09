import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensor = [int(x) for x in sys.stdin.readline().split()]
sensor = sorted(set(sensor))
gap = []

for i in range(1, len(sensor)):
    gap.append(sensor[i] - sensor[i - 1])
gap.sort()
print(sum(gap[:len(sensor) - K]))