# This is DMOJ problem ccc08j2.
# CCC '08 J2 - Do the Shuffle

playlist = 'ABCDE'

loop_mode = True

while loop_mode:
    btn = int(input())
    btn_time = int(input())
    while btn_time > 0:
        if btn == 1:
            playlist = playlist[1:] + playlist[0]
        elif btn == 2:
            playlist = playlist[-1] + playlist[0:4]
        elif btn == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:]
        elif btn == 4:
            loop_mode = False
            s = playlist
            print(f'{s[0]} {s[1]} {s[2]} {s[3]} {s[4]}')

        btn_time = btn_time - 1
# playlist = ['A', 'B', 'C', 'D', 'E']

# loop_mode = True

# while loop_mode:
    
#     btn = int(input())
#     btn_time = int(input())

#     while btn_time > 0:
#         if btn % 4 == 0:
#           s = playlist
#           print(f'{s[0]} {s[1]} {s[2]} {s[3]} {s[4]}')
#           loop_mode = False
#         elif btn % 4 == 1: 
#           first = playlist.pop(0)
#           playlist.append(first)
#         elif btn % 4 == 2:
#           last = playlist.pop(-1)
#           playlist.insert(0, last)
#         elif btn % 4 == 3:
#           first = playlist.pop(0)
#           second = playlist.pop(0)
#           playlist.insert(0, first)
#           playlist.insert(0, second)
#         btn_time = btn_time - 1
