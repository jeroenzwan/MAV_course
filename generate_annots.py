import os
import glob
import cv2
import numpy as np
import pandas as pd

folder_name = 'WashingtonOBRace/'
img_names = 'WashingtonOBRace/img_*.png'
filenames = []

for filename in glob.glob(img_names):
    filenames.append(filename)
filenames = sorted(filenames)

corners_annots = pd.read_csv(folder_name+'corners.csv', header=None, names=['img_name','y_c1','x_c1','y_c2','x_c2','y_c3','x_c3','y_c4','x_c4'])

for filename in filenames:
    img = cv2.imread(filename)
    cv2.imwrite(os.path.splitext(filename)[0] + '.jpg',img)
    corners = np.array(corners_annots[(folder_name+corners_annots[('img_name')])==filename])[:,1:]
    print(corners)
    width, height, _ = img.shape
    f = open(os.path.splitext(filename)[0] + '.txt', "w+")
    print(os.path.splitext(filename)[0] + '.txt', "w+")

    for j in range(4):
        x = corners[0,(2*j)]/width
        y = corners[0,(2*j+1)]/height
        w = 40/width
        h = 40/height
        message = f"{j} {x} {y} {w} {h}\n"
        f.write(message)