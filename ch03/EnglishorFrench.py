# DMOJ problem ccc11s1, English or French

lines_of_text = int(input())
sS_count = 0
tT_count = 0
for n in range(lines_of_text):
  lines = input()
  for i in range(len(lines)):
    if lines[i] == 's' or lines[i] == 'S':
      sS_count = sS_count + 1
    elif lines[i] == 't' or lines[i] == 'T':
      tT_count = tT_count + 1

if tT_count > sS_count:
  print('English')
elif tT_count <= sS_count:
  print('French')