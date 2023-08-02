# DMOJ problem ccc15j2, Happy or Sad

words = input()
happy_count = words.count(':-)')
sad_count = words.count(':-(')

if happy_count > sad_count:
    print('happy')
elif happy_count < sad_count:
    print('sad')
elif (happy_count == 0) \
    and (sad_count == 0):
    print('none')
else:
    print('unsure')