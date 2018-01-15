'''
Created on 13 Sep. 2017
@author: nikhils

List down properties of users. This wull create UserIdProperty.csv' in C:\temp folder..
UserID','account-selection.mode','account-selection.can-charge-personal','account-selection.can-charge-shared-from-list','account-selection.can-charge-shared-by-pin''auto-shared-account','default-shared-account'
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
        ual= []
        ual = server.api.listUserAccounts(token, 0, 1000)
        with open('UserIdProperty.csv', 'w', newline='\n') as f:
            wr = csv.writer(f)
            wr.writerow(['UserID','account-selection.mode','account-selection.can-charge-personal',\
            'account-selection.can-charge-shared-from-list','account-selection.can-charge-shared-by-pin',\
            'auto-shared-account','default-shared-account'])
            
            for i in range(len(ual)):
                    p=server.api.getUserProperties(token, 'nikhils', ['account-selection.mode', 'account-selection.can-charge-personal',\
                                                       'account-selection.can-charge-shared-from-list','account-selection.can-charge-shared-by-pin',
                                                       'auto-shared-account', 'default-shared-account'])
                    print('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(ual[i], p[0], p[1], p[2], p[3], p[4], p[5]))
                    wr.writerow([ual[i], p[0], p[1], p[2], p[3], p[4], p[5]])

    
        
if __name__ == "__main__":
    main()