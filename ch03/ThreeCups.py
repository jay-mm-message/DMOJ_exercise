# This is DMOJ problem coci06c5p1.

# A Swap the left and middle cups
# B Swap the middle and right cups
# C Swap the left and right cups

# l: left, m: middle, r: right
# ball_loc: location of the ball

ball_loc = 'l'

moves = input()
for swap_type in moves:
  if swap_type == 'A':
    if ball_loc == 'l':
      ball_loc = 'm'
    elif ball_loc == 'm':
      ball_loc = 'l'
  elif swap_type == 'B':
    if ball_loc == 'm':
      ball_loc = 'r'
    elif ball_loc == 'r':
      ball_loc = 'm'
  elif swap_type == 'C':
    if ball_loc == 'l':
      ball_loc = 'r'
    elif ball_loc == 'r':
      ball_loc = 'l'

if ball_loc == 'l':
   print(1)
elif ball_loc == 'm':
   print(2)
elif ball_loc == 'r':
   print(3)