# With testing script in Sublime text
def do_stuff(num=0):
	try:
		if num == 0 or num:
			return int(num) + 5
		else:
			return "please enter number!"
	except ValueError as err:
		return err


print(do_stuff())
