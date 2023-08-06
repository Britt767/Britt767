
"""
Created on Mon Jul 17 19:44:17 2023

@author: byer7
"""

print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")

password = input("Enter your password: ")

count = 0;

while count < 3 and password != "secret":
    print("Not this time, toast monkey\n")
    print("Try again...")
    password = input("Enter your password: ")
    count = +1

if password == "secret":
    print("Access granted")
    
input("\n\nPress the enter key to exit.")