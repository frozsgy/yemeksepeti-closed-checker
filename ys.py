import sys
import os
import platform
import requests
import time

def screech():
    sys.stdout.write('\a')
    if platform.system() == 'Linux':
        os.system("aplay -q kaspersky.wav")
    elif platform.system() == 'Windows':
        os.system("start /min mplay32 /play /close karspersky.wav")

# Edit the following URL to match your own favourite order place
url = "https://www.yemeksepeti.com/cajun-corner-100-yil-ankara?status=closed"

while True:
    r = requests.get(url)
    if (r.content).find("beklemek istemiyor") > -1:
        print "meh still closed :/"
        time.sleep(1)
    else :
        print "IT'S OPEN NOW RUN RUN RUN"
        screech()
        break
