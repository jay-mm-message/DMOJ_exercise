# This is DMOJ problem coci16c1p1

monthly_mb = int(input())
n = int(input())

available = monthly_mb
for i in range(n):
  use_cost = int(input())
  available = available - use_cost + monthly_mb
print(available)