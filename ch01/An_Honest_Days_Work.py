# DMOJ problem wc18c3j1, An Honest Day’s Work

P = int(input())
B = int(input())
D = int(input())

total = (P // B * D) + (P % B)

print(total )