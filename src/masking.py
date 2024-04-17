"""
Created By: ishwor subedi
Date: 2024-04-16
"""
"""
Masking is essential in image processing when if we want to extract the region of interest from the image.like form the person image we want to extract the face of the person.

"""

import cv2
import numpy as np
from reading_images_video import read_image, show_image, resize_image


class Masking:
    def __init__(self, image):
        w, h, _ = image.shape
        self.blank_image = np.zeros((w, h), dtype='uint8')
        self.image = image

    def create_mask(self):
        center = (self.image.shape[1] // 2, image.shape[0] // 2)
        mask = cv2.circle(self.blank_image.copy(), (center), 200, (255, 0, 0), -1)
        masked_image = cv2.bitwise_and(self.image, self.image, mask=mask)
        return mask, masked_image


if __name__ == '__main__':
    image_path = "images/sample_img.jpg"
    image = read_image(image_path)
    image = resize_image(image, 800, 500)
    mask = Masking(image)
    show_image(mask.blank_image, title="Blank Image")
    show_image(mask.image, title="Original Image")
    mask_image, masked_image = mask.create_mask()
    show_image(mask_image, title="Mask Image")
    show_image(masked_image, title="Masked Image")
