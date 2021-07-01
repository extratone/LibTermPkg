import sys

a = sys.argv + [None] * 5
c = len(sys.argv)




info = {
	'libterm': {
		'help': ['The help command displays a list of all built-in commands. It does not show commands added by installed packages.'],
		'package': ['The package command manages packages for Libterm. Type the command to see its options.']
	},
	'network': {
		'ifconfig': ['This is used for configuring TCP/IP network interface parameters.'],
		'ping': ['Ping is used to ping a server. For example, this is how you ping google.com:',
		         'ping google.com',
		         'You can use the -c argument to specify the amount of pings to do. For example, this is how you ping google.com 20 times:',
		         'ping google.com -c 20'],
		'telnet': ['This is a telnet program in LibTerm that you start by simply typing "telnet".',
		           'Once you are in the program, type "help" to see a list of commands you can use in it.',
		           'To exit the program, type "quit" or tap the "Stop" button above the keyboard.'],
		'host': ['This command is a DNS lookup tool.',
		         'When you specify a domain name, it gives its IP address. For example, this is how you find google.com\'s IP address:',
		         'host google.com',
		         'You can also specify an IP address, which will tell you its domain name:',
		         'host 172.217.14.110'],
		'nslookup': ['This is a program where you can enter a domain name and it shows the IP address.',
		             'To exit the program, type "exit" or tap the "Stop" button above the keyboard.']
	},
	'filesystem': {
		'chmod': ['This changes access permissions for a file. The syntax is:',
		          'chmod <confusing confucious thing> <filename>',
		          'The "confusing confucious thing" is a bit complicated. It specifies the permission mode you want to apply to the file.',
		          'This article on the Internet explains the confucious thing: http://www.washington.edu/computing/unix/permissions.html'],
		'gzip': ['When you specify a filename, this will compress the file and create a gzip file with the same name.',
		         'For example, to compress "farts.txt", type "gzip farts.txt" and the compressed file will be saved as "farts.txt.gz".'],
		'mv': ['This moves/renames a file. For example, this is how you rename poop.txt to no.txt:',
		       'mv poop.txt no.txt'],
		'cd': ['This changes the current directory. To go up one directory, use "cd ..".'],
		'tee': ['This command writes the output of another command to a file. For example, to put the output of "ls ../" on "ls.txt":',
		        'ls ../ | tee ls.txt',
		        'This overwrites the file. You can use -m to make it append to the end of the file instead.',
		        'You can output to multiple file at the same time:',
		        'ls ../ | tee -a a.txt b.txt c.txt'],
		'touch': ['This can be used to create new blank files or update the "last modified" time of a file.']
	},
	'misc': {
		'bc': ['This is a calculator program. You simply start the program and type math expressions, and it will output the result.',
		       'To exit the program, type "quit" or tap the "Stop" button above the keyboard.'],
		'date': ['When you just type "date" without arguments, it shows the current date and time.',
		         'See this thingy for info: https://www.techonthenet.com/linux/commands/date.php'],
		'say': ['WOW THIS COMMAND IS SO COOL BECAUSE IT ACTUALLY TALKS!!!!!',
		        'Type "say hi" to make ur device say hi!!!!!!!!!!!!!!!!!!!!']
	}
}




def header(text):
	return "=====" + text + "====="

def show(head, text, sort=False):
	if sort:
		text.sort()
	print("\033[33m" + "\n".join([ header(head), "\n".join(text), "="*(10+len(head)) ]) + "\033[0m")




usage = [
	'cmdguide list cmd.             Lists all commands',
	'cmdguide list cat.             Lists all categories',
	'cmdguide info <command name>.  Shows info about the specified command',
	'cmdguide cat <category name>.  Lists commands within the specified category', '',
	'Cmdguide is a program that provides info about the commands in LibTerm.',
	'It is not complete yet; many commands are not described in Cmdguide.'
]

if c==1:
	show("Cmdguide Usage", usage)




elif a[1] == "list":
	result = []
	title = ""
	if a[2] == "cmd":
		for cat in info.values():
			for cmdname in cat.keys():
				result.append(cmdname)
		title = "Command List"
	
	elif a[2] == "cat":
		for cat in info.keys():
			result.append(cat)
		title = "Categories"
	
	show(title, result, True)




elif a[1] == "cat":
	try:
		result = []
		for cmdname in info[a[2]].keys():
			result.append(cmdname)
		
		show(a[2], result, True)
	
	except KeyError:
		show("Error", ["The category '" + a[2] + "' does not exist."])




elif a[1] == "info":
	poop = True
	for cat in info.values():
		if a[2] in cat.keys():
			show(a[2], cat[a[2]])
			poop = False
			break
	
	if poop:
		print (":( we don't have a description for that command :( :( :( :) :( :(")




else:
	print(":( invalid command :( :( :( :) :( :(")