# DMOJ problem wc17c3j3, Uncrackable

pw = input()

# ll: lowercase letters
# ul: uppercase letters
# d: digit

# it must contain 
# at least (three) lowercase letters, 
# at least (two) uppercase letters, 
# and at least (one) digit.

# Output a single string, 
# either Valid if the password is valid, 
# or Invalid otherwise.

ll = 0
ul = 0
d = 0

if len(pw) >= 8 and len(pw) <= 12:
    
    for char in pw:
      if char >= 'a' and char <= 'z':
        ll = ll + 1
      elif char >= 'A' and char <= 'Z':
        ul = ul + 1
      elif char >= '0' and char <= '9':
        d = d + 1

    #print('ll: ', ll)
    #print('ul: ', ul)
    #print('d: ', d)

    if ll >= 3 and ul >= 2 and d >= 1:
      print('Valid')
    else:
      print('Invalid')
else:
  print('Invalid')