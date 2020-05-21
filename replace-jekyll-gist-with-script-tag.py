import sys
import fileinput
import os

def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as f:
        for line in f:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')

def replace_gist_on_file(fullPath, username):
	print("Checking " + fullPath)

	with open(fullPath, 'r') as file :
	  lines = file.readlines()

	replacements = []

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

def replace_gist_on_folder(folder, username):
	for file in os.listdir(folder):
	    if file.endswith(".md"):
	    	replace_gist_on_file(folder + "/" + file, username)

numberOfParameters = len(sys.argv)
if numberOfParameters < 2:
	print("ERROR: Filename or folder not provided")
	print("Usage: python replace-jekyll-gist-with-script-tag.py [file/folder] [github username]")
	exit()

if numberOfParameters < 3:
	print("ERROR: Github username not provided")
	print("Usage: python replace-jekyll-gist-with-script-tag.py [file/folder] [github username]")
	exit()

path = sys.argv[1]
username = sys.argv[2]
currentDirectory = os.getcwd()
fullPath = currentDirectory + "/" + path
isFile = os.path.isfile(path)

if isFile:
	replace_gist_on_file(fullPath, username)	
else:
	replace_gist_on_folder(fullPath, username)