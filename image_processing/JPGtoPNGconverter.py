import sys
import os
from PIL import Image


# Grab the first and second argument with sys

# Check if new exists and if not, create it with os

# Look through the folder and convert all images into pngs, saved to the new folder. 

existing_folder = sys.argv[1]
target_folder = sys.argv[2]

path = f'./{target_folder}'

if os.path.exists(path) == False:
  os.makedirs(path)

directory = existing_folder

for image in os.scandir(directory):
  img = Image.open(image.path)
  img.save(f'{path}/{image.name[:-4]}.png')
