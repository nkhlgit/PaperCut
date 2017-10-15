'''
Created on 25 Sep. 2017
@author: nikhil
This will read the aub.csv from c:\\tmp directory and adhust the balance.


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
directory='c:\\tmp\\'
inFile = 'aub.csv'
os.chdir(directory)

def main():
    with open( inFile, 'r', newline='\n') as f:
        next(f)
        rd = csv.reader(f)
        for row in rd:
            print("{0} {1}".format(row[0], row[1])) 
            uid = row[0]
            amt = float(row[1])
            server.api.adjustUserAccountBalance(token, uid, amt, 'Added amount by script')
            
if __name__ == "__main__":
    main()
    