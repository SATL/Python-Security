def activity01(num):
	#Determinate if an input is Even or Odd
	return 'Even' if num%2==0 else 'Odd'

def activity02(iv_one, iv_two):
	#DReturn the sum
	return iv_two+iv_two

def activity03(num_list):
	#Count how many are even
	count =0
	for x in num_list:
		if activity01(x)=='Odd':
			count+=1 
	return count

def activity04(in_string):
	#String backwars
	return in_string[::-1];



print activity04('alo')