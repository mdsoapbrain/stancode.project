"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red = 0
    green = 0
    blue = 0

    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue

    color_list = [red / len(pixels), green / len(pixels), blue / len(pixels)]
    return color_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    average_color = get_average(pixels)  # Calculate the average color of the pixels
    best_pixel = None
    min_dist = float('inf')  # Initialize minimum distance to a large value

    for pixel in pixels:
        dist = get_pixel_dist(pixel, average_color[0], average_color[1], average_color[2])  # Calculate color distance
        if dist < min_dist:  # Find the pixel with the smallest distance to the average color
            min_dist = dist
            best_pixel = pixel

    return best_pixel  # Return the best pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)  # Create a blank image with the same dimensions

    for x in range(width):
        for y in range(height):
            pixels = [image.get_pixel(x, y) for image in images]  # Extract pixels at (x, y) from all images
            best_pixel = get_best_pixel(pixels)  # Find the best pixel for this position
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red  # Set the best pixel color to the result image
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    print("Displaying image!")
    result.show()  # Display the resulting image


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):  # Find all .jpg files in the directory
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)  # Get a list of .jpg filenames in the directory
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)  # Load each image
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])  # Load all images from the provided directory
    solve(images)  # Process the images and create the ghost effect


if __name__ == '__main__':
    main()
