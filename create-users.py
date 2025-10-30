#!/usr/bin/python3

# INET4031
# Andy Rojas Sanchez
# Data Created: 10/28/2025
# Data Modified: 10/30/2025

'''
How the Code works
    The code works by creating users and assigning them into groups on Linux.
    Using python, it would add users, and groups where a user may not be assign.
    Using import libraries like os, re, and sys to be more automated instead of System Admin manully adding each users and groups.
'''

# Imports: Libraries that Python can't normally due
#  	os: To be able to use OS commands 
#	re: To be able to read and detect lines with special symbols like "#" 
#	sys: To be able to use read lines from stdin

import os
import re
import sys

def main():
    for line in sys.stdin:

	#Read the lines and detect "#" if so, skip the line.
	#The reason of this when searching and setting up groups for users.
      	
	#print(match)
	 match = re.match("^#",line)

    #The reason of line strip is due to the way it's format, it's split into 5 section
	#Username, password,Last_Name, First_Name, group 
        fields = line.strip().split(':')

	#The logic here is: If the match character match with the symbol or have less than 5, then skip
	#The reason being  the # is normally comments and preventing to have error or incorrect data output  
        if match or len(fields) != 5:
            continue

	#The purpose of the next three lines is to have bettter organization and to be able to put into groups
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

	#The reason of the split so it be better readibility in the database.
	#The bigger reason, if there were multiple group listed, it can still split. It be easier to work with later on. 
	#Example: user01, temppassword, Robert, Robertson, group01, group02
        groups = fields[4].split(',')

	#The point of this print statement is to let the user know the account being created,instead of just assuming it's not working
    #It's to let who's ever working with this know it's working
	    print("==> Creating account for %s..." % (username))

	#The line is  doing is adding the information towards the system. The cmd contain the shell command to be able to add it into the system 
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)


	#If it's first time running, you should unccoment the print statement to see if the code is working
	#The os.system would do is would use the cmd shell command to add the user from the user input and add it towards the actual system.
 
        #print cmd
        os.system(cmd)

        #Similiar to printing user account, it telling the person (system admin), that it's setting up a password for the user.
        print("==> Setting the password for %s..." % (username))

	#Similiar to previous command, it's now creaing the password with the shell command. Using the sudo command to be able to do the task.
	#The only difference, it's storing the same password, since it would need the user to confirm the password
	#Leading to have access the cmd and see if the password match.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd

	#If it's your first time running the code, you should comment the os.system to so that it's doesn't create a group or user when testing the code.
	#If left uncomment, it would try to attempt to run the priveous code and create user, password, and group and add it towards the system.
        os.system(cmd)

        for group in groups:
	#The if statment is looking for if there's a empty group "-" in the groups section.
	# If not, it can be assing to a group
	        if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
               	#print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()

