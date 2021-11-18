# Imports

import os
import subprocess
import re

# Current Directory getter $ Can also manually set the directory path as the folder_path directory

folder_path = os.getcwd()

# Sub Directory listing

folders = os.listdir(folder_path)

# Amount of Sub Directories to parse and global list initilization

folders_len = len(folders)
filename_list = []
file_path_list = []

# For loop to find all filenames in sub directories

for i in range(folders_len):
	file_path = folder_path + "//" +  folders[i]
	filenames = os.listdir(file_path)
	filename_list.append(filenames)
	file_path_list.append(file_path)	

# Amount of filenames found in all Sub Directories

filename_list_len = len(filename_list)
count = 0

# For loop for Parsing all found files in each Sub Directory

for j in range(filename_list_len):
	filename_sub_list_len = len(filename_list[j])
	filename_sub_list = filename_list[j]
	
	# Nested forloop for creating file path to each parsed file in Sub Directory

	for k in range(filename_sub_list_len):
		
		# Creating input files {taget Flac[or whatever file type needed]}

		file_in_folder_path = file_path_list[count] + "//" + filename_sub_list[k]
		input_filename = file_in_folder_path	
		file_in_folder_len = len(file_in_folder_path)
		print(file_in_folder_path, " :Input")
		print('\n')
		
		# Regular Expression search if statment for finding files that end in .flac [or whatever file type needed]
		
		if re.search('.flac',file_in_folder_path):

			# Creating desired output filename with file type needed

			output_filename = file_in_folder_path[:file_in_folder_len - 4] + "mp3"
			print(output_filename, " : Output")
			print('\n')

			# Sub Process to run ffmpeg command {in this case changing .flac --> .mp3} [subproccess.call can include and commands needed for changing desired file type]

			subprocess.call(['ffmpeg', '-i', input_filename, '-ab', '320k', '-map_metadata', '0', '-id3v2_version', '3', output_filename ])
			
			# Confirmation print statment leting user know convertion was made sucessfully

			print("flac --> mp3 filetype: converted")
			print("\n")
		else:
			# Else print statment created for files that dont match desired file type

			print("Not a flac filetype")
			print("\n")
			
	count += 1
