import urllib2,json
import requests

# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before.
tfile = open("/sys/bus/w1/devices/_siia_tuleb_anduri_ID_/w1_slave")
# Read all of the text in the file.
text = tfile.read()
# Close the file now that the text has been read.
tfile.close()
# Split the text with new lines (\n) and select the second line.
secondline = text.split("\n")[1]
# Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
temperaturedata = secondline.split(" ")[9]
# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
temperature = float(temperaturedata[2:])
# Put the decimal point in the right place and display it.
temperature = temperature / 1000

r = requests.get('http://192.168.1.222/emoncms/input/post.json?node=1&json={t1:'+str(temperature)+'}&apikey=_Sinu_API_v6ti_siia_')
