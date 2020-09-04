import pyautogui
import time

#Hello
#I have to write what you want to tell
#After running where you will click, it will post there
#So change it everytime what you want to tell.
#Thank you.
what_to_write = ["Hello","I am a Auto Writer","Created by Hemel",
                 "My wrok is to write insted of Hemel where he puts the mouse course click","Is't my work is awesome?","I will write any instruction that wull be given to me","Thank you."]

time.sleep(5)

for i in range (len(what_to_write)):
    pyautogui.typewrite(what_to_write[i])
    pyautogui.typewrite("\n")
    time.sleep(3)
    