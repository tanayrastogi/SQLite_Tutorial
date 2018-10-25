# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:59:09 2018

@author: tanay
"""

import paramiko
import sqlite3
import pandas as pd
from datetime import datetime

def copy_database():
    # Commands to connect to remote server
    print('Connecting to the server....')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.163', port = 22, username='test', password='3cte')
    print('Connection Successful!')
    
    ## Commands to execure commands to the server
    #stdin, stdout, stderr = ssh.exec_command('sudo ls')
    #stdin.write('3cte')
    #print (stdout.readlines())
    
    # Commands to transfer file from remote to local
    print('Copying database from the remote to the local...')
    remotefilepath = '/opt/zyax-device/main.sqlite'
    localfilepath  = 'D:\Python\stuff2Plot.db'
    sftp_client = ssh.open_sftp()
    sftp_client.get(remotefilepath, localfilepath)
    sftp_client.close()
    print('Done!')
    
    
#copy_database()


# Connecting to the local SQL database
conn = sqlite3.connect('D:\Python\stuff2Plot.db')
c = conn.cursor()

# Read the database
df = pd.read_sql_query("SELECT * FROM measurements", conn, index_col=['id'])
print(df.head())
df['timestamp'] = pd.to_datetime(df['timestamp'])

### Plotting the data
#plt.plot_date
#df.plot(x=['timestamp'], y=['value'])

