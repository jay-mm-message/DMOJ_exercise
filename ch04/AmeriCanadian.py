# DMOJ problem ccc02j2, AmeriCanadian

# Americans write neighbor and color while Canadians write neighbour and colour. 
# The user should type a word (not to exceed 64 letters) and 
# if the word appears to use American spelling
# the program should echo the Canadian spelling for the same word. 
# When the user types quit! the program should terminate.


# If the word has more than four letters and has a suffix consisting of a consonant 
# followed by or, you may assume it is an American spelling, 
# and that the equivalent Canadian spelling replaces the or by our. 
# Note: you should treat the letter y as a vowel.

def suffix_is_vowel(word):
    return word[-3] not in 'aeiouy'
def is_americans_spell(word):
    return word[-2:] == 'or'

while True:
    s = input()
    if s == 'quit!':
        break

    c = ''
    # if len(s) > 4 and s[-2:] == 'or' and s[-3] not in 'aeiouy':
    if len(s) > 4 and is_americans_spell(s) and suffix_is_vowel(s):
        c = s[:-2] + 'our'
    else:
        c = s[:]
    print(c)