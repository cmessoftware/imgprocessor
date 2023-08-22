# Importing Image class from PIL module
import os
from PIL import Image

class Processor:
      
    
      def resize(self, images, newx , newy):

        if images is None:
           return None
        
        res = []
        for img_file_name in images:
          # Opens a image in RGB mode
          im = Image.open(img_file_name)
          
          # Size of the image in pixels (size of original image)
          # (This is not mandatory)
          _, height = im.size
          
          # Setting the points for cropped image
          left = 4
          top = height / 5
          right = 154
          bottom = 3 * height / 5
          
          # Cropped image of above dimension
          # (It will not change original image)
          im2 = im.crop((left, top, right, bottom))
          newsize = (newx, newy)
          im2 = im2.resize(newsize)
          outputfilename = os.path.join(img_file_name, '75_75',img_file_name )
          im2.save(outputfilename, 'JPEG', quality=90)
          res.append(im2)

        return res
        # im2.show()
          
    
  
