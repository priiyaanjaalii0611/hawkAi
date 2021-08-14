import cv2 as cv
import numpy as np


contour_f=np.array(0)
cam = cv.VideoCapture(0)
address="http://192.168.29.145:8080/video"
cam.open(address)

cv.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv.imshow("test", frame)

    k = cv.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1




cv.destroyAllWindows()

cv.imshow("your image",frame)

cv.waitKey(0)
orig = frame
cv.imwrite("output.png",orig)
def get_new(old):
    new = np.ones(old.shape, np.uint8)
    cv.bitwise_not(new,new)
    return new


    

# these constants are carefully picked
MORPH = 9
CANNY = 84
HOUGH = 25

img = cv.cvtColor(orig, cv.COLOR_BGR2GRAY)
cv.GaussianBlur(img, (3,3), 0, img)


# this is to recognize white on white
kernel = cv.getStructuringElement(cv.MORPH_RECT,(MORPH,MORPH))
dilated = cv.dilate(img, kernel)

edges = cv.Canny(dilated, 0, CANNY, apertureSize=3)

lines = cv.HoughLinesP(edges, 1,  3.14/180, HOUGH)
for line in lines[0]:
        cv.line(edges, (line[0], line[1]), (line[2], line[3]),
                        (255,0,0), 2, 8)

# finding contours
contours = cv.findContours(edges.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_TC89_KCOS)[0]

contours = filter(lambda cont: cv.arcLength(cont, False) > 100, contours)
contours = filter(lambda cont: cv.contourArea(cont) > 100, contours)
contour_f=contours



# simplify contours down to polygons
rects = []
for cont in contours:
    rect = cv.approxPolyDP(cont, 40, True).copy().reshape(-1, 2)
    rects.append(rect)
    

# that's basically it
cv.drawContours(orig, rects,-1,(0,0,255),3)




# show only contours
new = get_new(img)
cv.drawContours(new, rects,-1,(0,255,0),1)
cv.GaussianBlur(new, (9,9), 0, new)
new = cv.Canny(new, 0, CANNY, apertureSize=3)

cv.namedWindow('result', cv.WINDOW_NORMAL)
cv.imshow('result', orig)
cv.waitKey(0)
# cv.imshow('result', dilated)
# cv.waitKey(0)
# cv.imshow('result', edges)
# cv.waitKey(0)
# cv.imshow('result', new)
# cv.waitKey(0)
            




