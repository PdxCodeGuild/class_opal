import pyautogui
from time import sleep


def logseq_json_export():
    '''
    Opens Logseq and saves a json of all Logseq data to downloads with the name 'daily-logseq.json
    '''
    pyautogui.press('win')                # press windows key
    sleep(1)                              # give time for loading
    pyautogui.write('logseq')             # search for logseq
    pyautogui.press('enter')              # open logseq
    sleep(5)                              # give time for loading
    pyautogui.click(x=1910, y=350)        # click on options
    sleep(3)                              # give time for loading
    pyautogui.click(x=1740, y=580)        # click on 'export graph'
    sleep(3)                              # give time for loading
    pyautogui.click(x=900, y=820)         # click on 'export as json'
    sleep(3)                              # give time for loading
    pyautogui.write('daily-logseq.json')  # rename file to 'daily-logseq.json'
    pyautogui.press('enter')              # save the file
    pyautogui.click(x=1365, y=820)        # confirm overwrite of last save
    sleep(1)                              # give time for loading
    pyautogui.hotkey('alt', 'f4')         # exit logseq
