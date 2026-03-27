INET4031 Add Users Script and User List

Abdirahman Farah

Program Description

This program helps automate the process of adding users to a Linux system. Instead of creating each user manually one at a time, the script reads user information from an input file and does the work for you. Normally, a system admin would have to use commands like adduser, passwd, and group commands by hand for every single user. This script uses those same commands, but it automates them so the process is faster, easier, and less likely to have mistakes.

Program User Operation

To use this program, the user first needs to create an input file that has the list of users in the right format. After that, the Python file should be made executable and then run from the terminal. The script will read the input file line by line and process each user. If a line is marked to be skipped or does not have the right format, the script will ignore it and move on.

Input File Format

Each line in the input file should have 5 fields separated by colons. The format is:

username:password:lastname:firstname:group1,group2

username is the login name for the new account
password is the password that will be set for that user
lastname is the user’s last name
firstname is the user’s first name
groups is the list of groups the user should be added to, separated by commas

If the user wants to skip a line, they should put # at the beginning of that line.
If the user should not be added to any extra groups, they should put - in the groups field.

Command Execution

Before running the program, the user may need to make the Python file executable with:

chmod +x create-users.py

Then the script can be run with:

./create-users.py < create-users.input

If running the script for real to create users on the system, it should be run with sudo:

sudo ./create-users.py < create-users.input
Dry Run

If the user chooses to do a dry run, the script will go through all the same steps without actually creating users or changing the system. Instead, it will print the commands that would have been run. This lets the user check the input and make sure everything looks right before running the script for real.
