#Import Libraries 
import cv2
import numpy as np
import time, argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--video', help = 'input video path')
args = parser.parse_args()

# Callback video is there is one; or if there isn't a video then bring the webcam data
cap = cv2.VideoCapture(args.video if args.video else 0)

# Wait 3 seconds for the webcam to turn on 
time.sleep(3)

# Grap background image from first part of the video 
# Background should not contain anyone(human)/ moving object / or the color scheme that is removed ex) red 
# For the first 50 frames per second, it saves the background 
for i in range(60):
  ret, background = cap.read()
  
# Save videos in directory of file
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('#video path/output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (background.shape[1], background.shape[0]))
out2 = cv2.VideoWriter('#video path/'output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (background.shape[1], background.shape[0])) 

# Read each frame from video or webcam
while(cap, isOpened()):
ret, img = cap.read()
if not ret:
break

# Convert the color spae from BGR to HSV
# HSV is used as this color scheme is closer to human skin color
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                       

# Generate mask to detect red color 
# Upper and lower values of the hsv value of red are separated so they are combined together                       
# Red values of mask 1 [0 ~ 10], [120 ~ 255], [70 ~ 255] mask 2 [170 ~ 180], [120 ~ 255], [70 ~ 255]
# Color values mask 1 [H], [S], [V] mask 2 [H], [S], [V]
                       
lower_red = np.array([0, 120, 70])                       
upper_red = np.array([10, 255, 255])                       
mask1 = cv2.inRange(hsv, lower_red, upper_red)  

lower_red = np.array([170, 120, 70])                       
upper_red = np.array([180, 255, 255])                       
mask2 = cv2.inRange(hsv, lower_red, upper_red) 

mask1 = mask1 + mask2

# black color scheme for black instead of red
# lower_black = np.array([0, 0, 0])                       
# upper_black = np.array([255, 255, 80])                       
# mask1 = cv2.inRange(hsv, lower_black, upper_black)
                       

# Refining the mask corresponding to the detected red color
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
                       
# Remove noise

mask_cloak = cv2.morphologyEx(mask1, op=cv2.MORPH_OPEN, kernel=np.ones(3,3), np.uint8), iterations=2)                       
mask_cloak = cv2.dilate(mask_cloak, kernel=np.ones((3,3), np.unit8), iterations=1)
mask_bg = cv2.bitwise_not(mask_cloak)

cv2.imshow('mask_cloak', mask_cloak)

# Generate the final output 
# bitwise and() is used as values with matrix that aren't 0 will be passed; in other words, only the mask area remains
res1 = cv2.bitwise_and(background, background, mask=mask_cloak)
res2 = cv2.bitwise_and(img, img, mask=mask_bg)
result = cv2.addWeighted(src1=res1, alpha=1, src2=res2, beta =1, gamma=0)

cv2.imshow('res1', res1)

# cv2.imshow('ori', img)
cv2.imshow('result', result)
out.write(result)
out2.write(img)

if cv2.waitKey(1) == ord('q'):
break

out.release()
out2.release()
cap.release()


                       
                       
                       
                      

                       


