# DMOJ problem coci18c3p1, Magnus

words = input()
# words = 'PROHODNIHODNIK'
# words = 'HHHHOOOONNNNIIII'
# words = 'MAGNUS'
subwords_count = 0
subwords = ''
for i in range(len(words)):
    if words[i] == 'H' \
      and 'H' not in subwords:
        
        subwords = subwords + 'H'
        #print(subwords)
    elif words[i] == 'O' \
      and 'H' in subwords \
      and 'O' not in subwords:
        
        subwords = subwords + 'O'
        #print(subwords)
    elif words[i] == 'N' \
      and 'H' in subwords \
      and 'O' in subwords \
      and 'N' not in subwords:
        
        subwords = subwords + 'N'
        #print(subwords)
    elif words[i] == 'I' \
      and 'H' in subwords \
      and 'O' in subwords \
      and 'N' in subwords \
      and 'I' not in subwords:
        
        subwords = subwords + 'I' 
        #print(subwords)
    
    if 'HONI' in subwords:
        #print('subwords compare HONI')
        subwords_count = subwords_count + 1
        subwords = ''
print(subwords_count)