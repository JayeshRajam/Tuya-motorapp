#!/usr/bin/env python
import time
import coloredlogs
from tuyalinksdk.client import TuyaClient
from tuyalinksdk.console_qrcode import qrcode_generate
coloredlogs.install(level='DEBUG')
import serial
 # Define the serial port and baud rate.
ser = serial.Serial('COM11', 115200)
flag = None
stat ='0'
client = TuyaClient(productid='0wwcdnfsph5ye5nu',
                    uuid='tuya3109c5966245faa1',
                    authkey='JryUNf86h02PhnRJccdIDATZKdLRtnAN')

def on_connected():
    print('Connected.')

def on_qrcode(url):
    qrcode_generate(url)

def on_reset(data):
    print('Reset:', data)

def on_dps(dps):
    global flag
    print('DataPoints:', dps)
    if(dps=={'101':False}):
        flag=False
    if(dps=={'101':True}):
        flag=True
    else:
        global stat
        stat = str(dps.get('102',"Nil"))
    client.push_dps(dps)

client.on_connected = on_connected
client.on_qrcode = on_qrcode
client.on_reset = on_reset
client.on_dps = on_dps

client.connect()
client.loop_start()

while True:
    if(flag==False):
        print("FAN is off...")
        ser.write(b'L')
        time.sleep(0.1)
    if(flag==True):
        print("FAN is on...")
        ser.write(stat.encode())
        time.sleep(0.1)
        print(ser.readline().decode('ascii'))
    time.sleep(1)