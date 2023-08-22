

# if(len(sys.argv) == 1):
#     print("Usage: resize_images pathImages newPixelX newPixelY")
# else:
#      path = str(sys.argv[1])
#      x = str(sys.argv[2])
#      y = str(sys.argv[3])


# folder path
from resize import Processor
from resize.helper import Helper


dir_path = "./" # current directory
x = 75
y = 75

img = Processor()
# list to store files name
imgFiles = Helper.get_images_files(dir_path)

print(imgFiles)

# img.resize(imgFiles,x,y)




