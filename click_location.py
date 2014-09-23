from PIL import Image
from pylab import *

im = array(Image.open('img.jpg'))
show()
while(1):
    imshow(im)
    print "Please click 3 points"
    x = ginput(1)
    print 'you clicked:',x
