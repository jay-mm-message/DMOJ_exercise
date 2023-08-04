# This is DMOJ problem ccc00s1.

n = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

# Unknown to her, the machines are entirely predictable. Each play costs one quarter. 
# The first machine pays 30 quarters every 35 th time it is played; 
# the second machine pays 60 quarters every 100 th time it is played; 
# the third pays 9 quarters every 10 th time it is played.

x = 0
play = 'm1'
while n > 0:
    n = n - 1
    x = x + 1
    if play == 'm1':
      m1 = m1 + 1
      if m1 == 35:
         m1 = 0
         n = n + 30
      play = 'm2'
    elif play == 'm2':
      m2 = m2 + 1
      if m2 == 100:
         m2 = 0
         n = n + 60
      play = 'm3'
    elif play == 'm3':
      m3 = m3 + 1
      if m3 == 10:
         m3 = 0
         n = n + 9
      play = 'm1'

print('Martha plays ' + str(x) + ' times before going broke.')