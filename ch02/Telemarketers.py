# This is DMOJ problem ccc18j1.

first = int(input())
second = int(input())
three = int(input())
four = int(input())

if (first == 8 or first == 9) \
    and (second == three) \
    and (four == 8 or four == 9):
      print('ignore')
else:
    print('answer')