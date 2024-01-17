import sys
import os
from PIL import Image

# 1. grab arguments from cmd 
arguments = sys.argv
input_folder = arguments[1]
new_folder = arguments[2]

# 2. check if new folder exists, if not create new folder
current_directory_str = os.getcwd()
new_directory_str = os.path.join(current_directory_str, new_folder)
input_directory_str = os.path.join(current_directory_str, input_folder)

if not os.path.exists(new_directory_str):
   os.makedirs(new_directory_str)

# 3. loop through input folder
input_directory = os.fsdecode(input_directory_str)

for file in os.listdir(input_directory):
    img = Image.open(f"./{input_folder}{file}")
    img_name = file[:file.index('.')]
    # 4. convert jpg to png
    # 5. save converted images to new folder 
    img.save(f'{new_directory_str}/{img_name}.png', 'png')    
    