# Mouse and Keyboard Automation 
# we need PYAUTOGUI which allows python to control Keyboard and Mouse (not in built in module, must import)

import pyautogui
import time
print(pyautogui.size()) # displays resolution of screen (1920 width; 1080 height)
pyautogui.moveTo(100, 100, duration = 1) # mouse moves automatically where it starts from 100 pixels on the right and 100 pixels down and moves to the left. The left corner of the screen represent (0,0) (x,y)
pyautogui.moveRel(0, 50, duration = 2.5) # moves mouse relative to previous position (now 150 pixels down)
print(pyautogui.position()) # this displays the position of the mouse (x = 100, y = 150)

pyautogui.click(60, 20, duration = 0.5) # this clicks a button on the screen and in this case, it clicks on "File". Remember the smaller the number, the closer the values are to the top left of the screen

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# dragTo / dragRel ; same as before but now these hold the mouse button while moving 

pyautogui.dragRel

time.sleep(2)
pyautogui.dragTo(500, 500, duration = 1)
pyautogui.dragRel(100, 0, duration = 1)
pyautogui.dragRel(0, 100, duration = 1)
pyautogui.dragRel(-100, 0, duration = 1)
pyautogui.dragRel(0, -100, duration = 1)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pyautogui.moveTo(1100, 300, duration = 1)
pyautogui.scroll(-500) # scrolls down 
pyautogui.scroll(500) # scrolls up 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Browse Youtube and search for video 

pyautogui.moveTo(1300, 170, duration = 2)
pyautogui.click(1300, 170, duration = 0.2)
pyautogui.typewrite("Luka Doncic")
pyautogui.moveRel(0, 50, duration = 0.5)
pyautogui.click(0, 0, duration = 0.2) # the problem with this is that it triggers fail-safe mode. The better way to automate web browser is with the use of Selenium