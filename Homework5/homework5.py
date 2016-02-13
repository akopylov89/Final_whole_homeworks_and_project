import os
import Image
import sys
input_file_directory = sys.argv[1]
for d, dirs,pictures in os.walk(input_file_directory):
    for picture in pictures:
        full_path = d + os.path.sep + picture
        resized_name = 'resized_' + picture
        resized_path = os.path.join(d, resized_name)
        try:
            img = Image.open(full_path)
            width_size, hieght_size = img.size
            int_width_size = int(width_size)
            int_hieght_size = int(hieght_size)
            resized_width_size = int_width_size/ 2
            resized_height_size = int_hieght_size/2
            im = img.resize((resized_width_size, resized_height_size))
            im = img.save(resized_path)
        except:
            print("Picture {} can't be resized".format(picture))

#just print - python homework5.py "D:\\Python\\Homeworks_all\\Homework5\\pictures"
