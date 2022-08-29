import pyautogui
import time

# 화면 크기 출력
print(pyautogui.size())

# 마우스 위치 좌표 확인
time.sleep(2)
print(pyautogui.position())

# 마우스 이동
pyautogui.moveTo(300, 200)

# 2초 동안 이동
pyautogui.moveTo(300, 200, 2)

# 왼쪽 클릭 
pyautogui.click()

# 더블 클릭
pyautogui.doubleClick()

# 오른쪽 클릭
pyautogui.click(button="right")

# 왼쪽 1초 마다 클릭 (3번)
pyautogui.click(clicks=3, interval=1)

# 왼쪽 드래그 
pyautogui.dragTo(400, 500)

# 2초 동안 왼쪽 드래그 
pyautogui.dragTo(400, 500, 2)

# 2초 동안 오른쪽 드래그
pyautogui.dragTo(400, 500, 2, button='right')