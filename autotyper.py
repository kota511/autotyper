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
    if key == Key.ctrl:
        running = True
        while running:
            left()
            right()

def on_release(key):
    global running
    if key == Key.ctrl:
        running = False
        time.sleep(0.5)

senser = keyboard.Listener(on_press=on_press, on_release=on_release)
senser.start()
while True:
    time.sleep(0.1)
#ADD WHAT YOU WANT TO AUTOTYPE INTO TEXT
# time.sleep(5)
# text = "Replace"
# for c in text:
#     my_keyboard.type(c)
#     time.sleep(0.1) #If system doesn't load your full text, up the number