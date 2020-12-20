import os
from os import walk

# change directory to suit your needs
<<<<<<< HEAD
<<<<<<< HEAD
path = "/home/path/" 
=======
path = "/media/imageDB/LPR/WCE_ANPR_DATA/renamethis/" 
>>>>>>> 5592f8e... Initial commit
=======
path = "/home/path/" 
>>>>>>> 34fe968... Update some configs and README

def write(path):
	files = open("textfile.txt","w")

	source_dir = path
	os.chdir(source_dir)
	list_dir = os.listdir()
	list_dir = [files for files in list_dir]
	list_dir = sorted(list_dir)

	for filename in list_dir:
		file_name, file_extension = os.path.splitext(filename)
		gt = file_name.split('_')[-1]
		file_name, file_extension = os.path.splitext(filename)
		files.write(source_dir+filename + "\t" + gt + "\n")

	files.close()

if __name__ == '__main__':
	write(path)