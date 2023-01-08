#!/usr/bin/env python3
'''
StephanieCobble | Lab 33 - List objects & methods
Using extend & append
Added the use of insert
'''

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(f'proto: {proto}')
print(f'item at index 1 in proto: {proto[1]}')
proto.extend("dns") # adds dns to end of list
proto.append("dns")
protoa.append("dns")
print(f'Proto with dns {proto}')
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print('proto with proto2 added using extend: {proto}')
protoa.append(proto2) # pass proto2 as an argument to the append method
print(f'protoa with proto2 added using append: {protoa}')


protob = ["apple", "strawberry", "raspberry"]
print(f'protob: {protob}')
protob.insert(1, "orange")
print(f'protob with orange inserted at index 1: {protob}')
