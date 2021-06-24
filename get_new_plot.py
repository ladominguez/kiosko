import os 
import time 

ssh_key='-i /home/pi/.ssh/grace_and_kiosko'
database='pi@192.168.0.21:/home/pi/ppm/air_quality.db'

x=os.stat('/home/pi/kiosko/ppm.png')
age=(time.time()-x.st_mtime)/3600 
#print("The age of the given file is: ",age)

if (age >= 1):
    os.system('scp %s %s .' % (ssh_key, database) )
    os.system('python3 /home/pi/kiosko/create_hourly_plot.py')

