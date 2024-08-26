from PIL import Image
import glob
import os


def resize_image(img, folder_name):
    width, height = img.size


    # determine if portrait or horizontal
    if width < height:
        new_width = 500
        new_height = 770
    else:
        new_width = 770
        new_height = 500


    # size down while maintaining aspect ratio
    img.thumbnail((new_width + 50, new_height + 50))


    # crop to desired size and save to new folder
    img.crop((0, 0, new_width, new_height)).save(f"./resized/{folder_name}/" + name + "_Resized.jpg")


# extract all images under photoshoot, under any folder
portraits = glob.glob('./photoshoot' + '/**/*.jpg', recursive=True)


for portrait in portraits:
    with Image.open(portrait) as img:
        # create a new folder for the photo under "resized"
        folder_name = portrait.split(os.sep)[1]
        if not os.path.exists(f"./resized/{folder_name}/"):
            os.makedirs(f"./resized/{folder_name}/")


        # extract name from original photo
        name = portrait.split(os.sep)[-1].split('.')[0]


        # apply resizing
        resize_image(img, folder_name)



