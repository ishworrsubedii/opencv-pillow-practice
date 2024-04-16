"""
Created By: ishwor subedi
Date: 2024-04-16
"""
import cv2
import numpy as np

from reading_images_video import read_image, resize_image, show_image
from color_spaces import ColorSpaceChange


# How to split and merge color channels of an image using OpenCV in Python?

def color_split_from_color_bgr(image):
    b, g, r = cv2.split(image)
    return b, g, r


def color_split_from_color_hsv(image):
    h, s, v = cv2.split(image)
    return h, s, v


def merge_color_channels(x, y, z):
    merged_image = cv2.merge((x, y, z))
    return merged_image


if __name__ == '__main__':
    image_path = "images/sample_img.jpg"
    image = read_image(image_path)
    image = resize_image(image, 800, 500)

    ## Splitting color channels from BGR image
    b, g, r = color_split_from_color_bgr(image)
    show_image(b, title="Blue Channel")
    show_image(g, title="Green Channel")
    show_image(r, title="Red Channel")

    ## Splitting color channels from HSV image
    # color_space = ColorSpaceChange(image)
    # hsv_image = color_space.bgr_to_hsv()
    # h, s, v = color_split_from_color_hsv(hsv_image)
    # show_image(h, title="Hue Channel")
    # show_image(s, title="Saturation Channel")
    # show_image(v, title="Value Channel")

    ## Merging color channels
    # merged_image = merge_color_channels(h, s, v)
    # show_image(merged_image, title="Merged Image")

    ## Merging color in blank image
    blank_image = np.zeros(image.shape[:2], dtype='uint8')
    blue_merge = merge_color_channels(b, blank_image, blank_image)
    green_merge = merge_color_channels(blank_image, g, blank_image)
    red_merge = merge_color_channels(blank_image, blank_image, r)

    show_image(blue_merge, title="Blue Channel Merge")
    show_image(green_merge, title="Green Channel Merge")
    show_image(red_merge, title="Red Channel Merge")
