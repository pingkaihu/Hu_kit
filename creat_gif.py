import sys
import cv2
import glob
import imageio

# Turn wildcard into array, ex: *.png -> [1.png, 2.png, 3.png]
image_list = glob.glob(sys.argv[1])
print(image_list)
frames = []
for i in range(len(image_list)):
    img = imageio.v3.imread(image_list[i])
    frames.append(img)
imageio.mimsave('./NEW.gif', frames, duration=3.0)
