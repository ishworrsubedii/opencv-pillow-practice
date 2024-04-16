"""
Created By: ishwor subedi
Date: 2024-04-16
"""

import cv2
import numpy as np
from numpy import ndarray


def show_image(image, title="image"):
    """
    Show image using cv2
    :param image: ndarray
    :return:
    """
    cv2.imshow(f'{title}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def read_image(path):
    """
    Read image using cv2
    :param path: path of the images
    :return: ndarray
    """
    image = cv2.imread(path)
    return image


def resize_image(image, width, height):
    """
    Resize image using cv2
    :param image: ndarray of image
    :param width: width of the image that need to be resized
    :param height: height of the image that need to be resized
    :return:
    """
    return cv2.resize(image, (width, height))


def scaling_images(image: ndarray, scale: float):
    """
    Scaling image using cv2
    :param image: ndarray of image
    :param scale: scale factor
    :return:
    """
    height = int(image.shape[0] * scale)
    width = int(image.shape[1] * scale)
    return cv2.resize(image, (width, height))


def read_video(video_path, rescale: bool = False, scale: float = 0.5):
    cap = cv2.VideoCapture(video_path)
    while True:
        istrue, frame = cap.read()
        if istrue:
            if rescale:
                frame = scaling_images(frame, scale)
            cv2.imshow('Video', frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()


if __name__ == '__main__':
    ## Image Reading
    image_path = 'images/ss.png'
    # image = read_image(image_path)
    # show_image(image, title="Original Image")
    # resized_image = resize_image(image, 300, 300)
    # show_image(resized_image, title="Resized Image")
    # scaled_image = scaling_images(image, 2.5)
    # show_image(scaled_image, title="Scaled Image")

    ## Video Reading
    video_path = "videos/stable_diffusion_try.mp4"

    # frame = read_video(video_path)
    rescaled_frame = read_video(video_path, rescale=True, scale=0.5)
