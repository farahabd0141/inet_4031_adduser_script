#!/usr/bin/python3

# INET4031
# Abdirahman Farah
# Date Created: 03/23/2026
# Date Last Modified: 03/23/2026

# os is used to run Linux commands from inside the Python script.
# re is used for pattern matching, like checking if a line starts with #.
# sys is used to read input from standard input, which is the create-users.input file.
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Check if the line starts with #.
        # A line starting with # is treated like a comment or skip line in the input file.
        match = re.match("^#", line)

        # Remove extra spaces/newlines, then split the line by :
        # This turns one input line into a list of 5 fields.
        fields = line.strip().split(':')

        # Skip the line if it is marked as a comment or if it does not have all 5 required fields.
        # This prevents bad input lines from being processed.
        if match or len(fields) != 5:
            continue

        # Get the username and password from the input line.
        # Build the GECOS field, which stores the user's full name information in /etc/passwd.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the group field by commas so the script can process each group one at a time.
        groups = fields[4].split(',')

        # Let the user know the script is about to create the account.
        print("==> Creating account for %s..." % (username))

        # Build the Linux adduser command that creates the new account with no password set yet.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # During a dry run, leave these commented out so the script only shows what it would do.
        # If uncommented, the script will actually create the Linux user account.
        #print(cmd)
        #os.system(cmd)

        # Let the user know the script is about to set the password.
        print("==> Setting the password for %s..." % (username))

        # Build the command that sends the password twice into passwd so the account gets its password set.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # During a dry run, leave these commented out so the script only prints the command.
        # If uncommented, the script will actually set the password for the user.
        #print(cmd)
        #os.system(cmd)

        for group in groups:
            # Check if the group field is not "-".
            # A dash means the user should not be added to any extra groups.
            # If the group is not "-", the script adds the user to that group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print(cmd)
                #os.system(cmd)

if __name__ == '__main__':
    main()
