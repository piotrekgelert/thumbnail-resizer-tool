import os
import sys

from PIL import Image
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from UI.untitled_ui import Ui_fm_main


class ThumbResizer(qtw.QWidget, Ui_fm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cb_sizes.addItems([16, 32,64,128])


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = ThumbResizer()
    window.show()
    sys.exit(app.exec())
# image_path = r'D:\Python_PORTFOLIO\10_thumbnail_resizer_tool\App_icons'
# image_in = 'content-management.png'
# size = 16

# with Image.open(os.path.join(image_path, image_in)) as im:
#     im.resize((size, size), Image.Resampling.LANCZOS)
#     im.save(os.path.join(image_path, image_in[:-4]+'_thumb.png'))

# '''

# 16, 32,64,128'''