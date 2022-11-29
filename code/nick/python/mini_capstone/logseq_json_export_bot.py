import pyautogui
from time import sleep


def logseq_json_export():
    pyautogui.press('win')
    sleep(1)
    pyautogui.write('logseq')
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click(x=1910, y=350)
    sleep(3)
    pyautogui.click(x=1740, y=580)
    sleep(3)
    pyautogui.click(x=900, y=820)
    sleep(3)
    pyautogui.write('daily-logseq.json')
    pyautogui.press('enter')
    pyautogui.click(x=1365, y=820)
    sleep(1)
    pyautogui.hotkey('alt', 'f4')
