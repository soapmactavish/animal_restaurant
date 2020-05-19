import win32gui
import time
import sys
import keyboard
from multiprocessing import Process
import pyautogui

pyautogui.FAILSAFE = False
# pyautogui.PAUSE = 0.01


def get_hwnd():
    # hwnd_title = dict()
    #
    # def get_all_hwnd(hwnd, mouse):
    #     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
    #         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
    #
    # win32gui.EnumWindows(get_all_hwnd, 0)
    #
    # for hwnd, title in hwnd_title.items():
    #     if title == '动物餐厅':
    #         return hwnd
    # return 0

    return win32gui.FindWindow(None, '动物餐厅')


def get_cordinates(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return left, top, right, bottom


def get_pos():
    ori_width = 320
    # ori_height = 568

    hwnd = get_hwnd()
    if hwnd:
        x, y, right, bottom = get_cordinates(hwnd)
        cur_width = right - x
        ratio = cur_width * 1.0 / ori_width
        return x, y, ratio
    else:
        print('no program found!\nexiting in 5 seconds')
        time.sleep(5)
        sys.exit()


def special(x, y, ratio):
    while True:
        # table
        # print('clicking special table guest')
        pyautogui.click(x + 242 * ratio, y + 343 * ratio)
        pyautogui.click(x + 169 * ratio, y + 343 * ratio)
        pyautogui.click(x + 99 * ratio, y + 343 * ratio)
        pyautogui.click(x + 242 * ratio, y + 248 * ratio)
        pyautogui.click(x + 169 * ratio, y + 248 * ratio)
        pyautogui.click(x + 99 * ratio, y + 248 * ratio)
        for i in range(10):
            pyautogui.click(x + 306 * ratio, y + 551 * ratio)
        time.sleep(0.5)
        for i in range(10):
            pyautogui.click(x + 236 * ratio, y + 366 * ratio)

        # mouse
        # print('clicking mouse')
        pyautogui.click(x + 120 * ratio, y + 230 * ratio)
        time.sleep(0.5)
        pyautogui.click(x + 286 * ratio, y + 516 * ratio)
        time.sleep(0.5)
        for i in range(10):
            pyautogui.click(x + 100 * ratio, y + 485 * ratio)

        # bird
        # print('clicking parrot')
        for i in range(15):
            pyautogui.click(x + 240 * ratio, y + 180 * ratio)

        # onehour
        # print('clicking one hour notification')
        pyautogui.click(x + 161 * ratio, y + 361 * ratio)

        # feedback
        # print('clicking feedback')
        pyautogui.click(x + 236 * ratio, y + 366 * ratio)

        # order
        # print('clicking order')
        pyautogui.click(x + 265 * ratio, y + 306 * ratio)
        pyautogui.click(x + 193 * ratio, y + 306 * ratio)
        pyautogui.click(x + 120 * ratio, y + 306 * ratio)
        pyautogui.click(x + 265 * ratio, y + 212 * ratio)
        pyautogui.click(x + 193 * ratio, y + 212 * ratio)
        pyautogui.click(x + 120 * ratio, y + 212 * ratio)

        # print('sleeping 15 seconds')
        time.sleep(15)


def publicity(x, y, ratio):
    while True:
        pyautogui.click(x + 285 * ratio, y + 525 * ratio)


def quit():
    keyboard.record(until='escape')
    print('exiting program')


def main():
    x, y, ratio = get_pos()
    print('found animal restaurant windows')
    print('position: ', x, y, ratio)

    pool = []

    p = Process(target=special, args=(x, y, ratio, ))
    pool.append(p)

    for i in range(1):
        p = Process(target=publicity, args=(x + i, y + i, ratio, ))
        pool.append(p)

    for p in pool:
        p.start()
    
    p = Process(target=quit)
    p.start()
    
    print('program is running, click ESC to quit')

    p.join()

    for p in pool:
        p.terminate()
    
    print('all processes are terminated, exiting in 5 seconds')
    time.sleep(5)


if __name__ == '__main__':
    main()
