
try:
	# f = open('testfiles.txt')
	# f = open('currupt_file.txt')
	# if f.name == 'currupt_file':
		raise Exception
	# var = bad_var
# except Exception:
# except FileNotFoundError:
except FileNotFoundError as e:
	# print("Sorry. This file doesn't exist")
	print(e)
# except Exception:
except Exception as e:
	# print('Sorry. Something went wrong')
	# print(e)
	print('Error!')
else:
	print(f.read())
	f.close()
finally:
	print("Executing Finally...")