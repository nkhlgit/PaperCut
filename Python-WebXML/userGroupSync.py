'''
Created on 27 Sep. 2017
@author: nikhil

This script will run UseAnd Group Synch whenever it runs
#
'''

from xmlrpc import client
import os
import os.path
import csv

# #CHNAGE it as your application Server IP/hostname
host_name = 'localhost'
port = 9191
print("Connecting to server {0} on port {1} ...".format(host_name, port))
server = client.Server('http://%s:%d/rpc/api/xmlrpc' % (host_name, port))

# #CHNAGE as per your admin password, auth token and inFile
token = 'token'


def main():
	server.api.performUserAndGroupSync(token)
            
if __name__ == "__main__":
    main()
    