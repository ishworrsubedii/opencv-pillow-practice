"""
Created By: ishwor subedi
Date: 2024-04-16
"""
"""
There are for basic bitwise operator
1. AND
2. OR
3. NOT
4. XOR
"""

import cv2
import numpy as np
from reading_images_video import read_image, show_image, resize_image


class BitwiseOperation:

    def __init__(self):
        self.blank_image = np.zeros((400, 400), dtype='uint8')
        self.rectangle_image = cv2.rectangle(self.blank_image.copy(), (30, 30), (370, 370), 255, -1)
        self.circle_image = cv2.circle(self.blank_image.copy(), (200, 200), 200, (255, 0, 0), -1)

    def bitwise_and(self):
        """
        It will place two images into the each other and if they are same then it will return the same image.

        It will return the intersection of the images.
        :return: Intersection of the images.
        """
        bitwise_and_image = cv2.bitwise_and(self.rectangle_image, self.circle_image)
        return bitwise_and_image

    def bitwise_or(self):
        """
        It will place two images into the each other and if they are same then it will return the same image.
        It will return the union of the images.
        :return: Union of the images.
        """
        bitwise_or_image = cv2.bitwise_or(self.rectangle_image, self.circle_image)
        return bitwise_or_image

    def bitwise_not(self):
        """
        It invert the binary color of the image.
        It will return the inverse of the image.
        :return: Inverse of the image.
        """
        bitwise_not_image = cv2.bitwise_not(self.rectangle_image)
        return bitwise_not_image

    def bitwise_xor(self):
        """
        Non intersecting regions of the images will be white.
        It will return the symmetric difference of the images.
        :return: Symmetric difference of the images.
        """
        bitwise_xor_image = cv2.bitwise_xor(self.rectangle_image, self.circle_image)
        return bitwise_xor_image


if __name__ == '__main__':
    bitwise_operation = BitwiseOperation()
    show_image(bitwise_operation.rectangle_image, title="Rectangle Image")
    show_image(bitwise_operation.circle_image, title="Circle Image")

    ## Bitwise AND

    bitwise_and_image = bitwise_operation.bitwise_and()
    show_image(bitwise_and_image, title="Bitwise AND Image")

    ## Bitwise OR
    bitwise_or_image = bitwise_operation.bitwise_or()
    show_image(bitwise_or_image, title="Bitwise OR Image")
    ## Bitwise Not
    bitwise_not_image = bitwise_operation.bitwise_not()
    show_image(bitwise_not_image, title="Bitwise NOT Image")

    ## Bitwise XOR
    bitwise_xor_image = bitwise_operation.bitwise_xor()
    show_image(bitwise_xor_image, title="Bitwise XOR Image")
