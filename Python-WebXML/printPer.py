'''
Created on 10 Sep. 2017 @author: nikhil Singh
Input file    :  print_logs_by_printer.csv in c:\tmp\ folder
Output file   : is target in c:\tmp\
Enter letter in 1St Arguments : a for all; h for hour;w for weekday;m for month number 
Example: 
    "printPer.py"   i.e. without argument will list Print per hour by default
    "printPer.py a" will print all data
    "printPer.py wd" will print week and day   
'''
import pandas as pd
import numpy as np
import os
import sys
import re

os.chdir('c:\\tmp\\')
inFile= 'print_logs_by_printer.csv'
df = pd.read_csv(inFile ,usecols=['Date','Printer Name', 'Total Printed Pages'], skiprows=2)
df['Date']=pd.to_datetime(df.Date, dayfirst=True)

def printPer(intrvl):
    if intrvl == 'hour':
        df[intrvl]=df.Date.dt.hour
    elif intrvl == 'weekday':
        df[intrvl]=df.Date.dt.weekday_name
    elif intrvl == 'day':
        df[intrvl]=df.Date.dt.day
    else:
        df[intrvl]=df.Date.dt.month
                         
    pph=df.pivot_table(index='Printer Name', columns=intrvl, values='Total Printed Pages',aggfunc=np.sum, margins=True )
    pph.to_csv('print_per_'+ intrvl + '.csv')
    df.drop(intrvl, axis=1, inplace=True)

def main():
    if len(sys.argv)<2:
        printPer('hour')
    elif re.search('.*a.*', sys.argv[1]):
                printPer('hour')
                printPer('weekday')
                printPer('day')
                printPer('month')
    else:
        if re.search('.*h.*', sys.argv[1]):
            printPer('hour')
        if re.search('.*w.*', sys.argv[1]):
            printPer('weekday')
        if re.search('.*d.*', sys.argv[1]):
            printPer('day')
        if re.search('.*m.*', sys.argv[1]):
            printPer('month')
            
if __name__ == "__main__":
    main()
    