# # Python program to explain os.path.join() method

# # importing os module
# import os

# # Path
# path = "/home"

# # Join various path components
# print(os.path.join(path, "User/Desktop", "file.txt"))


# # Path
# path = "User/Documents"

# # Join various path components
# print(os.path.join(path, "/home", "file.txt"))

# # In above example '/home'
# # represents an absolute path
# # so all previous components i.e User / Documents
# # are thrown away and joining continues
# # from the absolute path component i.e / home.


# # Path
# path = "/User"

# # Join various path components
# print(os.path.join(path, "Downloads", "file.txt", "/home"))

# # In above example '/User' and '/home'
# # both represents an absolute path
# # but '/home' is the last value
# # so all previous components before '/home'
# # will be discarded and joining will
# # continue from '/home'

# # Path
# path = "/home"

# # Join various path components
# print(os.path.join(path, "User/Public/", "Documents", ""))

# # In above example the last
# # path component is empty
# # so a directory seperator ('/')
# # will be put at the end
# # along with the concatenated value
# datadir = 'hello1', 'hello2', 'hello3'
# path = "imgcls/.idea/PetImages/"
# for datas in datadir:
#     hello = os.path.join(path, datadir)
#     print(hello)

import os
# rootdir = 'FYP-test-1\imgcls\.idea\PetImages'


# for subdir, dirs, files in os.walk(rootdir):
#     for file in dirs:
#         classnum = dirs.index(file)
#         newcls= str(classnum)
#         print(type(newcls))
#         print(newcls)


# b = [10, 20, 30]

# total = 0

# for ev in b:
#     total = total + ev
#     print(total)

# variable
# print(type(variable))

import cv2
import matplotlib.pyplot as plt

datadir = "imgcls/.idea/PetImages"
catagory = ["Dog", "Cat"]


img_array = 0

for subdir, dirs, files in os.walk(datadir):
    for file in files:
        print(file)
    # for img in os.listdir(path):
    #     img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
    #     img_array = cv2.imread(os.path.join(path, img))
    #     plt.imshow(img_array, cmap="gray")
    #     plt.show()


img_size = 50

# new_array = cv2.resize(img_array, (img_size, img_size))
# plt.imshow(new_array, cmap='gray')
# plt.show()
