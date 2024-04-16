"""
Created By: ishwor subedi
Date: 2024-04-16
"""
import cv2
from reading_images_video import show_image, read_image, resize_image


class ColorSpaceChange:
    """
    This class is for changing the color space of the image using OpenCV.
    """

    def __init__(self, image):
        self.image = image

    def bgr_gray(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return image

    def bgr_to_hsv(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        return image

    def bgr_to_lab(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)
        return image

    def bgr_to_rgb(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        return image

    def hsv_to_bgr(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)
        return image


if __name__ == '__main__':
    image_path = "images/sample_img.jpg"
    image = read_image(image_path)
    image = resize_image(image, 800, 500)
    color_space = ColorSpaceChange(image)
    gray_image = color_space.bgr_gray()
    hsv_image = color_space.bgr_to_hsv()
    lab_image = color_space.bgr_to_lab()
    rgb_image = color_space.bgr_to_rgb()
    bgr_image = color_space.hsv_to_bgr()
    show_image(title="Original image", image=image)
    show_image(title="Gray image", image=gray_image)
    show_image(title="HSV image", image=hsv_image)
    show_image(title="LAB image", image=lab_image)
    show_image(title="RGB image", image=rgb_image)
    show_image(title="HSV To BGR", image=bgr_image)
