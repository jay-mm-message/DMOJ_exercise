# DMOJ problem ccc20j2, Epidemiology

p = int(input())
n = int(input())
r = int(input()) # disease

if p <= 10 ** 7 and n <= p and r <= 10:
    day = 0
    infect_people = n
    while infect_people <= p:
        day = day + 1
        n = n * r
        infect_people = infect_people + n
        # print(f'infect: {infect_people}, day: {day}, p: {p}')
    print(day)