from os import walk

<<<<<<< HEAD
dirs = walk('/home/path')
=======
dirs = walk('/home/zeke/Downloads')
>>>>>>> 5592f8e... Initial commit
for path_from_top, subdirs, files in dirs:
	for f in files:
		if f.endswith('jpg'):
			print(str(path_from_top) + '/' + str(f))
			print("1")
		elif f.endswith('xml'):
			print(str(path_from_top) + '/' + str(f))
			print("2")