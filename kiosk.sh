#!/bin/bash
xset s noblank
xset s off
xset -dpms

unclutter -idle 0.5 -root &

# DRLA These lines did ot work out, I edited the Preference file manually
#sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
#sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

#/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://ds.iris.edu/seismon/index.phtml http://localhost:8081/page1.html http://localhost:8081/index.html &
/usr/bin/chromium-browser --noerrdialogs --kiosk --disable-inforbars http://ds.iris.edu/seismon/index.phtml http://localhost:8081/page1.html http://localhost:8081/index.html & 
/usr/bin/sudo /usr/bin/python3 /home/pi/kiosko/create_hourly_plot.py

while true; do
	sleep 15
	xdotool key ctrl+Tab; #xdotool keyup ctrl+Tab;
	currenttime=$(date +%M)
	if [[ "$currenttime" == "01" ]]; then

		/usr/bin/sudo /usr/bin/python3 /home/pi/kiosko/create_hourly_plot.py
		
		xdotool keydown ctrl+r; xdtool keyup ctrl+r;
		sleep 20
		xdotool key ctrl+Tab;
		xdotool keydown ctrl+r; xdtool keyup ctrl+r;
		sleep 20
		xdotool key ctrl+Tab;
		xdotool keydown ctrl+r; xdtool keyup ctrl+r;
		sleep 25
	fi
done

