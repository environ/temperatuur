# Temperatuuri ja keskkonna monitoorimine

Siia siis koondaks kokku vaarika riistvarale ja vabavaralistele lahendustele baseeruva teadmiste pagasi, mis toetavad keskkonnamõõdikute jälgimist.

Kasutatav riistvara:




	
Vajalik vaarika seadistamiseks:

	sudo modprobe w1-gpio
    sudo modprobe w1-therm
    cd /sys/bus/w1/devices/
    cd 10-000802cbxxxx
    cat w1_slave 

    sudo nano /etc/modules 
    
    lisa faili:
    	w1-gpio
		w1-therm


	wget https://bootstrap.pypa.io/get-pip.py
	sudo python get-pip.py 
	sudo pip install requests


	crontab -e
	*/1 * * * * python /home/pi/temperatuur_1.py

	
