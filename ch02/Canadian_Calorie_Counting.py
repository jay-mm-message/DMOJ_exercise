# CCC '06 J1 - Canadian Calorie Counting

burger_choices = int(input())
side_choices = int(input())
drink_choices = int(input())
dessert_choices = int(input())

total_calories = 0
if burger_choices == 1:
    total_calories = total_calories + 461
elif burger_choices == 2:
    total_calories = total_calories + 431
elif burger_choices == 3:
    total_calories = total_calories + 420
else:
    total_calories = total_calories + 0


if drink_choices == 1:
    total_calories = total_calories + 130
elif drink_choices == 2:
    total_calories = total_calories + 160
elif drink_choices == 3:
    total_calories = total_calories + 118
else:
    total_calories = total_calories + 0

if side_choices == 1:
    total_calories = total_calories + 100
elif side_choices == 2:
    total_calories = total_calories + 57
elif side_choices == 3:
    total_calories = total_calories + 70
else:
    total_calories = total_calories + 0

if dessert_choices == 1:
    total_calories = total_calories + 167
elif dessert_choices == 2:
    total_calories = total_calories + 266
elif dessert_choices == 3:
    total_calories = total_calories + 75
else:
    total_calories = total_calories + 0

print('Your total Calorie count is ' + str(total_calories) + '.')