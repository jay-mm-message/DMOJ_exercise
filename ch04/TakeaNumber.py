# DMOJ problem ecoo13r1p1, Take a Number

n = int(input())
serv = 0
students = 0
while True:
    ACT = input()
    if ACT == 'EOF':
        break
    elif ACT == 'TAKE':
        n = n + 1
        if n > 999:
            n = 1
        students = students + 1
        serv = serv + 1
    elif ACT == 'SERVE':
        serv = serv - 1
    elif ACT == 'CLOSE':
        print(f'{students} {serv} {n}') 
        students = 0
        serv = 0
