#library name: pyautogui
# link: https://pyautogui.readthedocs.io/en/latest/

# pip install pyinstaller==5.13.2
# pip install PyScreeze==0.1.30
# pip install opencv-python==4.9.0.80
# pip install pillow==10.3.0
# pip install pefile==2019.4.18

import pyautogui
from time import sleep

start=pyautogui.locateCenterOnScreen("start.png",confidence=0.8)

pyautogui.moveTo(start)
sleep(2)
pyautogui.click()



# pyautogui.moveTo(259,739)
# sleep(2)
# pyautogui.click()
# pyautogui.moveTo(932,672)
# sleep(2)
# pyautogui.click()
# pyautogui.moveTo(926,561)
# sleep(2)
# pyautogui.click()
# sleep(2)
# pyautogui.click()


# # Continuously print the coordinates of the mouse cursor
# while True:
#     # Get the current position of the mouse
#     x, y = pyautogui.position()
#     # Print the coordinates
#     print(f'X: {x}, Y: {y}')