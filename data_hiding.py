#! python3

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def histogram_8bit(image):
    num_of_bins = 256
    intensities_array = np.zeros(num_of_bins)
    img_hei = image.shape[0]
    img_wid = image.shape[1]
    
    for i in range(img_hei):
        for j in range(img_wid):
            pixel = image[i][j] 
            intensities_array[pixel] += 1
            
    x = np.arange(num_of_bins)

    return x, intensities_array
    
    # plt.figure(figsize=(15,5))
    # plt.bar(x, intensities_array)
    # plt.xticks(x)
    # plt.title(f"Histogram of {img_wid}x{img_hei}px")
    # plt.show()
    
def hide_data(cover_image, bit_stream):
    """ Method to hide a bit stream in a 8-bit grayscale image """
    
    # 8-bit image verification
    if cover_image.dtype != "uint8":
        return -1
    
    bins, intensities = histogram_8bit(cover_image)
    peak_point = np.argmax(intensities)
    print("Maximum number of bits for the given image is " + str(intensities[peak_point])) 
    
    # Data stream size verification
    size = len(bit_stream)
    if size > intensities[peak_point]:
        print("Bit stream is too long for this image")
        return -1
        
    # Shifts right histogram values larger than peak_point by 1
    img_hei = cover_image.shape[0]
    img_wid = cover_image.shape[1]
    for i in range(img_hei):
        for j in range(img_wid):
            pixel = cover_image[i][j]
            if pixel > peak_point and pixel < len(bins)-1:
                cover_image[i][j] += 1

    # Hide information
    bit_count = 0
    for i in range(img_hei):
        for j in range(img_wid):
            #print(bit_count)
            if bit_count < size:
                if cover_image[i][j] == peak_point:
                    if bit_stream[bit_count] == '1':
                        cover_image[i][j] += 1
                    bit_count += 1
            else:
                break
    return cover_image, peak_point, 
               
def reveal_data(cover_image, peak_point, size):
    """ Method to reveal a bit stream in a 8-bit grayscale image """
    
    # 8-bit image verification
    if cover_image.dtype != "uint8":
        return -1    
    bins, intensities = histogram_8bit(cover_image)
    img_hei = cover_image.shape[0]
    img_wid = cover_image.shape[1]
    
    # Get bit stream from image
    bit_count = 0
    bit_stream = []
    for i in range(img_hei):
        for j in range(img_wid):
            if bit_count < size:                
                pixel = cover_image[i][j]
                if pixel == peak_point:
                    bit_stream.append('0')
                    bit_count += 1
                elif pixel == peak_point + 1:
                    bit_stream.append('1')
                    bit_count += 1
            else:
                break
    
    return bit_stream
  
    # def string_to_binary(string):
        # binary_stream = ''.join(format(ord(x), 'b') for x in string)
        # return binary_stream
        
    # def binary_to_string(bit_stream):
        # index = 0
        # while(index < len(bit_stream)):
            # binary_to_int = int(bit_stream[index:index+8],2)
            # int_to_char = str(binary_to_int)
            # index += 8
            
        
    
    
img = cv.imread('boat.png', cv.IMREAD_GRAYSCALE)
cv.imshow('image', img)
cv.waitKey(0)
bit_stream = ['1','0','0','1','1','0','1','0','1','0','0','1','1','0','1','0','1','0','0','1','1','0','1','0']
print("Original bit stream: ")
print(bit_stream)
steg_img, peak_point = hide_data(img, bit_stream)
print(peak_point)
cv.imshow('steg_image', steg_img)
cv.waitKey(0)
bit_stream_return = reveal_data(steg_img, peak_point, len(bit_stream))
print("Original bit stream: ")
print(bit_stream_return)
    
    
    
    
    
    
    
    
    
    
    
    
    