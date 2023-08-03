# This is DMOJ problem coci16c1p1

megabytes_mb = int(input())
n = int(input())

available = megabytes_mb
for i in range(n):
  use_cost = int(input())
  available = available - use_cost + megabytes_mb
print(available)