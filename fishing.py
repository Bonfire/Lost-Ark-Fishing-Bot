import time
import random

import cv2
import keyboard
import numpy as np

from PIL import ImageGrab

shouldCast = True
fishingTemplate = cv2.imread('fishing_template.png', 0)
templateWidth, templateHeight = fishingTemplate.shape[::-1]

print("Starting bot in 5 seconds!")
time.sleep(5)
print("Started!")

while True:
    if (shouldCast):
        print("Casting out lure")
        keyboard.press_and_release('e')
        shouldCast = False
        continue

    imagePixels = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    pixelsNumpy = np.array(imagePixels)

    grayscaleImage = cv2.cvtColor(pixelsNumpy, cv2.COLOR_BGR2GRAY)
    templateMatch = cv2.matchTemplate(
        grayscaleImage, fishingTemplate, cv2.TM_CCOEFF_NORMED)
    matchLocations = np.where(templateMatch >= 0.8)

    for point in zip(*matchLocations[::-1]):
        if point != None:
            print("Detected catch! Reeling in lure")
            keyboard.press_and_release('e')
            shouldCast = True
            time.sleep(random.uniform(6, 7.5))
            break

    time.sleep(0.100)
