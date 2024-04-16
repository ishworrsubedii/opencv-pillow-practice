"""
Created By: ishwor subedi
Date: 2024-04-16
"""
import cv2
import numpy as np
from reading_images_video import show_image, read_image, resize_image
from draw_shape_write_text import put_text


## Translation
def image_translation(image, x, y):
    """
    This function is for translating the image from x and y coordinates.
    :param image:
    :param x:
    :param y:
    :return:

    -x=-->left
    -y=-->up
    +x=-->right
    +y=-->down

    """
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    w, h, _ = image.shape
    translated_image = cv2.warpAffine((image), translation_matrix, (w, h))
    return translated_image


## Rotation
def image_rotation(image, angle, roatation_point=None):
    """
    This function is for rotating the image
    :param image: ndarray of image
    :param angle: angle of rotation
    :return: rotated image
    """
    w, h, _ = image.shape
    if roatation_point is None:
        roatation_point = (w // 2, h // 2)  # it will define the center point of image and then rotate the image
    rotation_matrix = cv2.getRotationMatrix2D(roatation_point, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image


## Clipping
def image_clipping(image, start_x, start_y, end_x, end_y):
    """
    This function is for clipping the image
    :param image: ndarray of image
    :param start_x: starting x coordinate
    :param start_y: starting y coordinate
    :param end_x: ending x coordinate
    :param end_y: ending y coordinate
    :return: clipped image
    """
    clipped_image = image[start_x:end_x, start_y:end_y]
    cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
    return image


## Cropping
def image_cropping(image, start_x, start_y, end_x, end_y):
    """
    This function is for cropping the image
    :param image: ndarray of image
    :param start_x: starting x coordinate
    :param start_y: starting y coordinate
    :param end_x: ending x coordinate
    :param end_y: ending y coordinate
    :return: cropped image
    """
    cropped_image = image[start_x:end_x, start_y:end_y]
    return cropped_image


def image_flip(image, flip_code):
    """
    This function is for flipping the image
    :param image: ndarray of image
    :param flip_code: 0 for flipping vertically, 1 for flipping horizontally, -1 for flipping both horizontally and vertically
    :return: flipped image
    """
    return cv2.flip(image, flip_code)


if __name__ == '__main__':
    image_path = "images/sample_img.jpg"

    ## Translation
    # image = read_image(image_path)
    # image = resize_image(image, 800, 500)
    # translated_image = image_translation(image, 100, 100)  # right and down
    # show_image(image, "Original Image")
    # show_image(translated_image, "Translated Image")

    ## Rotation
    # image = read_image(image_path)
    # image = resize_image(image, width=800, height=500)
    # rotated_image = image_rotation(image, angle=10)
    # show_image(image, "Original Image")
    # show_image(rotated_image, "Rotated Image")

    ## Clipping
    # image = read_image(image_path)
    # image = resize_image(image, width=800, height=500)
    # clipped_image = image_clipping(image, 100, 100, 400, 400)
    # put_text(clipped_image, "Clipped Image", (100, 100))
    #
    # show_image(image, "Original Image")
    # show_image(clipped_image, "Clipped Image")

    ## Cropping
    # image = read_image(image_path)
    # image = resize_image(image, width=800, height=500)
    # cropped_image = image_cropping(image, 100, 100, 400, 400)
    # show_image(image, "Original Image")
    # show_image(cropped_image, "Cropped Image")

    ## Flipping
    image = read_image(image_path)
    image = resize_image(image, width=800, height=500)
    flipped_image = image_flip(image, 0)
    show_image(image, "Original Image")
    show_image(flipped_image, "Flipped Image")
