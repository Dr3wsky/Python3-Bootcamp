# one.py

def func(): 
	print("func() in one.py")

print("Top level in one.py")

if __name__ == '__main__':
	print("one.py is running directly")
else:
	print("one.py has been imported")
