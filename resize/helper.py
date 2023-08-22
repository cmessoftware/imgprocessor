

import os


class Helper:

    def get_images_files(self, path) -> list:
        img_files = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith((".jpg", ".jpeg",".png"))]
        return img_files

