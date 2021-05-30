import time, pyautogui
time.sleep(5)
f = open('lyrics2.txt', 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
print('listo papu')
