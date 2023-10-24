import time
from pynput.keyboard import Key, Controller

my_keyboard = Controller()

time.sleep(2)

text = "hello"
for c in text:
    my_keyboard.type(c)
    time.sleep(0.001)
