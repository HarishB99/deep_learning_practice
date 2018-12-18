import os
from PIL import Image
import array
import numpy as np

def convert(filename):
    try:
        with open(filename, 'rb') as f:
            size = os.path.getsize(filename)
            width = 1024
            rem = size % width
            byte_arr = array.array('B')
            byte_arr.fromfile(f, size - rem)
            byte_arr = np.asarray(byte_arr)
            np_arr = np.reshape(byte_arr, (len(byte_arr)//width, width))
            np_arr = np.uint8(np_arr)
            return np_arr
    except EnvironmentError as error:
        print('Error in convert_bytes_to_image.convert(): ', error.strerror)

