import numpy as np
import matplotlib.pyplot as plt
import os
import cv2


datadir ="imgcls/.idea/PetImages"
catagory = ["Dog","Cat"] #path from datadir to iterate thru all the images


img_array = 0

for subdir, dirs, files in os.walk(datadir):
    for file in files:
       path = os.path.join(subdir, file) #paths to cats and dogs dir should be the same name as the foldername
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE) #to convert the image to greyscale
        img_array = cv2.imread(os.path.join(path, img)) #to take the color image comes as blue green red in cv2
        # print(img_array) prints the pixel values of the image
        # print(img_array.shape) prints the matrix size which should be equal in all images
        plt.imshow(img_array,cmap="gray")
        plt.show()


#ERROR - only the images in black are showing so the images have to be selected problem is in the OS library i think.


img_size = 50

new_array =  cv2.resize(img_array,(img_size,img_size)) #length*width of the resized image
plt.imshow(new_array,cmap='gray') #showing the image in the grayscale
plt.show()

TrainingData = []

def createTrainingData():
    for subdir, dirs, files in os.walk(datadir):
        for file in dirs:
            ClassNum = dirs.index(file)

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array =  cv2.resize(img_array,(img_size,img_size))
                TrainingData.append([new_array,ClassNum])
            except Exception as e:
                pass




createTrainingData()
#print(len(TrainingData))

# first thing we did was iterating over catagories so everyhing at first is dogs and then cats so need
# to shuffle to mix them up so the accuracy is kinda low in that way

import random

random.shuffle(TrainingData)
for sample in TrainingData[:10]:
    print(sample[1])  #checking the shuffling is correct

X = [] #assigning them to variables before sending it to the NN -> feature set
y= [] #->label set

for features, labels in TrainingData:
    X.append(features)
    y.append(labels)

#we cannt pass list to the neural networks x has to be converted to array and also should be reshaped

X = np.array(X).reshape(-1,img_size,img_size,1) #1 here stands for the greyscale if this is color number = 3

# to save the things weve done so far picle is used otherwise we have to do he same process again and again

import pickle
# https://docs.python.org/3/library/pickle.html

pickle_out = open("X.pickle","wb") #writein backend
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb") #writein backend
pickle.dump(y,pickle_out)
pickle_out.close()

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)
  #this will give output as array


