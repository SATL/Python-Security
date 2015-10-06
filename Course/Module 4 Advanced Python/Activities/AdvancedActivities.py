import os

def isLinux():
	return os.name != 'nt'

if isLinux():
	import tkMessageBox as msgBox
else:
	import ctypes
	msgBox = ctypes.windll.user32.MessageBoxA

from time import sleep #need for multithreading
import threading, re

'''2.1 Ctypes: Write a function which takes two arguments, title and body
and creates a MessageBox with those arguments'''
def python_message_box(title = '' , body = ''):
	if isLinux():
		msgBox.showinfo('my app','my message')
	else:
		msgBox(None, body, title, 0)
	return


'''2.2 Ctypes: Write a function which takes two arguments, filename and
data and creates a file with that data written to it'''
def python_create_file(filename = '' , data = ''):
	f = open(filename, 'w+')
	f.write(data)
	f.close()
	return
    

'''2.3 Ctypes: Write a function which takes one argument, a filename,
and prints the data from that file'''
def python_read_file(filename = ''):
    return

'''2.4 Regex: Write a regular expression to search a data block for a 
string contained in <> (html-style) brackets. IE: <span color=black>'''
def regex_html(data):
	match = re.compile('<.*>')
	results = re.search(match, data)
	print data
	print 'Results:'
	print results.group()
	return
    

'''2.5 Regex: Write a regular expression to search a data block for 
phone numbers in the form of (xxx) xxx-xxxx'''
def regex_phone(data):
	phone_match = "\(\d{3}\) \d{3}-\d{4}"
	phone_results = re.findall(phone_match, data)
	print data
	print "Results:"
	print phone_results
	return

'''2.6 Regex: Write a regular expression to find every instance of the 
phrase "Nobody expects" and replace it with "The Spanish Inquisition"'''
def monty_python(data):
	print data
	data =data.replace("Nobody expects", "The Spanish Inquisition")
	print data
	return


'''2.7 Multi-threading: Write a function which runs this entire program,
each function getting its own thread.'''
def multiple_threads():

	functions = [python_message_box,
				python_create_file,
				python_read_file,
				regex_html,
				regex_phone,
				monty_python]

	args_list = [  ("Hello","World!"),
                ("Test.txt","IT WORKED!"),
                ("Test.txt",),
                ("ajfskdfajlsdhja;lkj<HTMLDATA>dsafsa;dfa",),
                ("kdsj;aifhjiodsh(555) 555-5555dsl'kaf;kadsjf",),
                ("Nobody expects",)]
	threads = [];

	for i in range(len(functions)):
		threads.append(threading.Thread(None, functions[i], None, args_list[i]))

	for i in range(len(threads)):
		threads[i].start()
		sleep(1)

	return

def main():
    multiple_threads()
    
main()






