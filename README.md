# INET4031 Add Users Script and User List

## Program:
How the Code works: 
The code works by creating users and assigning them into groups on Linux.
Using python, it would add users, and groups where a user may not be assign.
Using import libraries like os, re, and sys to be more automated instead of System Admin manully adding each users and groups.

## Program User Operation:
For using the create-user.py code, you need to uncomment the os.system(cmd) in order for the user automation creaiton to work. If not, it would not run. When using the create-users2.py, It would ask the user if you want to run it in "Dry Mode" which is a test run. If not, it would run the actaul code.


### Input File Format:
Since the file is create-users.input, we are accesing the data using ./create-uers.py < createusers.input. Where all the users being created are stored. This lets reading the data insde, and be automated. 

### Command Excution:
The user runs the code using python3 ./create-users.py < createusers.input. This lets access the data inside the create-users.input file and being able to automated create users. 

### "Dry Run"
It's like a simulation of the actual code, but withouht actaully creating the users. This is a good way to test the code and see if it's before actually creating the users. 

