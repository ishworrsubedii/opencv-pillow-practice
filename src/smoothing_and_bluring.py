"""
Created By: ishwor subedi
Date: 2024-04-16
"""

"""
We will only smooth the image if the image has a lot of noise and lighting conditions are not good.
we will use blurring the image to reduce the noise and details in the image.
in previously we have used the cv2.GaussianBlur() function to blur the image.
But here we will use other function for smoothing the images.
"""

import cv2
from reading_images_video import read_image, show_image, resize_image


class SmoothingImage:
    """
    This class is for smoothing the image using different techniques.
    """

    def __init__(self, image):
        self.image = image

    def average_blur(self, kernel_size=(5, 5)):  # higher kernal size will give more blur image
        """
        We define the kernal size for image from the image and that will calculate the average of all the pixels and
        update the central element , it will repeate the same for all the pixels in the image.
         This function is for smoothing the image using average blur.
        :param kernel_size: Tuple of kernel size for blurring the image.
        :return: Blurred image.
        """
        blurred_image = cv2.blur(self.image, kernel_size)
        return blurred_image

    def gaussian_blur(self, kernel_size=(5, 5), sigmaX=0):
        """
        It is similar to the average blur but instead of using the average of all the pixel it has the weight for each pixel.it will average of the products of those weights.
        this will give the less blurring effect.It is more accurate than the average blur.

        :param kernel_size: Tuple of kernel size for blurring the image.
        :param sigmaX: Standard deviation in the X direction.
        :return: Blurred image.
        """
        blurred_image = cv2.GaussianBlur(self.image, kernel_size, sigmaX)
        return blurred_image

    def median_blur(self, kernel_size=5):
        """
        It is also same things as the average blur but instead of using the average of all the pixel it will use the median of all the pixel.It is more effective among average and gaussian blur.
        This function is for smoothing the image using median blur.
        :param kernel_size: Kernel size for blurring the image.
        :return: Blurred image.
        """
        blurred_image = cv2.medianBlur(self.image, kernel_size)
        return blurred_image

    def bilateral_filter(self, d=9, sigmaColor=15, sigmaSpace=15):
        """
        This is the most effective among all the blurring techniques. It will preserve the edges and reduce the noise.
        It will apply blurring and it will retain the edges as well.
        This function is for smoothing the image using bilateral filter.
        :param d: Diameter of each pixel neighborhood.
        :param sigmaColor: Filter sigma in the color space.
        :param sigmaSpace: Filter sigma in the coordinate space.
        :return: Blurred image.
        """
        blurred_image = cv2.bilateralFilter(self.image, d, sigmaColor, sigmaSpace)
        return blurred_image


if __name__ == '__main__':
    image_path = "images/sample_noise.png"
    image = read_image(image_path)
    image = resize_image(image=image, width=800, height=500)
    smoothing_image = SmoothingImage(image)

    ## Average Blur
    # average_blur = smoothing_image.average_blur()
    # show_image(image, title="Original Image")
    # show_image(average_blur, title="Average Blur Image")

    ## Median Blur
    # median_blur = smoothing_image.median_blur()
    # show_image(image, title="Original Image")
    # show_image(median_blur, title="Median Blur Image")

    ## Gaussian Blur
    # gaussian_blur = smoothing_image.gaussian_blur()
    # show_image(image, title="Original Image")
    # show_image(gaussian_blur, title="Gaussian Blur Image")

    ## Bilateral Filter
    bilateral_filter = smoothing_image.bilateral_filter()
    show_image(image, title="Original Image")
    show_image(bilateral_filter, title="Bilateral Filter Image")
