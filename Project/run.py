import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

import cv2

image = cv2.imread('./100X100_2.jpg')

def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

#Kører pixels^2 gange = 81_000 milliarder (3_000^4)(N^2 N= pixels) gange ved et billede der er 3000*3000 pixels (9_000_000 pixels).
#Så kører O gange det samme som i dokumentet, for algoritme 1/2 (Der er den samme)
def calculate_Dist(image):
    shape_of_image = image.shape #= (x,y,3) (fordi rgb er 3 farver blandet).
    temp_image = np.zeros((shape_of_image[0], shape_of_image[1]))
    for x in range(shape_of_image[0]): #Samme som den første akse
        for y in range(shape_of_image[1]): #Samme som den anden akse

            sik = 0
            for xx in range(shape_of_image[0]):
                for yy in range(shape_of_image[1]):
                    if(x==xx and y==yy):
                        None
                    else:
                        sik += dist(image[x,y], image[xx,yy])

            temp_image[x,y] = sik

    return temp_image

def calculate_Dist2(image): #Effektivt gør det samme som calculate_Dist . bare med en list comprehension
    shape_of_image = image.shape #= (x,y,3) (fordi rgb er 3 farver blandet).
    temp_image = np.zeros((shape_of_image[0], shape_of_image[1]))
    temp_pixels = [dist(image[x,y], image[xx,yy]) for x in range(shape_of_image[0]) for y in range(shape_of_image[1]) for xx in range(shape_of_image[0]) for yy in range(shape_of_image[1]) if(x!=xx or y!=yy)]
    #LISTE UDEN SUMMERING.
    pixels = shape_of_image[0] * shape_of_image[1]
    for i in range(pixels):
        summed = np.sum(temp_pixels[i*(pixels-1):(i*(pixels-1))+(pixels-1)])
        temp_image[i//shape_of_image[1],i%shape_of_image[1]] = summed

    return temp_image

#image = [[[100,100,100]
#        ]]
#calculate_Dist(image)
#print(image.shape)
calc2 = calculate_Dist2(image)
calc = calculate_Dist(image)
print(f'(calc2: {calc2}; calc: {calc})')
print(calc2==calc)
