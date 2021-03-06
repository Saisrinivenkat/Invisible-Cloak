import cv2
import numpy as np

Cap = cv2.VideoCapture(0)

back = cv2.imread('./back.jpg')  # Here Upload The background as You want


while Cap.isOpened():

    ret, frame = Cap.read()

    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        red = np.uint8([[[255, 0, 0]]])
        hsv_blue = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        # Here I'm using the different hsv value as I've Cal by my Wish

        low_val_b = np.array([0,0,0]) # hue+10,100,100
        up_val_b = np.array([0, 0, 255]) #hue-10,255,255

        # Masking value which are blue
        mask = cv2.inRange(img, low_val_b, up_val_b)

        mask1 = cv2.dilate(mask, np.ones(
            (9, 9), np.uint8), iterations=1)

        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones(
            (5, 5), np.uint8),  iterations=2)

        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, np.ones(
            (5, 5), np.uint8), iterations=1)

        section1 = cv2.bitwise_and(back, back, mask=mask1)

        mask2 = cv2.bitwise_not(mask1)  # Masking the value other than Blue

        section2 = cv2.bitwise_and(frame, frame, mask=mask2)

        # Getting the final Image
        Final = cv2.addWeighted(section1, 1, section2, 1, 0)

        cv2.imshow("Cloak", Final)

    if cv2.waitKey(3) == ord('q'):
        break

Cap.release()
cv2.destroyAllWindows()
