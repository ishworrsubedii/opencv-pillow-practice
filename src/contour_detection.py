"""
Created By: ishwor subedi
Date: 2024-04-16
"""

import cv2
import numpy as np
from reading_images_video import show_image, read_image, resize_image
from essential_functions import convert_to_gray, blur_image, edge_detection, dilate_image


def contour_detection(image):
    """
    Contours are basically the boundaries of objects—the line or curve that joins the continuous point along the boundary of an object.
    From a mathematical point of view, contours and edges are two different things. Contours are useful tools when you get into shape analysis and object detection, recognition, and shape analysis.
    :param image: ndarray of the images
    :return: array of detected contour
    """

    w, h = image.shape
    blank = np.zeros(shape=(w, h))
    contours, hirarchy = cv2.findContours(image, cv2.RETR_LIST,
                                          cv2.CHAIN_APPROX_SIMPLE)  # hierarchy is the relationship between contours like if we have rectangle inside the circle then the hierarchy will be like that
    print(f"Number of contours found: {len(contours)}")

    contours = cv2.drawContours(blank, contours, -1, (255, 255, 255), 2)
    return contours


if __name__ == '__main__':
    image_path = "images/sample_img.jpg"
    image = read_image(image_path)
    resize = resize_image(image, 800, 500)
    blur_image = blur_image(resize)
    gray_image = convert_to_gray(blur_image)
    edge_det = edge_detection(gray_image)

    contour = contour_detection(edge_det)
    show_image(title="Original image", image=image)
    show_image(title="resized image", image=resize)
    show_image(title="blur image", image=blur_image)
    show_image(title="gray scale", image=gray_image)
    show_image(title="edge detection", image=edge_det)
    show_image(title="Contour detection", image=contour)
