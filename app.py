
from luma.core.interface.serial import i2c, spi, pcf8574
# from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010
from time import sleep
import socket
import psutil
import os
# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
# substitute bitbang_6800(RS=7, E=8, PINS=[25,24,23,27]) below if using that interface
serial = spi(device=0, port=0)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)


def Draw_Oled(msg: list):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        for i, line in enumerate(msg):
            draw.text((10, i*8+4), line, fill="white")


while True:
    ip_address = os.popen('ip addr show wlan0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
    host_name = socket.gethostname()
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(1)/100
    virtual_mem = psutil.virtual_memory()
    temps = psutil.sensors_temperatures()
    temp = 0
    for name, entrys in temps.items():
        temp = entrys[0].current
    msg = [
        f'IP: {ip_address}',
        f'MEM:     {round(virtual_mem.available/(1024*1024),3)}',
        f'MEM act.:{round(virtual_mem.active/(1024*1024),3)}',
        f'MEM free:{round(virtual_mem.free/(1024*1024),3)}',
        f'Temp:    {temp}',
        f'',
        f'           RPi4B8G']
    Draw_Oled(msg)
