'''
Created on 5 Sep. 2017
@author: nikhil Singh

This script will addjust amount to users listed in specific file.
create three files on 'Web-Service Client Machine': u20.txt, u15.txt and u7.txt.6. 
In u20.txt list down the name of all "User ID" (avoid any space ) seprated by new line who should be allocated £20. 
In u15.txt list down the name of all "User ID" (avoid any space ) separated by new line who should be allocated £15. 
In u7.txt list down the name of all "User ID" (avoid any space ) separated by new line who should be allocated £7.

'''

from xmlrpc import client
import os
import os.path

host_name = 'localhost'
port = 9191

print("Connecting to server {0} on port {1} ...".format(host_name, port))
server = client.Server('http://%s:%d/rpc/api/xmlrpc' % (host_name, port))

# Your admin password or auth token
auth_token = 'token'
loc='C:\\pc\\Py\\addCredit\\'

def addAmount(filename, amt):
    file = loc + filename
    if os.path.isfile(file) and os.access(file, os.R_OK):
        print ('File {0} exists and is readable'.format(file))
        f=open(file)
        for line1 in f:
            line=line1.rstrip('\n')
            if server.api.isUserExists(auth_token, line):
                current_balance = server.api.getUserAccountBalance(auth_token, line)
                print('The user {0} current balance is {1} ... '.format(line, current_balance), end= '')
                server.api.adjustUserAccountBalance(auth_token, line, amt, 'Added amount by script') 
                current_balance = server.api.getUserAccountBalance(auth_token, line)
                print('Now user {0} new balance is {1}'.format(line, current_balance))
            else:
                print("{0} :can't find in PaperCut".format(line))
    else:
        print ('Either file {0} is missing or is not readable'.format(file))

def main():
    addAmount('u20.txt', 20.00)
    addAmount('u15.txt', 15.00)
    addAmount('u7.txt', 7.00)
    
if __name__ == "__main__":
    main()
