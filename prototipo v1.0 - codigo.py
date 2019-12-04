from machine import Pin
from time import sleep

ledAmar = Pin(12, Pin.OUT)
ledVerde = Pin(14, Pin.OUT)
entrada1 = Pin(4, Pin.IN, Pin.PULL_UP)
entrada2 = Pin(5, Pin.IN, Pin.PULL_UP)
botReset = Pin(13, Pin.IN, Pin.PULL_UP)
ledAmar.off()
ledVerde.off()

while True:
    
  if entrada1.value() == 0:
    ledAmar.on()
    ledVerde.off()
  elif entrada2.value() == 0:
    ledAmar.off()
    ledVerde.on()
    
  if botReset.value() == 0:
    ledAmar.off()
    ledVerde.off()
 
  
