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
#Asks the user is they want to do a dry run
    dry_run = input("Are you doing a dry run?(Y/N): ").strip().upper() == "Y"
    for line in sys.stdin:

        #Checks if the line starts with '#' which would be a command
        #It skips comments or non data lines in the input file
        match = re.match("^#", line)

        #Removes the white space and splits the line with ':'
	#Each line is supposed to contain 5 fields/categories
        fields = line.strip().split(':')

        #skips if the line doesn't have 5 fields
	#this code will only accept records that are properly formatted with 5 fields
        if len(fields) != 5:
            if dry_run:
                if match: #skips line if #
                    print("DRY RUN so skipping comment line:", line.strip())
            else: #skips if wrong number of fields
                print("DRY RUN so skipping lines with wrong number of fields:", line.strip())
            continue
        #Takes the user information from the specific fields
	#username: user's username
	#password: user's password
	#gecos: properly formatts the user's information
        username = fields[0]
        password = fields[1]
        groups = fields[4].split(',')
        gecos = "%s %s,,," % (fields[3],fields[2])

        #splits the group fields so that the user can be assigned to multiple groups
        groups = fields[4].split(',')

        #message that indicates that the user account is being created
        print("==> Creating account for %s..." % (username))

	#builds system command to create the user account with disabled password and specified user info
	#
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        if dry_run: #if in dry run just print the command instead of running it
            print("DRY RUN: Would run:", cmd) #
        else: # runs the command to create the user
            os.system(cmd)
        #keeps these commented to verify commands before execution
        #if it's uncommented it will execute the command and create the user account
        #print(cmd)

        #Displays a message indicating that the password is set
        print("==> Setting the password for %s..." % (username))
	#Creates the command to set the user's password
	#uses echo to send the password more than once
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        if dry_run: #prints the command that would set the password
            print("DRY RUN: Would run:", cmd)
        else: #runs the command to set the password
            os.system(cmd)
        #Keeps commented to verify if it's correct
        #If it's uncommented it will set the user's password
        #print(cmd)

        for group in groups:
            #Checks if the group is not '-' which means their isn't a group assignment
	    #if it's valid it assigns the user to a specified group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
            if dry_run: #dry runs prints the command instead of running it
                print("DRY RUN: Would run:", cmd)
            else: #runs the command to add the user to the group
                os.system(cmd)

if __name__ == '__main__':
    main()
