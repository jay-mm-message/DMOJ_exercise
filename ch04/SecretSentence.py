# This is DMOJ problem coci08c3p2.

# k: Kemija 
sentence_org = input()
sentence_chg = ''
	
i = 0
while i < len(sentence_org):
# encode
	# if sentence_org[i] in 'aeiou':
	#     sentence_chg = sentence_chg + sentence_org[i] + 'p' + sentence_org[i]
	# else:
	#     sentence_chg = sentence_chg + sentence_org[i]
	# i = i + 1
# decode
	if sentence_org[i] in 'aeiou':
		i = i + 2 # shift encode code
		
	sentence_chg = sentence_chg + sentence_org[i]
	i = i + 1
# display result
print(sentence_chg)