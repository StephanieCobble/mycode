#!/usr/bin/env python3
'''
StephanieCobble | Lab 30 - Working with lists

'''
# create a list with 3 items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display first item
print("The first item in the list (IP): " + my_list[0] )

# display second item
print("The second item in the list (port): " + str(my_list[1]) )

# display last item
print("The last item in the list (state): " + my_list[2] )


#Challenge: Show only the IP addresses from a list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(f'IP addresses: {iplist[3]}, {iplist[4]}')
