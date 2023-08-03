# DMOJ problem coci13c3p1, Rijeci

# 1. n = 0, a
# 2. n = 1, b
# 3. n = 2, ba
# 4. n = 3, bab
# 5. n = 4, babba
# 6. n = 5, babbabab

# count a: b:
# 1. 1 0
# 2. 0 1
# 3. 1 1
# 4. 1 2
# 5. 2 3
# 6. 3 5

n = int(input())

b = 0
a = 0
if n == 0:
    b = 0
elif n == 1:
    b = 1
else:
    x = 0
    y = 1
    for i in range(2, n+1):
        tmp = y
        y = y + x
        x = tmp
    b = y

if n == 0:
    a = 1
elif n == 1:
    a = 0
else:
    x = 0
    y = 1
    for i in range(3, n+1):
        tmp = y
        y = y + x
        x = tmp
    a = y
    
print(a, b)

# pre_letter = 'A'
# letter = ''
# if n > 0 and n <=46:

#   for i in range(n):
#       if i == 0:
#           letter = 'B'
#       else:
#           tmp_letter = letter
#           letter = letter + pre_letter
#           pre_letter = tmp_letter

# # print(letter)
# a_count = letter.count('A')
# b_count = letter.count('B')

# print(a_count, b_count)