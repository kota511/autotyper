import threading
import time
from pynput import keyboard, mouse

running = False

def click_function():
    while True:
        if running:
            mouse.Controller().click(mouse.Button.left)
        time.sleep(0.01)

def on_press(key):
    global running
    if key == keyboard.Key.shift:
        running = not running

listener = keyboard.Listener(on_press=on_press)
listener.start()

click_thread = threading.Thread(target=click_function, daemon=True)
click_thread.start()

while True:
    time.sleep(0.1)
