"""
@author HeTongHao
@date 2019/4/3 14:27
@description
需要安装:
brew install imagemagick@6
brew install gs
"""

from wand.image import Image


def convert_pdf_to_jpg(filename, resolution=120):
    with Image(filename=filename, resolution=int(resolution / 10)) as img:
        print('pages = ', len(img.sequence))
        with img.convert('jpeg') as converted:
            converted.save(filename='/Users/HTH/Desktop/bull文件/page.jpeg')


convert_pdf_to_jpg('/Users/HTH/Desktop/bull文件/er图.pdf', 500)
