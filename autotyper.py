import time
import threading
from pynput import keyboard
from pynput.keyboard import Key, Controller

my_keyboard = Controller()

def left():
    my_keyboard.press(Key.left)
    time.sleep(0.1)
    my_keyboard.release(Key.left)

def right():
    my_keyboard.press(Key.right)
    time.sleep(0.1)
    my_keyboard.release(Key.right)

running = False

def move_left_right():
    while running:
        left()
        right()

def on_press(key):
    global running
    if key == Key.shift:
        if not running:
            running = True
            threading.Thread(target=move_left_right).start()
        else:
            running = False

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the program running
while True:
    time.sleep(0.1)

#ADD WHAT YOU WANT TO AUTOTYPE INTO TEXT
# time.sleep(5)
# text = "Replace"
# for c in text:
#     my_keyboard.type(c)
#     time.sleep(0.1) #If system doesn't load your full text, up the number