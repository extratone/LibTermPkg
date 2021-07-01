import sys


if len(sys.argv) > 1:
	if sys.argv[1] == '--help':
		print('\n'.join([
			'To see version info, use --version',
			'Usage: pager FILENAME',
			'When using the pager, after each line appears, you can:',
			'  * Press enter to show the next line',
			'  * Enter a number followed by enter to go forward the specified amount of lines',
			'  * Press "q" followed by enter to exit',
		]))
		sys.exit()
	elif sys.argv[1] == '--version':
		print('\n'.join([
			'Pager for LibTerm version 1.0',
			'Made by Dull Bananas',
			'Website: https://dull.pythonanywhere.com',
		]))
		sys.exit()
	else:
		with open(sys.argv[1], 'r') as f:
			contents = f.read()
else:
	sys.exit()


lines = contents.split('\n')
line_iter = iter(lines)


for line in line_iter:
	option = input(line)
	if option == '':
		continue
	elif option == 'q':
		break
	else:
		for _ in range(int(option)-1):
			next(line_iter)