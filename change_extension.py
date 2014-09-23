#Convert filetype

from PIL import Image
import os


def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('jpg')]

path = raw_input("Enter path to directory")
filelist = get_imlist(path)
ext = raw_input("Enter the extension:")
for infile in filelist:
    outfile = os.path.splitext(infile)[0] + "."+ext
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot convert", infile

