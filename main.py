import time
from machine import Pin
import urequests
import network
import machine
from network import WLAN
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='WiFi ID', auth=(WLAN.WPA2, 'WiFi password'))
while not wlan.isconnected():
    machine.idle()
print("WiFi connected succesfully")
print(wlan.ifconfig())
print(wlan.ifconfig())
p2=Pin('G22', Pin.IN)
i = 1
while i>0:
    stan = p2.value()
    if stan == 1: 
        print ("Poziom zbiornika - OK")
        res = urequests.get('https://api.callmebot.com/whatsapp.php?phone=(phoneNumber)&text=Poziom+zbiornika+-+OK&apikey=ApiKey')
        print(res.text)
        time.sleep(60)
    else:
        print("Poziom zbiornika - MAKSIMUM")
        res = urequests.get('https://api.callmebot.com/whatsapp.php?phone=(phoneNumber)&text=Poziom+zbiornika+-+MAKSIMUM&apikey=ApiKey')
        print(res.text)
        time.sleep(60)

  

