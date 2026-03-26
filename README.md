# Program Description

This program reads an input file containing user account information and automatically executes system commands to create those users on a Linux system. The user does not need to manually enter information during execution; instead, they prepare the input file in the correct format and run the script. 

## Input file format:
Each line in the input file represents a single user and must contain exactly five fields separated by colons (:):

username:password:first_name:last_name:groups


Each line of the input represents one of the file fields:

* Username- is the account name of the user
* Password- the password of the user
* first name- used in the display name of the program
* last name- used in the display name of the program
* groups- groups are separated with a comma and have a '-' if a group is not needed
* if a line starts with '#' and doesn't have 5 fields it is then skipped
### Additional Rules
* Lines starting with # are treated as comments and skipped
* Lines that do not contain exactly 5 fields are ignored

## Command Execution:
1. make sure you have both create-users files
2. run "chmod +x create-users.py"
3. run "sudo ./create-users.py < create-users.input"

## "Dry Run":

You can test the script without making any system changes.
Steps:
1. Comment out all lines containing:
   os.system(cmd)
3. Uncomment the corresponding:
   print(cmd)

This will display the commands that would be executed without actually creating users.
