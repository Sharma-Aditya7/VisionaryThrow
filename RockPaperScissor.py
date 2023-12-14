import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import random
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#   ====================================================================================================
#   The parameters will have to be re-tuned when overlaying on the final bg
#   ====================================================================================================

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0, 0]

while True:
    imgBG = cv2.imread('Resources/BG.png')
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)  # Using it to resize the image on a scale
    imgScaled = imgScaled[:, 80:480]

    # Find Hands
    hands, img = detector.findHands(imgScaled)

    if startGame:

        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1                      #Rock
                    if fingers == [1, 1, 1, 1, 1]:
                            playerMove = 2                  #Paper
                    if fingers == [0, 1, 1, 0, 0]:
                            playerMove = 3                  #Scissor

                    randomNumber = random.randint(1,3)
                    imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

#   ====================================================================================================
#               Game Logic
#   ====================================================================================================

                    # Player Wins
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1

                    # AI Wins
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1

    imgBG[234:654, 795:1195] = imgScaled

    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (i49, 310))

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("BG", imgBG)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        stateResult = False
        initialTime = time.time()

#   ====================================================================================================
#   Resource folder required here onwards
#   Don't have the actual png files rn, will use something else and then replace it later
#   Files were originally extracted from the sc of Ritul's Figma file
#   ====================================================================================================


'''
import cv2
import numpy as np

def main_menu():
    # Load the logo
    logo = cv2.imread('your_logo.png')  # Replace 'your_logo.png' with the path to your PNG logo
    logo = cv2.resize(logo, (400, 200))  # Adjust the size as needed

    # Create a black background for the menu
    menu = np.zeros((400, 600, 3), dtype=np.uint8)

    # Add the logo to the menu
    menu[50:250, 100:500] = logo

    # Add buttons to the menu
    button_height = 50
    button_width = 200

    cv2.rectangle(menu, (200, 300), (400, 300 + button_height), (0, 255, 0), -1)  # Quick Play button
    cv2.rectangle(menu, (200, 400), (400, 400 + button_height), (0, 255, 0), -1)  # Tournament button
    cv2.rectangle(menu, (200, 500), (400, 500 + button_height), (0, 255, 0), -1)  # Exit button

    # Add button labels
    cv2.putText(menu, "Quick Play", (250, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(menu, "Tournament", (250, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(menu, "Exit", (250, 530), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('GestureRPS', menu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
main_menu()

'''

