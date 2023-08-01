# DMOJ problem wc15c2j1, A New Hope

str_head = "A long time ago in a galaxy"
str_tail = "away..."

num = int(input())

if num == 1:
    words = str_head + " far " + str_tail
else:
    repeat_words = " far," * (num - 1)
    words = str_head + repeat_words + " far " + str_tail

print(words)