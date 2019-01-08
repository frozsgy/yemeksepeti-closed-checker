import sys
import os
import platform
import requests
import time

def screech():
    if platform.system() == 'Linux':
        os.system("aplay -q kaspersky.wav")
    elif platform.system() == 'Windows':
        import winsound
        winsound.PlaySound('kaspersky.wav',winsound.SND_ALIAS)

url = raw_input('Paste the URL of the restaurant: ')

while True:
    r = requests.get(url)
    if (r.content).find("beklemek istemiyor") > -1:
        print "meh still closed :/"
        time.sleep(1)
    else :
        print "IT'S OPEN NOW RUN RUN RUN"
        screech()
        break
