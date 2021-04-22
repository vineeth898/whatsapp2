import pyautogui as p
import time
import pyperclip
import Ai
import pickle
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
data=pickle.load(open("/home/pi/Desktop/Houseautomation/info.pickle",'rb'))
time.sleep(10)

def openchat():
    p.click(61,16)
    time.sleep(30)
    p.click(502,288)
    time.sleep(1)
    p.hotkey('ctrl','r',interval=0.1)
    time.sleep(10)
    p.click(397,117)
    time.sleep(0.5)
    p.write('web.whatsapp.com')
    time.sleep(0.1)
    p.press('enter')
    time.sleep(120)
    p.click(122, 219)
    time.sleep(5)
    p.write('bot')
    time.sleep(5)
    p.moveTo(125, 340)
    time.sleep(5)
    p.click()
    p.sleep(1)
def check():
    if(p.pixelMatchesColor(526, 627,(255,255,255))):
        return(True)
    else:
        return(False)
def getmessage():
    p.moveTo(535, 621)
    p.tripleClick()
    p.sleep(0.5)
    p.hotkey('ctrl','c',interval=0.1)
    p.sleep(0.1)
    return(pyperclip.paste())
def sendmessage(message):
    p.click(623, 689)
    time.sleep(0.2)
    pyperclip.copy(message)
    p.hotkey('ctrl','v')
    p.press('enter')
    time.sleep(2)
openchat()
Ai.setup()
sendmessage("im up!")
time.sleep(2)
while True:
    if(check()==1):
        message=getmessage()
        if(message[0]!="!"):
            sendmessage(Ai.getresponse(message))
        else:
            if(message[1]=="f"):
                data[0]=[(data[0][0]+1)%2,(data[0][1]+1)%2]
                print(data)
            elif(message[1]=="1"):
                data[1]=[(data[1][0]+1)%2,(data[1][1]+1)%2]
                print(data)
            elif(message[1]=="2"):
                data[2]=[(data[2][0]+1)%2,(data[2][1]+1)%2]
                print(data)
            elif(message[1]=="o"):
                data[3]=[(data[3][0]+1)%2,(data[3][1]+1)%2]
                print(data)
            pickle.dump(data,open("/home/pi/Desktop/Houseautomation/info.pickle",'wb'))
            sendmessage("Changed")
        time.sleep(0.1)
