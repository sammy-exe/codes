# from matplotlib import pyplot as plt
# import matplotlib.image as mpimg

# img = mpimg.imread('/media/sammy/PART1/random photu/Screenshot from 2022-07-25 10-54-18.jpg')
# R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
# img = 0.2989 * R + 0.5870 * G + 0.1140 * B
# plt.imshow (img, cmap='gray')
# plt.show()

from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

img1 = np.array(Image.open('/media/sammy/PART1/random photu/geeks'))
figure, plots = plt.subplots(ncols=3, nrows=1)
for i, subplot in zip(range(3), plots):
    temp = np.zeros(img1.shape, dtype='uint8')
    temp = img1[:,:,i]
    subplot.imshow(temp)
    subplot.set_axis_off()
plt.show()