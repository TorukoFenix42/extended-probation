from os import walk

<<<<<<< HEAD
<<<<<<< HEAD
dirs = walk('/home/path')
=======
dirs = walk('/home/zeke/Downloads')
>>>>>>> 5592f8e... Initial commit
=======
dirs = walk('/home/path')
>>>>>>> 34fe968... Update some configs and README
for path_from_top, subdirs, files in dirs:
	for f in files:
		if f.endswith('jpg'):
			print(str(path_from_top) + '/' + str(f))
			print("1")
		elif f.endswith('xml'):
			print(str(path_from_top) + '/' + str(f))
			print("2")