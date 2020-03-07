import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Dropout , Activation,Flatten,Conv2D,MaxPooling2D
import pickle

from tensorflow.keras.callbacks import TensorBoard

# TensorBoard provides the visualization and tooling needed for machine learning experimentation
gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction = 0.33) #this shows how much memory should be allocated to each of thr model to run
# The name tf.GPUOptions is deprecated. Please use tf.compat.v1.GPUOptions instead.
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options)) #this can be used to run many models at the same time.
# The name tf.Session is deprecated. Please use tf.compat.v1.Session instead,The name tf.ConfigProto is deprecated. Please use tf.compat.v1.ConfigProto instead.

X = pickle.load(open("X.pickle","rb"))
y = pickle.load(open("y.pickle","rb"))

X = X/255.0    #normalizinf the data deviding by the maximum value.

model = Sequential() #simple sequentiol model

#without an activation function it becomes an linear activation function which is useless

# Layer one starts
model.add(Conv2D(64,(3,3), input_shape = X.shape[1:])) #convolution layer 3,3 is the window size.
# and then the other is input shape
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=[2,2]))

# layer 2 starts
model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=[2,2]))

# layer 3 starts
model.add(Flatten()) #flattning the layers
model.add(Dense(64))
model.add(Activation("relu"))

# output layer
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss = "binary_crossentropy",
              optimizer = "adam",
              metrics = ['accuracy'])

model.fit(X,y,batch_size=32,epochs = 3 ,validation_split =0.1,use_multiprocessing = True,shuffle = True)
# batch size means how any data you wanna pass at one time.