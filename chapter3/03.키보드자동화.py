import pyautogui
import pyperclip

# 1. 키보드 입력(문자)
pyautogui.write('startcoding')
pyautogui.write('startcoding', interval=0.25)
pyautogui.write('스타트코딩')

# 2. 키보드 입력(키)
pyautogui.press('enter')
pyautogui.press('up')

# 3.1 키보드 입력(ctrl + c)
pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')

# 3.2 hotkey 이용
pyautogui.hotkey('ctrl', 'c')

# 4. 한글 입력 방법
pyperclip.copy('스타트코딩')
pyautogui.hotkey('ctrl', 'v')