'''
Created on 16 Oct. 2017 
@author: nikhils
Download the user_list.csv and print_summary_by_user.csv from PaperCut User Reports and same them in "c:\tmp" location
This script read email address of users from "user_list.csv" and map them with user ID in "print_summary_by_user.csv" 
The Output file is "print_summary_by_user_Email.csv"
'''

import pandas as pd
import os
from itertools import islice

os.chdir('c:\\tmp\\')
infl1= 'user_list.csv'
infl2='print_summary_by_user.csv'
df1 = pd.read_csv(infl1 ,usecols=['Username','Email'], skiprows=1)
df2 = pd.read_csv(infl2 , skiprows=2)
df2 = df1.merge(df2, on='Username', how='right')
with open("print_summary_by_user.csv") as f1:
    head = list(islice(f1, 2))
with open("print_summary_by_user_Email.csv", "w") as f2:
    for item in head:
        f2.write(item)    
df2.to_csv('print_summary_by_user_Email.csv', mode = 'a')

if __name__ == "_main_":
    main()      