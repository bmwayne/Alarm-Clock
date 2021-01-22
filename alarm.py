import datetime
import playsound

alarmhour = int(input("what hour do you want to set the alarm?"))
alarmminute = int(input("what minute do you want to set the alarm?"))
amPm = str(input("am or pm?"))
print("Alarm Successfully Set!")
if(amPm == 'pm'):
    alarmhour += 12

while(True):
    if(alarmhour == datetime.datetime.now().hour and alarmminute == datetime.datetime.now().minute):
        print("wake up mando")
        playsound.playsound("D:\python\'alarmclock\'mandalorian.mp3")
        break