vaild = False

while not vaild:
    s = input("please entry password: ")
    vaild = len(s) == 5 and s[:2] == 'xy'

if vaild:
    print("password correct")