"""
Authors: Alexander Bousman and Javan Hirwa
inverted.py
Project 11

This program takes all the images in the card_images folder
inverts their color, saving the inversion as separate photos
in the inverted_images folder
"""

from PIL import Image, ImageOps
import os

for i in os.listdir("./card_images"):
    img = Image.open("./card_images/" + i)
    newImg = ImageOps.invert(img.convert('RGB'))
    newImg.save("./card_images/" + ("inverted_" + i))