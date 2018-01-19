'''
Created on 18 Jan. 2018 @author: nikhils
This script is to create internal users in Bulk using web-xml API..
it reads batch-internal-user-example.tsv from c:\tmp directory and set properties.Please refrence.

Pros: Remove the dependency to access Server terminal access to run server command and put tsv file.
 
Critical steps before running the script:  
    - Install Python3; 
    - Enable Web-XML API on Server. Refer=> https://www.papercut.com/products/ng/manual/common/topics/tools-web-services.html
    - Create batch-internal-user-example.tsv file. 
      Refer => https://www.papercut.com/products/ng/manual/applicationserver/topics/user-guest-internal.html#user-guest-internal-import-file-format

'''
import csv
import os
from xmlrpc import client
from IPython.utils.tokenize2 import String
import time

# Set operation Location
OpsPath ='C:\\tmp\\'
os.chdir(OpsPath)
#Initiate LogFiles by writting time in it. Exception Condition
LogFile= 'addInternalUser.log'
localtime = time.asctime( time.localtime(time.time()) )
with open(LogFile, 'w+') as wLog:        
    Line=  localtime+ '\n'
    wLog.write(Line)

#Write in log file
def Log( e ):
    with open(LogFile, 'a') as wLog:
        Line = str(e)+ '\n'
        wLog.write(Line)
        wLog.close()
    return
        
    
if __name__ == '__main__':
    inFile= 'batch-internal-user-example.tsv'
    # # Replace the localhost with IP/Hostname of your PaperCut Application Server
    host_name = 'localhost'
    port = 9191
    print("Connecting to server {0} on port {1} ...".format(host_name, port))
    server = client.Server('http://%s:%d/rpc/api/xmlrpc' % (host_name, port))
     # #CHNAGE as per your admin password or auth token
    token = 'token'
    
    #print("Importing job from row: ", end=' ')
    with open(inFile, newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        #Header = next(reader)
        Header=["userName", "Password", "balance", "restricted","full-name","email", "department", "office", "primary-card-number", "card-pin", "notes", "secondary-card-number", "home" ]
        print(Header)
        i=0
        #Add only User from Each Row
        for row in reader:
            i +=1 
            userId = str(row[0]) 
            print(userId, ' ' ,end = '')
            pswd = str(row[1])
            # FullName,eMail, idNo, pinNo as ''. They will add them in setPropeties.
            try:
                Res = server.api.addNewInternalUser(token, userId, pswd, '', '' , '', '')  
            except Exception as e:
                print(e)
                Log(e)
                continue    
            print("Added,now setting-up Properties")
            #Set user properties
            properties= []
            j=1
            for PropertyVal in row[2:]:
                j+=1
                PropertyVal = str(PropertyVal)
                PropertyVal= PropertyVal.strip()
                if PropertyVal:
                    Property = [Header[j],PropertyVal] 
                    properties.append(Property)
            print(properties)
            try:
                server.api.setUserProperties(token, userId, properties)
            except Exception as e:
                print(e)                
                Log(properties)
                Log(e)
                continue                                           
    print("\nScript is completed. Check Users on PaperCut. Also check if any error logged in at: " + OpsPath + LogFile)

   
