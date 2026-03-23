
#!/usr/bin/python3

# inet4031
# abdirahman farah
# date created: 03/23/2026
# date last modified: 03/23/2026

# os is used to run linux commands from inside the script
# re is used to check patterns like lines starting with #
# sys is used to read input from the file line by line
import os
import re
import sys

def main():
    # ask user if they want dry run or real run
    # dry run = just show commands, real run = actually create users
    answer = input("run in dry-run mode? y for yes, n for no: ").strip().upper()
    dry_run = answer == "Y"

    # loop through each line from the input file
    for line in sys.stdin:
        # check if line starts with # (means skip this line)
        match = re.match("^#", line)

        # split the line into parts using :
        # should give username, password, last name, first name, groups
        fields = line.strip().split(':')

        # skip lines that start with #
        # only show message if dry run is on
        if match:
            if dry_run:
                print("skipping line because it starts with #")
            continue

        # skip lines that don’t have all 5 parts
        # this prevents errors from bad input
        if len(fields) != 5:
            if dry_run:
                print("skipping bad line because it does not have 5 fields")
            continue

        # assign values from the line
        username = fields[0]
        password = fields[1]

        # gecos is used for storing user info in /etc/passwd (full name)
        gecos = "%s %s,,," % (fields[3], fields[2])

        # split groups by comma so we can add user to multiple groups
        groups = fields[4].split(',')

        # create the user account
        print("==> creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # if dry run, just print command
        # if not, actually run it
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # set the user password
        print("==> setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # same logic for dry run vs real run
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # add user to groups
        for group in groups:
            # "-" means no groups, so skip it
            if group != '-':
                print("==> assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)
            else:
                # only show this in dry run
                if dry_run:
                    print("no extra groups for %s" % (username))

if __name__ == '__main__':
    main()

