#!/usr/bin/env python3

#created list with three items
my_list = [ "192.168.0.5", 5060, "UP" ]

#firt item in the list 
print("The first item in the list (IP): " + my_list[0] )

#second item in list
print("The second item in the list (port): " + str(my_list[1]) )

#last item in list
print("The last item in the list (state): " + my_list[2] )

#new list for challenge
iplist =iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(f"These are just the IP addresses in the iplist: {iplist[3]}, {iplist[4]}!")
