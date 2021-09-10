#!/usr/bin/env python3
#PASSTRIQUE

comment = input("Type your comment below\n> ")#INPUT: user's sentence, to process
vowels='aeiouy'#list of vowels

i = 0
comment_final = ''
while(i < len(comment)):
	a = 0
	while (a < len(vowels)):
		#print(comment[i], " compared to ", vowels[a])"""Uncomment line for verbose mod"""
		if comment[i] == vowels[a]:
			comment_final = comment_final + "-" #Replacement line
			break
		else:
			if (a == 5):#At step 5, the char isn't vowel. So we keep the original value
				comment_final = comment_final + comment[i]#Add user's char
			else:
				pass#Do nothing
		a = a + 1
	i = i + 1

print("\nResult: ",comment_final)
