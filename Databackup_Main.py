# !/usr/bin/python
import os
import sys
import subprocess
from os.path import join, getsize
#from collections import counter
from pandas import DataFrame, Series 
import pandas as pd 
import csv
import numpy as np
from datetime import datetime
import glob
from subprocess import Popen, PIPE
import commands
from dateutil.parser import parse
import pathlib
import time
import platform
import datetime
from pathlib import Path
from datetime import date, timedelta 
from pytz import common_timezones, all_timezones
import os.path, time
import subprocess

#Analyze Time within the block
data = pathlib.Path('/media/jennifer/')
#print(data)
#print(data.stat())
#print(type(data.stat()))


st = data.stat()
#print(st.st_atime)
#print(type(st.st_ctime))


#def daterange(start_date, end_date):
#	for n in range(int((end_date + start_date).days)):
#	    yield start_date + timedelta(n)
#start_date = []
#end_date = []
#for single_date in daterange(start_date, end_date):
#	print(single_date.strftime("%Y-%m-%d"))

#Make a date range including timestamps using pandas, can control the frequency of how far back it is is called 

#index = pd.date_range('01/01/2021 00:00:00','12/31/2022 00:00:00', freq = 'D')
#print(index)
padlocktime = pd.date_range(start = '01/01/2021 00:00:00', end ='12/31/2022 12:59:00', freq = 'D', tz ='UTC')

#print("Last modified: %s" %time.ctime(os.path.getmtime(r'/media/jennifer/')))
#print("Created: %s" %time.ctime(os.path.getmtime(r'/media/jennifer/')))

#look into size
#Returns back information on size of files but only does so based on the files being in Bytes - will have to create a loop to convert larger files into bytes in order for more samples to be included in analysis
Path(r'/media/jennifer/').stat()
file = Path(r'/media/jennifer/').stat().st_size
file_size = os.path.getsize(r'/media/jennifer/')
#print(file_size)


#Calculate file size(s) in Kb, MB, GB or lager
def convert_bytes(size):
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if size < 1024.0:
			return "%3.1f %s" % (size, x)
		size /= 1024.0
f_size = os.path.getsize(r'/media/jennifer/')
x = convert_bytes(f_size)
#print(x)
fs1 = x
#print(fs1)

#Pull out the directories, roots and Misc Files/Folders
path = '/media/jennifer/'
def walklevel(path, depth = 1):
    if depth < 0:
        for root, dirs, files in os.walk(path):
            yield root, dirs[:], files
        return
    elif depth == 0:
        return

    base_depth = path.rstrip(os.path.sep).count(os.path.sep)
    for root, dirs, files in os.walk(path):
        yield root, dirs[:], files
        cur_depth = root.count(os.path.sep)
        if base_depth + depth <= cur_depth:
            del dirs[:]

#os.system(cmd)
#padlock = cmd
#print(os.system)
#print commands.getstatusoutput('ls -slh')



#for root, dirs, files in os.walk('/media/jennifer'):
#	print root, "*",
#	print sum(getsize(join(root, name)) for name in dirs), 
#	print "modified", 


dir_list = []
for i in walklevel(path, depth = 5):
    dir_list.append(i)
column_names = ['root', 'directories', 'files']
df = pd.DataFrame(dir_list, columns=column_names)
#print(df)
df.to_csv("padlock_databackup.tsv", sep='\t')
#pd.read_csv("padlock_databackup.tsv", sep = '\t')
#df.info() #can check pandas core Data Frame


#for root, dirs, files in os.walk('/media/jennifer's):
#os.system('/media/jennifer')
#print(os.system)
#cmd = '''sudo ls -slh %s'''%('/media/jennifer')
cmd = '''sudo du -sh %s'''%('/media/jennifer')
linuxdata = subprocess.check_output(cmd, shell= True).split('\n')
print(linuxdata)
output_list =linuxdata
print(output_list)
