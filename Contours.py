from PIL import Image
from pylab import *

#read image into an array
im = array(Image.open('s9.jpg').convert('L'))

#create a new figure
figure()

#don't use colors
gray()

#show contours
contour(im,origin = 'image')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
show()
