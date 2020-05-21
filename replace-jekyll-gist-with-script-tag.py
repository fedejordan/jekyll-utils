import sys
import fileinput
import os

def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as f:
        for line in f:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')

# Read from file
numberOfParameters = len(sys.argv)
if numberOfParameters < 2:
	print("ERROR: Filename not provided")
	print("Usage: python replace-jekyll-gist-with-script-tag.py [file] [github username]")
	exit()

if numberOfParameters < 3:
	print("ERROR: Github username not provided")
	print("Usage: python replace-jekyll-gist-with-script-tag.py [file] [github username]")
	exit()

filename = sys.argv[1]
username = sys.argv[2]
# print("Filename: " + filename)
currentDirectory = os.getcwd()
# print("Current directory: " + os.getcwd())
fullPath = currentDirectory + "/" + filename
# print("Full path for file: " + fullPath)

with open(fullPath, 'r') as file :
  lines = file.readlines()

replacements = []

# Replace the target string
for line in lines:
	if "% gist" in line:
		components = line.split()
		gistId = components[2]
		print("Found gist: " + gistId)
		tagString = "<script src=\"https://gist.github.com/" + username + "/" + gistId + ".js\"></script>"
		replacements.append([line, tagString])

for replacement in replacements:
	replace_in_file(fullPath, replacement[0], replacement[1])

replacementsCount = len(replacements)
if replacementsCount == 0:
	print("No gists were found")
else:
	print("Replaced " + str(replacementsCount) + " gists")
	# else:
	# 	print("Line does not contain gist")

# Write the file out again
# with open('file.txt', 'w') as file:
#   file.write(filedata)

# print(filedata)

# try:
# 	with fileinput.FileInput(fullPath, inplace=True, backup='.bak') as file:
# 		print("Actual filename: " + fullPath)
# 		print("File: " + file)
# 		for line in file:
# 			print("Looking for gist on " + line)
# 			if "{% gist" in line:
# 				print("Found gist: " + line)
# except:
# 	print("[ERROR]: Cannot read file")
# print(line.replace(text_to_search, replacement_text), end='')