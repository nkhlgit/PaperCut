'''
Created on 13 Sep. 2017 @author: nikhil Singh

Usage: Please change host_name, token  and os.chdir() as per you Environment. 
Please refer #CHANGE String in Comment section
OutPut the File will create a "SharedAccountPin.csv" in C:\tmp directory. 
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

# #CHNAGE as per your admin password or auth token
token = 'token'
directory='c:\\tmp\\'
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory)

def main():
    sal= []
    sal = server.api.listSharedAccounts(token, 0, 1000)
    with open('SharedAccountPin.csv', 'w', newline='\n') as f:
        wr = csv.writer(f)
        wr.writerow(['UserID','pin'])
        for i in range(len(sal)):
            p=server.api.getSharedAccountProperty(token, sal[i], 'pin')
            print('{0}, {1}'.format(sal[i], p))
            wr.writerow([sal[i], p])
        
if __name__ == "__main__":
    main()