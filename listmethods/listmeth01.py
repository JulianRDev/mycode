#!/usr/bin/env python3

#create a list
proto = ["ssh", "http", "https"]

#create another list
protoa = ["ssh", "http", "https"]

#print the list
print(proto)

#print the second item on the list
print(proto[1])

#this will add "dns" to proto
proto.append("dns")
print(proto)

#this will add "dns" to protoa
protoa.append("dns")
print(protoa)

# a list of common ports
proto2 = [ 22, 80, 443, 53 ]

# pass proto2 as an argument to the extend method
proto.extend(proto2) 
print(proto)

# pass proto2 as an argument to the append method
protoa.append(proto2)
print(protoa)
