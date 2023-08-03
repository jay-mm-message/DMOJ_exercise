# DMOJ problem coci12c5p1, Ljestvica

A_tone = 'ADE'
C_tone = 'CFG'   

tone = input()

a_count = 0
c_count = 0

for i in range(len(tone)):
    if i == 0 or tone[i] == '|':
      if tone[i+1] in A_tone:
         a_count = a_count + 1
      if tone[i+1] in C_tone:
         c_count = c_count + 1

if a_count == c_count:
   if tone[-1] == 'A':
      print('A-mol')
    

if a_count > c_count:
  print('A-mol')
else:
  print('C-dur')