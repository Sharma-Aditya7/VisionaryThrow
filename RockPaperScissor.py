import cv2
import cvzone


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#   ====================================================================================================
#   The parameters will have to be re-tuned when overlaying on the final bg
#   ====================================================================================================


while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img,(0,0),None,0.875,0.875)      #Using it to resize the image on a scale

    cv2.imshow("Image",img)
    cv2.imshow("BG", imgBG)
    cv2.imshow("Scaled", imgScaled)

    cv2.waitKey(1)

#   ====================================================================================================
#   Resource folder required here onwards
#   Don't have the actual png files rn, will use something else and then replace it later
#   Files were originally extracted from the sc of Ritul's Figma file
#   ====================================================================================================

