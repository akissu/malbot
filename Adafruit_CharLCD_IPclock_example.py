#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

cmd0 = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd1 = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

lcd.begin(16,1)

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

while 1:
	lcd.clear()
	eth0ipaddr = run_cmd(cmd0)
	wlan0ipaddr = run_cmd(cmd1)
	#lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
	lcd.message('eth:%s' % ( eth0ipaddr ) )
	lcd.message('wln:%s' % ( wlan0ipaddr ) )
	sleep(2)
