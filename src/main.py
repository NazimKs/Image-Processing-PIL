# -*- coding: utf-8 -*-
"""This file contains the main procedure to execute some of the common methods used in image processing.
@author KESKES Nazim
@version 1.0.0
@since 15 Septembre 2022
"""

from PIL.Image import *

# Function to invert the image
def inversion(image):
    """Function allows the inversion of an image
    """
    # Get the size (x,y) of the image
    (x,y) = image.size
    for j in range(y):
        for i in range(x):
            # For each pixel (x,y), invert its color by subtracting its current value from 255
            inv_tmp = 255 - Image.getpixel(image,(i,j))
            # Update the pixel with the new inverted value
            Image.putpixel(image,(i,j),inv_tmp)
    return image

# Function to convert the image to black and white
def black_and_white(image , s):
    """Function allows the conversion of an image to a "black and white" theme
        """
    # Get the size (x,y) of the image
    (x,y) = image.size
    for j in range(y):
        for i in range(x):
            # Get the color value of the pixel
            color = Image.getpixel(image,(i,j))
            # If the color is less than or equal to the threshold value, set it to 0
            if color <= s:
                color = 0
            # If the color is greater than the threshold value, set it to 255
            else:
                color = 255
            # Update the color value of the pixel with the new value
            Image.putpixel(image,(i,j),color)
    return image

# Function to draw a line on the image
def line(image, j , color):
    """Function allowing to draw a white line on the image
    """
    # Get the size (x,y) of the image
    (x,y) = image.size
    for i in range(x):
        # For each pixel where the vertical position is j, set its color to the given color value
        Image.putpixel(image,(i,j),color)
    return image

# Function to darken the image
def darken(image):
    """Function allows the conversion of an image to a darken one.
    """
    # Get the size (x,y) of the image
    (x,y) = image.size
    for i in range(x):
        for j in range(y):
            # Get the color value of the pixel (i,j)
            color = Image.getpixel(image,(i,j))
            # For each pixel (i,j), divide its color value by 2 to make it darker
            Image.putpixel(image,(i,j),color//2)
    return image

# Function to lighten the image
def lighten(image):
    """Function allows the conversion of an image to a lighten one.
    """
    # Get the size (x,y) of the image
    (x,y) = image.size
    for i in range(x):
        for j in range(y):
            # Get the color value of the pixel (i,j)
            color = Image.getpixel(image,(i,j))
            # For each pixel (i,j), multiply its color value by 2 to make it lighter
            # If the resulting value is greater than 255, set the pixel to the brightest color (255, white)
            if 2 * color > 255:
                Image.putpixel(image,(i,j),255)
            # Otherwise, set the pixel to the value of 2 times the original color
            else:
                Image.putpixel(image,(i,j),2 * color)
    return image


# The no_rouge function
def no_rouge(image):
    """Function allows to replace the red color values of each pixel with zero.
    """
    # Get the width and height of the image (x,y)
    (x,y) = image.size
    for i in range(x):
        for j in range(y):
            # Get the RGB values of pixel (i,j)
            (red, green, blue) = image.getpixel((i, j))
            # Set the pixel (i,j) to the same green and blue colors, but with red set to 0
            image.putpixel((i, j), (0, green, blue))
    return image

# A function that returns the value corresponding to the last 3 bits of a number
def value_of_last_3_bits(n):
    """Function that takes an integer n and returns the decimal value corresponding to the last 3 bits in its binary representation.
        """
    tmp = [0,0,0,0,0,0,0,0]
    j = n
    # Convert n to binary form using a list
    for i in range(8):
        tmp[-i-1] = j % 2
        j = j // 2
    # Calculate the decimal value of the last 3 bits
    return tmp[-1] + 2 * tmp[-2] + 4*tmp[-3]

# A function that returns the value corresponding to the last 3 bits of a number, followed by 10000
def shift(m):
    """Function that takes an integer m and returns the decimal value corresponding to the last 3 bits of m followed by the binary digits 10000.
    """
    tmp = [0,0,0,0,0,0,0,0]
    j = m
    # Convert m to binary form using a list
    for i in range(8):
        tmp[-i-1] = j % 2
        j = j // 2
    # Calculate the decimal value of the last 3 bits, followed by 10000
    return (2 ** 4) + (2 ** 5) * tmp[-1] + (2 ** 6) * tmp[-2] + (2 ** 7) * tmp[-3]

# The decoder function using the value_of_last_3_bits and shift functions
def decoder(image):
    """Function that takes an input image and decodes a hidden message that has been encoded into the red, green, and blue color values of each pixel using the last 3 bits of each color value.
    """
    # Get the width and height of the image (x,y)
    (x,y) = image.size
    for i in range(x):
        for j in range(y):
            # Get the RGB values of pixel (i,j)
            (red, green, blue) = image.getpixel((i, j))
            red = shift(value_of_last_3_bits(red))
            green = shift(value_of_last_3_bits(green))
            blue = shift(value_of_last_3_bits(blue))
            # Set the pixel (i,j) to the same colors, but with the last 3 bits shifted to the left and filled with 0s
            image.putpixel((i, j), (red, green, blue))
    return image

# A function that returns the binary value of a number as a list, with leading zeros
def trans_bin(n):
    """Function that takes an integer n and returns a list representing its binary digits.
    """
    tmp = [0,0,0,0,0,0,0,0]
    j = n
    # Convert n to binary form using a list
    for i in range(8):
        tmp[-i-1] = j % 2
        j = j // 2
    # Return the binary value as a list
    return tmp

# The cache function that combines two images into one
def cache(illusion_image, hidden_image):
    """
    Function that takes two input images, an "illusion" image and a "hidden" image, and encodes the hidden image into the red and blue color values of each pixel of the illusion image using the last 3 bits of each color value.
    """
    # Get the width and height of the image (x,y)
    (x,y) = illusion_image.size
    for i in range(x):
        for j in range(y):
            # Get the RGB values

            (rouge1, vert1, bleu1) = illusion_image.getpixel((i, j))

            # recuperer la valeur de les couleurs RBG du pixel(i,j) de l'image cacher
            (rouge2, vert2, bleu2) = hidden_image.getpixel((i, j))

            #calculer le nouveau rouge on prennant les 5 bits les plus forts de l'image illusion completer par les 3 bits les plus forts de l'image caché
            n, m = trans_bin(rouge1), trans_bin(rouge2)
            rouge = m[2] + 2 * m[1] + 4 * m[0] + 8 * n[4] + 16 * n[3] + 32 * n[2] + 64 * n[1] + 128 * n[0]
            # calculer le nouveau vert on prennant les 5 bits les plus forts de l'image illusion completer par les 3 bits les plus forts de l'image caché
            n, m = trans_bin(bleu1), trans_bin(bleu2)
            bleu = m[2] + 2 * m[1] + 4 * m[0] + 8 * n[4] + 16 * n[3] + 32 * n[2] + 64 * n[1] + 128 * n[0]
            # calculer le nouveau bleu on prennant les 5 bits les plus forts de l'image illusion completer par les 3 bits les plus forts de l'image caché
            n, m = trans_bin(vert1), trans_bin(vert2)
            vert = m[2] + 2 * m[1] + 4 * m[0] + 8 * n[4] + 16 * n[3] + 32 * n[2] + 64 * n[1] + 128 * n[0]
            #affecter les 3 nouvelles couleurs a le pixel(i,j)
            illusion_image.putpixel((i, j), (rouge, vert, bleu))
    return illusion_image


def main() -> None:
    """a main Function allowing the execution of a sequence of the image processing methods defined above to test them.
    """
    # Open the image file
    img = open("assets/black_and_white.png","r")
    # Display the image
    Image.show(img)

    # Display the inverted image
    Image.show(inversion(img))

    # Display the black and white image with threshold value of 125
    img = open("assets/black_and_white.png", "r")
    Image.show(black_and_white(img, 125))

    # Display the image with a white (255) line at row 100
    img = open("assets/black_and_white.png", "r")
    Image.show(line(img, 100, 255))

    # Display the darkened image
    img = open("assets/black_and_white.png", "r")
    Image.show(darken(img))

    # Display the brightened image
    img = open("assets/black_and_white.png", "r")
    Image.show(lighten(img))

    # Display the image without red color
    img = open("assets/colors.png", "r")
    Image.show(no_rouge(img))

    # Test the function value_of_last_3_bits
    print(value_of_last_3_bits(187))

    # Test the function shift
    print(shift(3))

    # Display the decoded image without red color
    img = open("assets/colors.png", "r")
    Image.show(decoder(img))

    # Open the image to hide and the image to hide it in
    img = open("assets/colors.png", "r")
    img2 = open("assets/cache_image.jpg", "r")
    # Display the final image with the hidden image
    Image.show(cache(img, img2))

    # Close the image
    img.close()

if __name__ == "__main__":
    main()
