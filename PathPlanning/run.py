from planning_framework import path
import cv2 as cv
import numpy as np 
import argparse
import matplotlib.pyplot as plt 

parser = argparse.ArgumentParser(description = "Path Planning Visualisation")

parser.add_argument("-n", "--n_heuristic", default = 2, help = "Heuristic for A* Algorithm (default = 2). 0 for Dijkstra\'s Algorithm")
args = parser.parse_args()
N_H = int(args.n_heuristic)



drawing = False # true if mouse is pressed
mode = 'obs' # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
sx, sy = 0, 0
dx, dy = 50, 50
# mouse callback function
def draw(event,x,y,flags,param):
    global mode, sx, sy, dx, dy, drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == 'obs':
                cv.rectangle(img,(x-5,y-5),(x+5,y+5),(255,255,255),-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'obs':
            cv.rectangle(img,(x-5,y-5),(x+5,y+5),(255,255,255),-1)
        elif mode == 'src':
            cv.circle(img, (x, y), 5, (255, 0, 0), -1)
            sx, sy = x, y
        elif mode == 'dst':
            cv.circle(img, (x, y), 5, (0, 255, 0), -1)
            dx, dy = x, y


img = np.zeros((512,512,3), np.uint8)
inv_im  = np.ones(img.shape)*255

cv.namedWindow('Draw the Occupancy Map')
cv.setMouseCallback('Draw the Occupancy Map',draw)
while(1):
    cv.imshow('Draw the Occupancy Map',inv_im - img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
mode = 'src'
img_ = img

cv.namedWindow('Set the Starting Point')
cv.setMouseCallback('Set the Starting Point',draw)
while(1):
    cv.imshow('Set the Starting Point',inv_im - img)
    if cv.waitKey(20) & 0xFF == 27:
        break
    # cv.waitKey(20)
cv.destroyAllWindows()
mode = 'dst'

end = 'Set the End Point'
cv.namedWindow(end)
cv.setMouseCallback(end,draw)
while cv.getWindowProperty(end, 0) >= 0:
    cv.imshow(end,inv_im - img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

img = cv.resize(img_, (50, 50), interpolation = cv.INTER_AREA)
inv_img = np.ones(img.shape)
np.savetxt("map.txt", np.array(img[:,:, 0]))
plt.imshow(inv_img - img)

start = (np.array([sx, sy])*50//512)
end   = (np.array([dx, dy])*50//512)

path(start, end, N_H)