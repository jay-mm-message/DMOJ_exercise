# DMOJ problem ccc11s2, Multiple Choice

number = int(input())

student_response = ''
correct_answers = ''

count = 0
for n in range(number * 2):
  char = input()
  if count < number:
    student_response = student_response + char
  elif count >= number:
    correct_answers = correct_answers + char
  count = count + 1

corrent_count = 0
for i in range(len(correct_answers)):
  if student_response[i] == correct_answers[i]:
    corrent_count = corrent_count + 1
print(corrent_count)
