from machine import Pin
from utime import sleep
import random

import machine
import asyncio

gpoLeds = {
    0: 6,
    1: 7,
    2: 8,
    3: 9,
    4: 10,
    5: 11,
    6: 12,
    7: 13
}

def writeLed(address, state):
    led = Pin(address, Pin.OUT)
    if int(state):
        led.high()
    else:
        led.low()
        
def resetLeds(leds):
    for led in leds:
        writeLed(leds[led], 0)

async def blink(pin, delay):
    led = machine.Pin(pin, machine.Pin.OUT)

    while True:
        led.toggle()
        print("blink pin: " + str(pin) + " delay(ms): " + str(delay))
        await asyncio.sleep_ms(delay)
        
async def main():
    resetLeds(gpoLeds)
    
    for led in gpoLeds:
        asyncio.create_task(blink(gpoLeds[led], random.randrange(100, 1000)))
    
    while True:
        print("done!")
        await asyncio.sleep_ms(1000)
        
        
asyncio.run(main())