# DMOJ problem ccc07j1, Who is in the Middle

# b1, b2, b3 for bears numbers
b1 = int(input())
b2 = int(input())
b3 = int(input())

# m: Mama_bear's 
m = 0
if b1 > b2 and b2 > b3:
  m = b2
elif b3 > b2 and b2 > b1:
  m = b2
elif b2 > b1 and b1 > b3:
  m = b1
elif b3 > b1 and b1 > b2:
  m = b1
elif b1 > b3 and b3 > b2:
  m = b3
elif b2 > b3 and b3 > b1:
  m = b3
print(m)