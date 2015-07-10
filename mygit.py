import sys
import os
import shutil

def save():
	if not os.path.exists('.myvcs'):
		os.mkdir('.myvcs')

	new_name = str(len(os.listdir('.myvcs')))
	new_name = '.myvcs/' + new_name
	os.mkdir(new_name)

	files_to_copy = os.listdir('.')
	if '.myvcs'  in files_to_copy:
		files_to_copy.remove('.myvcs')

	for file in files_to_copy:
		shutil.copy(file, new_name + '/')

def checkout(version):  
# copy all files in number in current directory after deleting everything in the directory
	files_to_remove = os.listdir('.')
	if '.myvcs' in files_to_remove:
		files_to_remove.remove('.myvcs')

	for file in files_to_remove:
		os.remove(file)
	
	for file in os.listdir('.myvcs/' + version):
		shutil.copy('.myvcs/' + version + '/' + file, ".")

def latest():
	if len(os.listdir('.myvcs')) == 0:
		print "There is saved version yet"
		return
	save_list = [int(item) for item in os.listdir('.myvcs')]
	checkout(str(max(save_list)))




def main():
	if sys.argv[1] == 'save':
		save()
	elif sys.argv[1] == 'checkout':
		if len(sys.argv) < 3:
			print "You need to specify which snapshot to restore"
			return
		if not os.path.exists('.myvcs/' + sys.argv[2]):
			print "There is no save with that name"
			return
		checkout(sys.argv[2])
	elif sys.argv[1] == 'latest':
		latest()
	else:
		print "I don't know how to do that!"

main()
