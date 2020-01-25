import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Dropout , Activation,Flatten,Conv2D,MaxPooling2D
import pickle

X = pickle.load(open("X.pickle","rb"))
y = pickle.load(open("y.pickle","rb"))

X = X/255 #normalizinf the data devidong by the maximum value

model = Sequential() #simple sequentiol model

# Layer one starts
model.add(Conv2D(64,(3,3), input_shape = X.shape[1:])) #convolution layer 3,3 is the window size
# and then the other is input shape
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=[2,2]))

# layer 2 starts
model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=[2,2]))

# layer 3 starts
model.add(Flatten()) #flattning the laters
model.add(Dense(64))

# output layer
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss = "binary_crossentropy",
              optimizer = "adam",
              metrics = ['accuracy'])

model.fit(X,y,batch_size=32,validation_split =0.1)