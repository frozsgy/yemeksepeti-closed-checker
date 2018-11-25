import requests
import time

url = "https://www.yemeksepeti.com/cajun-corner-100-yil-ankara?status=closed"
r = requests.get(url)

while(1):
    if((r.content).find("beklemek istemiyor") > -1):
        print "meh still closed :/"
        time.sleep(1)
    else :
        print "IT'S OPEN NOW RUN RUN RUN"
        break
