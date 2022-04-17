import pyautogui

# 왼쪽 드래그 
pyautogui.dragTo(400, 500)
# 2초 동안 왼쪽 드래그 
pyautogui.dragTo(400, 500, 2)
# 2초 동안 오른쪽 드래그
pyautogui.dragTo(400, 500, 2, button='right')