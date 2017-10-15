from xmlrpc import client
import os
import os.path

host_name = 'localhost'
port = 9191

print("Connecting to server {0} on port {1} ...".format(host_name, port))
server = client.Server('http://%s:%d/rpc/api/xmlrpc' % (host_name, port))

# Your admin password or auth token
token = 'token'
os.chdir('c:\\tmp\\')

def main():
	sal= []
	sal = server.api.listSharedAccounts(token, 0, 9)
	for i in range(len(sal)):
		pin=api.getSharedAccountProperty(token, sal[i], pin)
		print(pin)
	
if __name__ == "__main__":
    main()