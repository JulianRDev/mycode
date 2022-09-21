#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   EXERCISE: LISTS, INPUT, PRINT, CONCATENATE, VARIABLES"""

def main():

    # creating a list
    wordbank= ["indentation", "spaces"]

    # creating list of students
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # append integer 4 to wordbank
    wordbank.append(4)

    #convert num into an integer
    num= int(input("Pick a student number!"))

    #slice one of the elements from the list tlgstudents and save returned name as variable
    student_name= tlgstudents[num]

    # print sentence using elements from tlgstudents list and student_name string
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()
