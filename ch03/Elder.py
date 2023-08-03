# DMOJ problem coci18c4p1, Elder

wand_wizard = input()
duels_time = int(input())
duels_changes_list = wand_wizard

for i in range(duels_time):
    duels = input()
    if wand_wizard in duels[-1]:
        wand_wizard = duels[0]
        if wand_wizard not in duels_changes_list:
            duels_changes_list = duels_changes_list + wand_wizard


print(wand_wizard)
print(len(duels_changes_list))


# Input

# The first line contains an uppercase letter of the English alphabet,
#  the label of the wizard that the wand obeyed at the beginning.

# The second line contains an integer number N ( 1 ≤ N ≤ 100 ) , 
# the number of duels from the text of the task.

# In the next N rows there are two different uppercase letters of 
# the English alphabet Z 1 and Z 2 separated by a space, whereas 
# the wizard with the label Z 1 defeated the wizard with the 
# label Z 2 in the i th duel. Output

# In the first line print an uppercase letter of the English alphabet,
#  answer to the first question from the task description.

# In the second line print an integer number, answer to the 
# second question from the task description. Scoring

# Correct answer to the first question is worth 2 points 
# and the correct answer to the second question is worth 3 points. 
# If you do not know how to solve some part of the task,
# then print any value in the corresponding line.