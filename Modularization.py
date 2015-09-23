import operator

lastString = ''

def removeLetterFromString():
	print "Remove Letter"
	text =raw_input("Enter string: ")
	letter =raw_input("Enter letter: ")[0]
	print text.replace(letter, "")

	return

def numCompare():
	print "Num Compare"
	num1 = int(raw_input("Input first number: "))
	num2 = int(raw_input("Input second number: "))
	if num1>num2:
		print "%i is higher than %i" %(num1, num2)
	elif num2>num1:
		print "%i is higher than %i"%(num2, num1)
	else:
		print "numbers are equal"
	return

def printString():
	print "Show last String"
	global lastString
	print lastString

def calculator():
	sign_dict = { '+' : operator.add, '-': operator.sub, '*':operator.mul, '/':operator.div}
	print "Calculator"
	num1 = int(raw_input("Input first number: "))
	sign =raw_input("Action: ")
	num2 = int(raw_input("Input second number: "))
	print sign_dict[sign](num1, num2) 
	return

def acceptAndStore():
	print "Accept and Store String"
	global lastString
	lastString = raw_input('Introduce a text: ')
	return

def main():
	options = [acceptAndStore, calculator, printString, numCompare, removeLetterFromString]

	while (True):
		print "\nSELECT OPTION:"
		print "1.-Accept and Store"
		print "2.-Calculator"
		print "3.-Print Stored String"
		print "4.-Number Comparation"
		print "5.-Letter remover"

		options[int(raw_input('Selection: '))-1]()
	return


main()
