from random import randrange
from PIL import image, imageGrab
import pyautogui as pag
import win32gui as win
import time
import re
import pytesseract as tess
import json

with open('./lib/utilities.json', 'r') as f:
    util_json = json.load(f)


def pixel_search(lookup):
    zone = util_json['pixel'][lookup]
    image = __screenshot(zone['coords'])
    for x in range(1, image.width):
        for y in range(1, image.height):
            if image.getpixel(x, y) in zone['colors']:
                return True
    return False


def measure_bar(lookup):
    zone = util_json['pixel'][lookup]
    image = __screenshot(zone['coords'])
    y = round(image.height / 2, 0)
    for x in range(image.width, 1, -1):
        if image.getpixel(x, y) in zone['colors']:
            return (x / image.width) * 100
    return False


def read_zone(lookup):
    zone = util_json['pixel'][lookup]
    image = __screenshot(zone['coords'])
    processed_img = __image_to_text(image, zone['colors'])
    read_img = tess.image_to_string(processed_img)
    return __clean_string(read_img)


def click(x, y):
    pos_x, pos_y = __get_window_pos()
    return pag.click(x + pos_x, y + pos_y)


def send(key, hold=randrange(0.2, 0.3)):
    __win_activate()
    time.sleep(randrange(0.1, 0.3))
    pag.keyDown(key)
    time.sleep(hold)
    pag.keyUp(key)
    time.sleep(randrange(0.1, 0.3))


def move(path, sec):
    if path == 'left':
        send('a', sec)
    elif path == 'right':
        send('d', sec)
    elif path == 'up':
        send('w', sec)
    elif path == 'down':
        send('s', sec)


def __image_to_text(image, colors):
    for x in range(1, image.width):
        for y in range(1, image.height):
            if image.getpixel(x, y) in colors:
                image.putpixel(x, y, '0x000000')
            else:
                image.putpixel(x, y, '0xFFFFFF')
    return False


def __clean_string(string):
    return re.sub("[^a-zA-Z0-9 -]", string.lower())


def __get_window_pos():
    hwnd = win.FindWindow(None, "PokeOne")
    rect = win.GetWindowRect(hwnd)
    return rect[0], rect[1]


def __win_activate():
    hwnd = win.FindWindow(None, "PokeOne")
    if win.GetActiveWindow == hwnd:
        return 0
    else:
        return win.SetActiveWindow(hwnd)


def __screenshot(arr):
    pos_x, pos_y = __get_window_pos()
    x1 = arr[0] + pos_x
    y1 = arr[1] + pos_y
    x2 = arr[2] + pos_x
    y2 = arr[3] + pos_y
    return pil.ImageGrab(bbox=(x1, y1, x2, y2))
