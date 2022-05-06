from turtle import clear # enables users to create pictures and shapes by providing them with a virtual canvas
import numpy as np # use numerical operations
import matplotlib.pyplot as plt # use for data manipulation
import cv2 # use for image processsing & video processing

cap = cv2.VideoCapture(0) # video capturing

while True:
    _, image = cap.read()
    # covert to greyscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect edges
    edges = cv2.Canny(grayscale, 30, 100)
    #detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    # drwaining lines
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # show images
    cv2.imshow("image", image) 
    cv2.imshow("edges", edges)
    if cv2.waitKey(250) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()