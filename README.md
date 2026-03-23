# INET 4031 User Creation Script
Abdirahman Farah

## Description
This script creates users, sets their passwords, and adds them to groups on a Linux system. It reads everything from an input file so you don’t have to do it manually.

## How it works
The script reads each line from the input file. Each line has the username, password, name, and groups. It creates the user, sets the password, and adds them to groups. If a line is wrong or starts with #, it skips it.

## How to run

Make it executable:
chmod +x create-users.py

Dry run:
./create-users.py < create-users.input

Run for real:
sudo ./create-users.py < create-users.input
