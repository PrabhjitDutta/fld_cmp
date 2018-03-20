# fld_cmp

This is a command-line application built using Python and Click. The user can use the given command fld_cmp to scan to folders and find similar/dissimlar
files or folder (i.e. files or folders compare with their name or format) inside of the directories provided by the user or even sync the two folders. The user is provided with three options
they can either compare the folders for similar files/folders, compare the folder for dissimilar files/folders, or sync the two directories. 

Two modules have been used:
* `click`
* `os`

## Installing the Command

*Navigate to the folder where you have downloaded the files using cd command on the command line.'
*Then type':
  `pip install --editable .`
  
## Using the Commands

You can always use the:

		`fld_cmp --help.` to search for help.
		
The syntax of the command is fld_cmp [PATH1] [PATH2] 1/2, 
where PATH1 represents the address of one of the folder you want to scan 
and PATH2 is the address of the folder you want to compare it to 
and finally you have to type: 
* 1  if you want to scan for similar files/folder
* 2 for different files/folders.
* 3 to sync the two directories.
  