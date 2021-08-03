# MicroPython SH1106 OLED driver
#
# Pin Map SPI for ESP8266
#   - 3v - xxxxxx   - Vcc
#   - G  - xxxxxx   - Gnd
#   - D7 - GPIO 13  - Din / MOSI fixed
#   - D5 - GPIO 14  - Clk / SCLK fixed
#   - D8 - GPIO 4   - CS (optional, if the only connected device)
#   - D2 - GPIO 5   - D/C
#   - D1 - GPIO 2   - Res (required, unless a Hardware reset circuit is connected)
#
# for CS, D/C and Res other ports may be chosen.
#
from machine import Pin, SPI
import sh1106

spi = SPI(1, baudrate=1000000)
#display = sh1106.SH1106_SPI(width, height, spi, dc, res, cs, rotate=0)
display = sh1106.SH1106_SPI(128, 64, spi, Pin(18), Pin(22), Pin(24))
display.sleep(False)
display.fill(0)
display.text('Testing 1', 0, 0, 1)
display.show()
