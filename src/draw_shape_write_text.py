"""
Created By: ishwor subedi
Date: 2024-04-16
"""

import cv2
import numpy as np
from numpy import ndarray
from reading_images_video import show_image


def put_text(image, text: str, position: tuple, color=(0, 255, 0)):
    """
    Put text on the image using cv2
    :param image: image ndarray
    :param text: text that we wanted to put on the image
    :param position: position of the text on the image
    :param color: color of the text RGB
    :return: image array with text included
    """
    cv2.putText(image, text=text, org=position, fontFace=cv2.FONT_HERSHEY_COMPLEX, color=color, fontScale=2)
    return image


def draw_rectangle(text: str = "Rectangle", position: tuple = (10, 200), color=(255, 255, 255),
                   enable_text: bool = False):
    """
    Draw shapes using cv2
    :return: ndarray of image
    """
    image = np.zeros((500, 500, 3), dtype='uint8')
    image[:] = 0, 0, 0
    cv2.rectangle(image, (200, 100), (250, 250), color=(255, 255, 0))
    if enable_text:
        image = put_text(image, text=text, position=position, color=color)
    return image


def draw_circle(enable_text: bool = False):
    """
    Draw circle using cv2
    :return: ndarray of image
    """
    image = np.zeros((500, 500, 3), dtype='uint8')
    image[:] = 0, 0, 0
    put_text(image, text="Circle", position=(10, 200), color=(255, 255, 255))
    cv2.circle(image, (250, 250), 50, (255, 255, 0))
    return image


def draw_line():
    """
    Draw line using cv2
    :return: ndarray of image
    """
    image = np.zeros((500, 500, 3), dtype='uint8')
    image[:] = 0, 0, 0
    cv2.line(image, (100, 100), (200, 200), (255, 255, 0), 3)
    return image


if __name__ == '__main__':
    ## Draw Rectangle
    # shape = draw_rectangle()
    # show_image(image=shape, title="Draw Shapes")
    # shape = draw_rectangle(enable_text=True)
    # show_image(image=shape, title="Draw Shapes with Text")
    ## Draw Circle
    # image = draw_circle()
    # show_image(image=image, title="Draw Circle")

    ## Draw Line
    image = draw_line()
    show_image(image=image, title="Draw Line")
