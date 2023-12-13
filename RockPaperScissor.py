import cv2
import mediapipe
import cvzone


cap = cv2.VideoCapture(0)


while True:
    imgBG = cv2.imread("Resources/BG.png")

    success, img = cap.read()
    cv2.imshow("Image",img)
    cv2.imshow("BG", imgBG)

    cv2.waitKey(1)

#   ====================================================================================================
#   Resource folder required here onwards
#   Don't have the actual png files rn, will use something else and then replace it later
#   Files were originally extracted from the sc of Ritul's Figma file
#   ====================================================================================================

