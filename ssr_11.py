import RPi.GPIO as GPIO
from time import sleep
import time
import sys
import os

ssr_pin = 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr_pin,GPIO.OUT)

ont=float(sys.argv[1])
offt=float(sys.argv[2])

path = './go11.txt'

while True:
  is_file = os.path.isfile(path)
  if is_file:
    print("find go11.txt\n")
  else:
    print("stop this proram")
    GPIO.output(ssr_pin, False)
    exit()
  GPIO.output(ssr_pin, True)
  print("SSR 11 ON ("+str(ont)+"sec)\n")
  time.sleep(ont)
  GPIO.output(ssr_pin, False)
  print("SSR 11 OFF ("+str(offt)+"sec)\n")
  time.sleep(offt)
