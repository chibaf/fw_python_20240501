import RPi.GPIO as GPIO
from time import sleep
import time
import sys
import os
import datetime

ont=float(sys.argv[1])
offt=float(sys.argv[2])

ssr_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr_pin,GPIO.OUT)

f=open("ssr12_log.txt",'a',encoding="utf-8")
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
d = now.strftime('%Y %m %d %H:%M:%S')
s1=d+": ssr_12 "+str(ont)+" "+str(offt)+" starts\n"
f.write(s1)
f.close()

path = './go12.txt'

while True:
  is_file = os.path.isfile(path)
  if is_file:
    print("find go12.txt\n")
  else:
    print("stop this proram")
    f=open("ssr12_log.txt",'a',encoding="utf-8")
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    d = now.strftime('%Y %m %d %H:%M:%S')
    s1=d+": ssr_12 "+str(ont)+" "+str(offt)+" stops\n"
    f.write(s1)
    f.close()
    GPIO.output(ssr_pin, False)
    exit()
  GPIO.output(ssr_pin, True)
  print("SSR 12 ON ("+str(ont)+"sec)\n")
  time.sleep(ont)
  GPIO.output(ssr_pin, False)
  print("SSR 12 OFF ("+str(offt)+"sec)\n")
  time.sleep(offt)
