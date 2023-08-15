# This is DMOJ problem ccc00s1.

quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

# 35th paid 30
# 100th paid 60
# 10th paid 9
machine = 0
slot_time = 0
while quarters > 0:
    if (machine % 3) == 0:
        first = first + 1
        if (first % 35) == 0:
            quarters = quarters + 30
        # if first == 35:
        #     first = 0
        #     quarters = quarters + 30

    elif (machine % 3) == 1:
        second = second + 1
        if (second % 100) == 0:
            quarters = quarters + 60
        # if second == 100:
        #     second = 0
        #     quarters = quarters + 60

    elif (machine % 3) == 2:
        third = third + 1
        if (third % 10) == 0:
            quarters = quarters + 9
        # if third == 10:
        #     third = 0
        #     quarters = quarters + 9

    slot_time = slot_time + 1
    machine = machine + 1 
    quarters = quarters - 1

# print('Martha plays ' + str(slot_time) + ' times before going broke.')
print(f'Martha plays {slot_time} times before going broke.')