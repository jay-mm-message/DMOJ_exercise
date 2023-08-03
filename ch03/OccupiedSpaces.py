# This is DMOJ problem ccc18j2.

park_total = int(input())
yesterday_park = input()
today_park = input()

occupied = 0
for i in range(park_total):
    if yesterday_park[i] == 'C' \
      and today_park[i] == 'C':
        occupied = occupied + 1

print(occupied)