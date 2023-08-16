# DMOJ problem coci08c1p2, Ptice

# Adrian claims that the best sequence is: A , B , C , …
# Bruno is convinced that this is better: B , A , B , C , …
# Goran laughs at them and will use this sequence: C , C , A , A , B , B , … 
Adrian_gets = 'ABC'
Bruno_gets = 'BABC'
Goran_gets = 'CCAABB'

exam_number = int(input())
correct_answers = input()

Adrian_correct = 0
Bruno_correct = 0
Goran_correct = 0
i = 0

if exam_number <= 100 and exam_number >= 1:

    while len(Adrian_gets) < exam_number:
        Adrian_gets = Adrian_gets + Adrian_gets
    while len(Bruno_gets) < exam_number:
        Bruno_gets = Bruno_gets + Bruno_gets
    while len(Goran_gets) < exam_number:
        Goran_gets = Goran_gets + Goran_gets

    while i < exam_number:
        if correct_answers[i] == Adrian_gets[i]:
            Adrian_correct = Adrian_correct + 1
        if correct_answers[i] == Bruno_gets[i]:
            Bruno_correct = Bruno_correct + 1
        if correct_answers[i] == Goran_gets[i]:
            Goran_correct = Goran_correct + 1
                
        i = i + 1

    max = 0
    if max < Adrian_correct:
        max = Adrian_correct
    if max < Bruno_correct:
        max = Bruno_correct
    if max < Goran_correct:
        max = Goran_correct

    print(max)
    if max == Adrian_correct:
        print('Adrian')
    if max == Bruno_correct:
        print('Bruno')
    if max == Goran_correct:
        print('Goran')