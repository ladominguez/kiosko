
import matplotlib.pyplot as plt
#import numpy
import sqlite3
import pandas
import matplotlib.dates as md
from datetime import datetime

import os
import time

# Update data base is image is older than 1 hour
ssh_key='-i /home/pi/.ssh/grace_and_kiosko'
database='pi@192.168.0.21:/home/pi/ppm/air_quality.db'

x=os.stat('/home/pi/www/ppm.png')
age=(time.time()-x.st_mtime)/3600
#print("The age of the given file is: ",age)

if (age >= 0.9):
    os.system('scp %s %s /home/pi/kiosko/' % (ssh_key, database) )
    #os.system('python3 /home/pi/kiosko/create_hourly_plot.py')

# Create new plot

plt.rcParams['timezone'] = 'Mexico/General'
tnow=datetime.now().strftime("%Y%m%d%H%M%S")

cmd_sql = r"select  *,datetime(ts,'unixepoch','localtime')  from measurements2 where ts >= (select strftime('%s',(select datetime('now','-24 hour','localtime'))))"

db = sqlite3.connect("/home/pi/kiosko/air_quality.db")
df = pandas.read_sql_query(cmd_sql, db)
df2 = df

df2['m1_0_cf1'] = df2['m1_0_cf1'].clip(upper=500)
df2['m2_5_cf1'] = df2['m2_5_cf1'].clip(upper=500)
df2['m10_0_cf1'] = df2['m10_0_cf1'].clip(upper=500)
df2['ts'] = pandas.to_datetime(df2['ts'], unit='s')

df2.plot(x='ts',y=['m1_0_cf1', 'm2_5_cf1', 'm10_0_cf1'])
date_form = md.DateFormatter("%y/%m/%d %H:%M")
plt.gca().xaxis.set_major_formatter(date_form)
plt.title('Sinatel, Mexico')
plt.grid()
plt.savefig('/home/pi/www/ppm.png')


