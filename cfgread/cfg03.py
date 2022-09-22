#!/usr/bin/env python3

line_count = 0

file_name = input("what file should I load? : ")
## create file object in "r"ead mode
with open(file_name, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    for config in configlist:
        line_count += 1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(line_count)
print(configlist)

