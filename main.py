import os
import shutil

from PIL import Image

input_path = "Angel/"
output_path = "output/"

supported_extensions = (".jpeg", ".jpg", ".png", ".tiff", ".tif", ".raw", ".webp", ".bmp")


if __name__ == '__main__':
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)

    for path, subdirs, files in os.walk(input_path):
        print(path, subdirs, files)
        os.makedirs(output_path + path)
        for name in files:
            filename, file_ext = os.path.splitext(name)
            if file_ext in supported_extensions:
                img = Image.open(path + "/" + name)
                width = img.width
                height = img.height
                if width > 3000 or height > 3000:
                    if width > 3000:
                        os.system("ffmpeg -i " + path + "/" + name + " -vf scale=3000:-1 " + output_path + path + "/" + filename + ".jpg")
                    else:
                        os.system("ffmpeg -i " + path + "/" + name + " -vf scale=-1:3000 " + output_path + path + "/" + filename + ".jpg")


