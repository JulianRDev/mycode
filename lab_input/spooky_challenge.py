#!/usr/bin/python3
"""Spooky Chellenge | Julian 
   """


def main():

    vampire_count = 0

    #open file in read mode
    with open("dracula.txt","r") as spooky:
        with open("vampytimes.txt","w") as creepy:
            #loop over lines
            for line in spooky:
                #if the line contains the word vampire we want to print the line
                if "vampire" in line.lower():
                    #add to counter if condition met
                    vampire_count += 1
                    print(line)
                    #writes content into file
                    creepy.write(line)
    print(vampire_count)

main()
