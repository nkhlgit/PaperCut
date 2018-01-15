'''
Created on 5 Jan. 2018 @author: nikhil
This will  read the CSV and import Job logs from "c:\temp\Joblog_template.csv" to PaperCut Server
using Web XML API: https://www.papercut.com/products/ng/manual/common/topics/tools-web-services.html
Fill the printlog_template.csv having job details as per PaperCut Specifications https://www.papercut.com/products/ng/manual/common/topics/tools-importing-jobs.html.
No Need to change date format as per the guide, Python Script should be able to covert the date to yyyyMMddTHHmmss format

The line starting with "# #" need to be chnage to adopt the script as per your environment.
'''

import pandas as pd
import os
from xmlrpc import client
import datetime, dateutil.parser


if __name__ == '__main__':
    os.chdir('c:\\tmp\\')
    inFile= 'Joblogs_template.csv'
    df = pd.read_csv(inFile)
	# # Replace the localhost with IP/Hostname of your PaperCut Application Server
    host_name = 'localhost'
    port = 9191
    print("Connecting to server {0} on port {1} ...".format(host_name, port))
    server = client.Server('http://%s:%d/rpc/api/xmlrpc' % (host_name, port))
     # #CHNAGE as per your admin password or auth token
    token = 'token'
    df1 = df.where((pd.notnull(df)), "null")
    j=0
    print("Importing job from row: ", end=' ')
    for row in df1.itertuples():
        j +=1
        print(j,  end=' ')
        inString= "user=" + row[1] + ",server=" + row[2] + ",printer=" + row[3]
        if row[4] != "null":
            inString = inString + ",time=" + (dateutil.parser.parse(row[4]).strftime("%Y%m%dT%H%M%S"))
        # initilaize the column name count, coumn count is 1 less as it dosen't conten index. 
        i = 4
        for col in row[5:]:
                if col != "null":
                    Header= df1.columns[i]
                    inString = inString + (",{0}={1}".format(Header, col))
                i += 1
        server.api.processJob(token,inString)
    print("\nIn case , now error showwn, probably done")  