
from resize import Processor
from resize.helper import Helper


class TestProcessor:
  
    def test_resize_image(self):

        images = Helper.get_images_files(self, '../img')
        x = 75
        y = 75

        res = Processor.resize(images, x, y)

        assert res is not None 
        assert len(res) == len(images)



