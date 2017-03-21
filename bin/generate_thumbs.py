#!/usr/bin/env python
import os
import glob

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

img_path = os.path.abspath('../assets/themes/img/example')
dest_path = os.path.abspath('../assets/themes/thumbnails')
if not os.path.exists(dest_path):
    os.makedirs(dest_path)
files = glob.glob(img_path+'/*')

for f in files:
    filename, ext = os.path.splitext(os.path.basename(f))
    dest_file = os.path.join(dest_path, filename + '-thumbnail' + ext)
    command = 'convert {} -resize 250x {}'.format(f, dest_file)
    os.system(command)
