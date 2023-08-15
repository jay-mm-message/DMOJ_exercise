

press_btn = 0
press_times = 0

s = 'ABCDE'

while press_btn != 4:
    press_btn = int(input())
    press_times = int(input())
    
    while press_times > 0:
        press_times = press_times - 1
        if press_btn == 1:
            s = s[1:] + s[0]
        elif press_btn == 2:
            s = s[-1] + s[:-1]
        elif press_btn == 3:
            s = s[1] + s[0] + s[2:]

output = ''
song_playlist = s
for c in song_playlist:
    output = output + c + ' '

print(output)