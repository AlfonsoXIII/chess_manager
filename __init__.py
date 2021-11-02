import os
from PIL import Image

import main

def Main():

    path_wait_list = ["images/2DBoardPieces/0/", 
                    "images/2DBoardPieces/1/", 
                    "images/base_buttons/",
                    "images/menu_buttons/"]
    images = {}

    for path in path_wait_list:
        files = os.listdir(path)

        for file in files:
            image = Image.open(path+file) #Obertura del spritemap amb la llibreria PIL
            images[(file.split("."))[0]] = image

    main.Main(images)

if __name__ == "__main__":
    Main()