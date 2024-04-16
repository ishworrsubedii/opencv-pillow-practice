"""
Created By: ishwor subedi
Date: 2024-04-16
"""
import cv2
import numpy as np
from reading_images_video import show_image, read_image


# Converting the image to grayscale
def convert_to_gray(image):
    """
    Convert the image to grayscale
    :param image: ndarray of image
    :return: ndarray of grayscale image
    """
    image = cv2.cvtColor(image,
                         cv2.COLOR_BGR2GRAY)  # We can also use other color conversion methods like cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, etc.
    return image


## Blur the image
def blur_image(image):
    """
    Blur the image using GaussianBlur
    :param image: ndarray of image
    :return: ndarray of blurred image
    """
    image = cv2.GaussianBlur(src=image, ksize=(11, 11),
                             sigmaX=0)  # ksize is the kernal size of the filter, sigmaX is the standard deviation in X direction
    return image


## Edge Detection
def edge_detection(image, threshold1=100, threshold2=200):
    """
    Detect the edge of the image using Canny edge detection

    :param image: ndarray of image
    :return: ndarray of edge detected image
    """
    image = cv2.Canny(image, threshold1, threshold2)
    # image = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

    return image


def dilate_image(image, iterations=5):
    """
    Dilate the image using cv2.dilate
    :param image: ndarray of image of canny edge detected image
    :param iterations: number of iterations
    :return: ndarray of dilated image
    """
    image = cv2.dilate(image, iterations=iterations, kernel=np.ones((5, 5), np.uint8))
    return image


if __name__ == '__main__':
    ## Grayscale image

    image_path = "images/ss.png"
    # image = read_image(image_path)
    # gray_image = convert_to_gray(image)
    # show_image(image, "Original Image")
    # show_image(gray_image, "Gray Image")

    ## Blur Images
    # image = read_image(image_path)
    # blur = blur_image(image)
    # show_image(image, "Original Image")
    # show_image(blur, "Blurred Image")

    ## Edge Detection
    # image = read_image(image_path)
    # gray_image = convert_to_gray(image)
    # edge = edge_detection(gray_image)
    # show_image(image, "Original Image")
    # show_image(gray_image, "Gray Image")
    # show_image(edge, "Edge Detected Image")

    ## Dilation of the image
    # image = read_image(image_path)
    # gray_image = convert_to_gray(image)
    # edge = edge_detection(gray_image)
    # blur = blur_image(edge)
    # dilated_image = dilate_image(blur)
    # show_image(image, "Original Image")
    # show_image(gray_image, "Gray Image")
    # show_image(blur, "Edge Detected Image")
    # show_image(dilated_image, "Dilated Image")
