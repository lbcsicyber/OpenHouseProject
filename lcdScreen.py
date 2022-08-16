import time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

def safe_exit(singal, frame):
    exit(1)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    lcd.text("hello", 1)
    lcd.text("Cutie", 2)

    pause()

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()