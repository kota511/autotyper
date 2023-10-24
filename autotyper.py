import time
from pynput import keyboard
from pynput.keyboard import Key, Controller

my_keyboard = Controller()
def cmdv(): #to test
    with my_keyboard.pressed(Key.cmd):
        my_keyboard.type('v')
def left():
    my_keyboard.press(Key.left)
    time.sleep(0.1)
    my_keyboard.release(Key.left)
def right():
    my_keyboard.press(Key.right)
    time.sleep(0.1)
    my_keyboard.release(Key.right)

running = False

def on_press(key):
    global running
    if key == Key.ctrl and not running:
        running = True
        while running:
            left()
            right()

def on_release(key):
    global running
    if key == Key.ctrl and running:
        running = False


senser = keyboard.Listener(on_press=on_press, on_release=on_release)
senser.start()
time.sleep(10)
senser.stop()

#ADD WHAT YOU WANT TO AUTOTYPE INTO TEXT
# time.sleep(5)
# text = "Replace"
# for c in text:
#     my_keyboard.type(c)
#     time.sleep(0.1) #If system doesn't load your full text, up the number