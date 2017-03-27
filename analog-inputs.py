from gpiozero import MCP3008
from time import sleep
from neopixel import Adafruit_NeoPixel

r = MCP3008(channel=0)
g = MCP3008(channel=1)
b = MCP3008(channel=2)
LEDS = 12
PIN = 18

strip = Adafruit_NeoPixel(LEDS, PIN)
strip.begin()

while True:
    red = round(r.value * 255)
    green= round(g.value * 255)
    blue = round(b.value * 255)
    print(red,green,blue)
    for i in range(LEDS):
        strip.setPixelColorRGB(i, red, green, blue)
        strip.show()
    sleep(0.1)

