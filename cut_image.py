import sys
import cv2
import glob

# Turn wildcard into array, ex: *.png -> [1.png, 2.png, 3.png]
image_list = glob.glob(sys.argv[1])
print(image_list)

# Define upper left point and image size
x = 0
y = 0
w = 400
h = 400

# Crop images and save cropped images
for i in range(len(image_list)):
    img = cv2.imread(image_list[i])
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite("cropped_"+image_list[i], crop_img)
