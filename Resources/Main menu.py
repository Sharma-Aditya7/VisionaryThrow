import cv2
import numpy as np

def main_menu():
    # Load the logo
    #logo = cv2.imread("Resources/1.png")  # Replace 'your_logo.png' with the path to your PNG logo
    #logo = cv2.resize(logo, (400, 200))  # Adjust the size as needed

    # Create a black background for the menu
    menu = np.zeros((400, 600, 3), dtype=np.uint8)

    # Add the logo to the menu
    #menu[50:250, 100:500] = logo

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
