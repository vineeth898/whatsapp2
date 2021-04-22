import random
from datetime import date
import RPi.GPIO as GPIO
import pickle
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import os
data=[]
responses=[]
def setup():
    info=pickle.load(open("/home/pi/Desktop/Houseautomation/info.pickle",'rb'))
    GPIO.setup(2,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(3,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(4,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(17,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.output(2,info[0][1])
    GPIO.output(3,info[1][1])
    GPIO.output(4,info[2][1])
    GPIO.output(17,info[3][1])
    data1=["greeting",["hello","hi","Good","morning","afternoon","night","its", "nice","meet","pleasure","to","you","whats" ,"new","yo","yooooo"],[0]]
    data2=["greetingquestion",["how","are","doing","you","doing?","are","you","fine?","well?","fine","well","doing","you?"],[0]]
    data3=["bye",["bye","byeee","hope ","you","had","a","good","time","nice","talking","to","you","goodbye","bye","see","later","soon","ive","got","to","get","going","must","im","in","a","rush","off"],[0]]
    data4=["selfwhat",["who","are","you","what","are","you?","what","is","whats","name","name"],[0]]
    data5=["selfmaker",["who","made","made","you","you?","whose","your","maker","maker","maker?","what"],[0]]
    data6=["insutl",["your","a","an","idiot","stupid","idiot","stupid","dumb","dumb"],[0]]
    data7=["date",["whats","what","is","the","date","day","today","date"],[0]]
    d,ata8=["fanon",["fan","on","switch"],[0]]
    data9=["fanoff",["fan","off","of","switch"],[0]]
    data14=["light1on",["light1","1","light","on","switch"],[0]]
    data15=["light1off",["light1","1","light","off","of","switch"],[0]]
    data10=["light2on",["light2","2","light","on","switch"],[0]]
    data11=["light2off",["light2","2","light","off","of","switch"],[0]]
    data12=["otheron",["other","on","switch"],[0]]
    data13=["otheroff",["other","off","of","switch"],[0]]
    data16=["shutdown",["shutdown","shut","down","switchoff","switchof"],[0]]
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    data.append(data5)
    data.append(data6)
    data.append(data7)
    data.append(data8)
    data.append(data9)
    data.append(data10)
    data.append(data11)
    data.append(data12)
    data.append(data13)
    data.append(data14)
    data.append(data15)
    data.append(data16)

    data1=["greeting",["Yo!","hello","Vamos","yolooo","HOLOOOO","Long time no see!!!","pleasure to meet you"]," "]
    data2=["bye",["I would not love to meet you again","Byee","Would Like to meet you again","see Y'a","Nice talking to you,bye","Hope not to meet you again","BYE.","That wa squite a short conversation","hope to see you again"]," "]
    data3=["greetingquestion",["Im Doing just as fine as i did yesterday","Fine","Im fine","Im doing good"]," "]
    data4=["selfwhat",["Im Ursula made by master Srkipton","Im Ursula!","my name is Ursula"]," "]
    data5=["selfmaker",["Im made by Master Skripton","Skripton","The great Skripton","Master Skripton, the great youtuber"]," "]
    data6=["insutl",["NOOOOOOOOOOOOOOOO you are","You insult me??, wait till robots take over the world, youll be the first one to be killed","wait till Elon finishes his work takes over the world with robots, your going to be the first one to die","Your going to regret"]," "]
    data7=["date",[],"date"]
    data8=["fanon",[],"fanon"]
    data9=["fanoff",[],"fanoff"]
    data14=["light1on",[],"light1on"]
    data15=["light1off",[],"light1off"]
    data10=["light2on",[],"light2on"]
    data11=["light2off",[],"light2off"]
    data12=["otheron",[],"otheron"]
    data13=["otheroff",[],"otheroff"]
    data16=["shutdown",[],"shutdown"]
    responses.append(data1)
    responses.append(data2)
    responses.append(data3)
    responses.append(data4)
    responses.append(data5)
    responses.append(data6)
    responses.append(data7)
    responses.append(data8)
    responses.append(data9)
    responses.append(data10)
    responses.append(data11)
    responses.append(data12)
    responses.append(data13)
    responses.append(data14)
    responses.append(data15)
    responses.append(data16)
def type(Sen):
    mostlytype=" "
    global data
    Sen=Sen.lower()
    Sen=Sen.split(" ")
    mostscore=0
    for List in data:
        for words in List[1]:
            if(List[2][0]>mostscore):
                mostscore=List[2][0]
                mostlytype=List[0]
            for senword in Sen:
                if senword==words:
                    List[2][0]=List[2][0]+1
    if(mostscore==0):
        mostlytype="dnms"
    for x in data:
        if(x!=0):
            x[2][0]=0
        else:
            x[2][0]=1
    return(mostlytype)

def response(typ):
    global responses
    for n in responses:
        if(typ!="dnms"):
            if(n[0]==typ and n[2]==" "):
                return(n[1][random.randint(0,len(n[1])-1)])
            elif(n[0]==typ and n[2]!=" "):
                return(dowork(n[2]))
        else:
            return("no")
def dowork(work):
    info=pickle.load(open("/home/pi/Desktop/Houseautomation/info.pickle",'rb'))
    cr=["okay","doing","Will do","OKAY","Eh","Okay!"]
    if(work=="date"):
        return(date.today())
    if(work=="fanon"):
        GPIO.output(2,info[0][0])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="fanoff"):
        GPIO.output(2,info[0][1])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="light1on"):
        GPIO.output(3,info[1][0])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="light1off"):
        GPIO.output(3,info[1][1])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="light2on"):
        GPIO.output(4,info[2][0])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="light2off"):
        GPIO.output(4,info[2][1])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="otheron"):
        GPIO.output(17,info[3][0])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="otheroff"):
        GPIO.output(17,info[3][1])
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="shutdown"):
        os.system('sudo shutdown')
def getresponse(INPUT):
    TyPE=type(INPUT)
    Xesponse=response(TyPE)
    return(Xesponse)