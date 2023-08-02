# DMOJ problem dmopc16c1p0, C.C. and Cheese-kun

width = int(input())
extra_cheesines = int(input())

mode_satisfied = ""
# C.C. will be absolutely satisfied if 
# the pizza she gets has a width of 3 units and an extra-cheesiness of at least 95 % .
if (width == 3) \
  and (extra_cheesines >= 95):
    mode_satisfied = 'absolutely'
# C.C. will be fairly satisfied if 
# the pizza she gets has a width of 1 unit and an extra-cheesiness of at most 50 % .
elif (width == 1) \
  and (extra_cheesines <= 50):
    mode_satisfied = 'fairly'
else:
    mode_satisfied = 'very'

print("C.C. is " + mode_satisfied + " satisfied with her pizza.")