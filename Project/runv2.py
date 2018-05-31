import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from skimage.segmentation import slic
import skimage.io
from skimage.util import img_as_float
import cv2

img = skimage.io.imread('./wallpaper-2.jpg')

img_rgb = img_as_float(img)

segments_slic = slic(img_rgb, n_segments=250, compactness=10, sigma=1, enforce_connectivity=False)
cv2.imshow("BGR", img_rgb)
cv2.waitKey(2)