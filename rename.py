import os
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

partialpath = parser.get('path', 'batch')

#set for batch number
rng = parser.get('path', 'batch_no')
rng = int(rng)

#path =  os.getcwd()

def rename_jpg_files():
	for j in range(rng):
		source_dir = partialpath + 'batch_' + str(j) + '/'
		os.chdir(source_dir)
		list_dir = os.listdir()
		list_dir = [file for file in list_dir]
		list_dir = sorted(list_dir)
		i = 0
		for filename in list_dir:	
			file_name, file_extension = os.path.splitext(filename)
		
			# for i in range(len(list_dir)):
			if file_extension == ('.jpg'):
				if(file_name[-1:] == '_') or (file_name[-5:] == '_0000'):
					file_no = file_name.split('_')[-2]			
					print('no result', file_name, file_extension)	
					os.rename(file_name + file_extension, str(format(i + 1, '006d')) + '_' + file_no + '_0000' + file_extension)			
			
				else:
					file_no = file_name.split('_')[-2]
					file = file_name.split('_')[-1]		
					print('result', file_name, file_extension)
					os.rename(file_name + file_extension, str(format(i + 1, '006d')) + '_' + file_no + '_' + file + file_extension)
			elif file_extension == ('.xml'):
				continue
		
			i += 1
		
def rename_xml_files():	
	for j in range(rng):
		source_dir = partialpath + 'batch_' + str(j) + '/'
		os.chdir(source_dir)
		list_dir = os.listdir()
		list_dir = [file for file in list_dir]
		list_dir = sorted(list_dir)
		k = 0
		for filename in list_dir:	
			file_name, file_extension = os.path.splitext(filename)
		
			# for i in range(len(list_dir)):
			if file_extension == ('.xml'):
				if(file_name[-1:] == '_') or (file_name[-5:] == '_0000'):
					file_no = file_name.split('_')[-2]			
					print('no result', file_name, file_extension)	
					os.rename(file_name + file_extension, str(format(k + 1, '006d')) + '_' + file_no + '_0000' + file_extension)			
			
				else:
					file_no = file_name.split('_')[-2]
					file = file_name.split('_')[-1]		
					print('result', file_name, file_extension)
					os.rename(file_name + file_extension, str(format(k + 1, '006d')) + '_' + file_no + '_' + file + file_extension)
			elif file_extension == ('.jpg'):
				continue
		
			k += 1
			
#test increment		
def increment():
	i = 0
	for i in range(100000):		
		print(format(i + 1, '006d'))
		i += 1
		
#test rename function
def rename():
	os.rename('oldfile', 'newfile')

if __name__ == '__main__':
	rename_jpg_files()
	rename_xml_files()	
	