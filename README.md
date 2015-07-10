# mygit
Basic git in python

Basic git program with three functions: save, checkout, latest.
The functions are called by passing their names as arguments when executing the python file mygit.py.
The function checkout takes an extra argument, the number of the version to be restored, which is passed when executing mygit.py.

The function "save" saves all the files in the current directory into a numbered directory located in the directory .myvcs.
The function "checkout(number)" deletes all the files in the current directory and copies all the files in the backup directory .myvcs/number into the current directory.
The function latest deletes all the files in the current directory and copies all the files in the latest backup directory.

