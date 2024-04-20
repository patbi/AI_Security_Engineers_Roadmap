
with open('venv.jpg', 'rb') as rf:
	with open('venv_copy.jpg', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)
		# for line in rf:
		# 	wf.write(line)



# with open('file-demo.txt', 'r') as rf:
# 	with open('file-demo-copy', 'w') as wf:
# 		for line in rf:
# 			wf.write(line)



# with open('file-demo-write.txt', 'w') as f:
# 	# pass
# 	f.write('11 - This is C++ File')
# 	f.seek(0)
# 	f.write('11 - This is C File')



# with open('file-demo-write.txt', 'r') as f:
# 	f.write('Test')


# with open('file-demo.txt', 'r') as f:
# 	size_to_read = 10

# 	f_contents = f.read(size_to_read)
# 	print(f_contents, end='')

# 	f.seek(0)

# 	f_contents = f.read(size_to_read)
# 	print(f_contents)

	# print(f.tell())




# with open('file-demo.txt', 'r') as f:
# 	# size_to_read = 100

# 	size_to_read = 10
# 	f_contents = f.read(size_to_read)

# 	while len(f_contents) > 0:
# 		# print(f_contents, end='')
# 		print(f_contents, end='*')
# 		f_contents = f.read(size_to_read)


# with open('file-demo.txt', 'r') as f:

# 	f_contents = f.read(100)
# 	print(f_contents, end='')

# 	f_contents = f.read(100)
# 	print(f_contents, end='')




# with open('file-demo.txt', 'r') as f:

# 	for line in f:
# 		print(line, end='')


# with open('file-demo.txt', 'r') as f:
# 	f_contents = f.readline()
	# f_contents = f.readlines()
	# print(f_contents) 
	# print(f_contents, end='') 

	# f_contents = f.readline()
	# print(f_contents)
	# print(f_contents, end='')


# with open('file-demo.txt', 'r') as f:
# 	f_contents = f.read()
# 	print(f_contents) 


# with open('file-demo.txt', 'r') as f:
# 	pass
# print(f.read())


# f = open('file-demo.txt', 'r')

# print(f.mode)

# f.close()

