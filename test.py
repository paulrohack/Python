import pyautogui, cv2
import numpy as np
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imshow('s', image)
cv2.waitKey(0)
#  cv2.imwrite("in_memory_to_disk.png", image)