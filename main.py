import time
from methods import *
import cv2
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--cam_id', type=int, default=0)
parser.add_argument('--file', type=str, default=None, help="Optionally use a video file instead of a live camera")


args = parser.parse_args()


if args.file is not None:
    cap = cv2.VideoCapture(args.file)

else:
    cap = cv2.VideoCapture(args.cam_id)


while True:

    _,image = cap.read()

    marker = find_marker(image)
    print(marker)

    #print the output
    center = (int(marker[0][0]),int(marker[0][1]))
    cv2.putText(image, " object location in "  +str(center),
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2)

    cv2.circle(image, center, int(marker[1][0]), (0, 255, 255), 2)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    key = cv2.waitKey(1)
    #Press Esc to stop the program
    if key == 27:
        break


cv2.destroyAllWindows()
