# Program Description

This program reads a file that contains user information and automatically the system commands to then create the users. The user doesn't need to feed them any information just prepare the correct input for the input file and then run the script. This program should be run in the terminal. 

## Input file format:

Each line of the input represents one of the file fields:
Username- is the account name of the user
Password- the password of the user
first name- used in the display name of the program
last name- used in the display name of the program
groups- groups are separated with a comma and have a '-' if a group is not needed
-if a line starts with '#' and doesn't have 5 fields it is then skipped

## Command Execution:
1. make sure you have both create-users files
2. run "chmod +x create-users.py"
3. run "sudo ./create-users.py < create-users.input"

## "Dry Run":

You can test the script without making any system changes.
Steps:
Comment out all lines containing:
os.system(cmd)
Uncomment the corresponding:
print(cmd)
This will display the commands that would be executed without actually creating users.

