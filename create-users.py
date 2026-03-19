#!/usr/bin/python3

# INET4031
# Amanda Mathison
# 03/18/2026
# 03/18/2026

# os: executes commands like adduser, passwrd
# re: filters the lines
# sys: reads input from standard input
import os
import re
import sys

def main():
    for line in sys.stdin:

        #Checks if the line starts with '#' which would be a command
        #It skips comments or non data lines in the input file
        match = re.match("^#",line)

        #Removes the white space and splits the line with ':'
	#Each line is supposed to contain 5 fields/categories
        fields = line.strip().split(':')

        #skips if the line doesn't have 5 fields
	#this code will only accept records that are properly formatted with 5 fields
        if match or len(fields) != 5:
            continue
        #Takes the user information from the specific fields
	#username: user's username
	#password: user's password
	#gecos: properly formatts the user's information
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #splits the group fields so that the user can be assigned to multiple groups
        groups = fields[4].split(',')

        #message that indicates that the user account is being created
        print("==> Creating account for %s..." % (username))

	#builds system command to create the user account with disabled password and specified user info
	#
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #keeps these commented to verify commands before execution
        #if it's uncommented it will execute the command and create the user account
        #print(cmd)
        os.system(cmd)

        #Displays a message indicating that the password is set
        print("==> Setting the password for %s..." % (username))
	#Creates the command to set the user's password
	#uses echo to send the password more than once
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Keeps commented to verify if it's correct
        #If it's uncommented it will set the user's password
        #print(cmd)
        os.system(cmd)

        for group in groups:
            #Checks if the group is not '-' which means their isn't a group assignment
	    #if it's valid it assigns the user to a specified group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
