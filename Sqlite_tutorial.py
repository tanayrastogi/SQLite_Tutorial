#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:34:11 2018

@author: tanay

SQlite Tutorial
https://www.youtube.com/watch?v=o-vsdfCBpsU
"""

import sqlite3
from datetime import datetime
import random
import time


# Connection to the database
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dataPlot (datetime TEXT, value REAL)')
    
def data_entry():
    c.execute("INSERT INTO dataPlot VALUES('2018-01-01', 65)")
    
    # To save the file once inserted into the database
    conn.commit()
    
    # To close the file once done
    c.close()
    conn.close()

def dynamic_data_entry():
    time_step  = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    value = random.randrange(1, 10)
    
    # Insert data to the database
    c.execute('INSERT INTO dataPlot (datetime, value) VALUES(?, ?)',(time_step, value))
    conn.commit()
    

    
  
create_table()
for i in range(1,10):
    dynamic_data_entry()
    time.sleep(2)

c.close()
conn.close()
    