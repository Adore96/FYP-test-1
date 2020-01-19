import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

datadir = "path to directory x:something"
catagories = ["Dog","Cat"] #path from datadir to iterate thru all the images

for catagory in catagories:
    path = os.path.join(datadir,catagories) #paths to cats and dogs dir should be the same name as the foldername
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE) #to convert the image to greyscale
        img_array = cv2.imread(os.path.join(path, img)) #to take the color image comes as blue green red in cv2
        # print(img_array) prints the pixel values of the image
        # print(img_array.shape) prints the matrix size which should be equal in all images
        plt.imshow(img_array,cmap="gray")
        plt.show()
        break
    break

img_size = 50

new_array =  cv2.resize(img_array,(img_size,img_size)) #length*width of the resized image
plt.imshow(new_array,cmap='gray') #showing the image in the grayscale
plt.show()

TrainingData = []

def createTrainingData():
    for catagory in catagories:
        path = os.path.join(datadir, catagories)
        ClassNum = catagories.index(catagory) #taking the image labels as 0 and 1 according to the array index

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array =  cv2.resize(img_array,(img_size,img_size))
                TrainingData.append([new_array,ClassNum])
            except Exception as e:
                pass

createTrainingData()
print(len(TrainingData))


