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

def check(url):
    while True:
        r = requests.get(url)
        page = r.content
        if (page.find("beklemek istemiyor".encode()) + page.find("anda servis vermemektedir".encode())) > -2:
            now = time.strftime("%H:%M:%S")
            print(now + " - meh still closed :/")
            time.sleep(1)
        else :
            print("IT'S OPEN NOW RUN RUN RUN")
            screech()
            break

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1 :
        url = args[1]
    else :
        url = input('Paste the URL of the restaurant: ')
    try:
        check(url)
    except KeyboardInterrupt:
        print("Aight, imma check myself out!")
        exit()
