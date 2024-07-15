from zipfile import ZipFile 
import os 

def get_all_file_paths(directory): 
 
	file_paths = [] 

	for root, directories, files in os.walk(directory): 
		for filename in files:  
			filepath = os.path.join(root, filename) 
			file_paths.append(filepath) 

	# returning all file paths 
	return file_paths		 

def zip():  
	directory = input("enter directory name to zip: ")

	file_paths = get_all_file_paths(directory) 

	print('Following files will be zipped:') 
	for file_name in file_paths: 
		print(file_name) 

	# writing files to a zipfile 
	with ZipFile('my_python_files.zip','w') as zip: 
		# writing each file one by one 
		for file in file_paths: 
			zip.write(file) 

	print('All files zipped successfully!')		 

def main():
	a=input("Do you want to zip a file y/n: ")
	if a=='y':
		zip()
		
	b=input("Do you want to unzip a file y/n: ")	
	if b=='y':
		unzip()
	else:
		return 	
		

def unzip(): 
    file_name = input("Enter file name to unzip: ")
  
    with ZipFile(file_name, 'r') as zip: 
        zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!') 

if __name__ == "__main__": 
    main() 

