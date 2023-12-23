import os
import pathlib
import sys

from PIL import Image
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from UI.untitled_ui import Ui_fm_main


class ThumbResizer(qtw.QWidget, Ui_fm_main):
    sizes_dict = {'16px':16, '32px':32, '64px':64, '128px':128,'256px': 256,'512px': 512}
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cb_sizes.addItems([x for x in self.sizes_dict.keys()])
        self.pb_resize.clicked.connect(self.image_workout)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_select_img_path.clicked.connect(self.path_to_file)
        self.pb_select_folder_path.clicked.connect(self.path_to_folder)

    def image_workout(self):
        pathh = self.pb_select_img_path.text()
        save_pathh = self.pb_select_folder_path.text()
        image_name = pathh.split('\\')[-1].split('.')[0]
        curr_size = self.sizes_dict[self.cb_sizes.currentText()]
        with Image.open(pathh) as im:
            img = im.resize((curr_size, curr_size), Image.Resampling.LANCZOS)
            img.save(os.path.join(save_pathh, image_name+'_thumb.png'))
    
    def path_to_file(self):
        file_path = qtw.QFileDialog.getOpenFileName()
        self.lb_selected_img_path.setText(file_path[0])
        self.check_img_in_folder(file_path[0])

    def path_to_folder(self):
        folder_path = qtw.QFileDialog.getExistingDirectory()
        self.lb_selected_folder_path.setText(folder_path)
        
    
    def check_img_in_folder(self, pth):
        print(pth)

        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = ThumbResizer()
    window.show()
    sys.exit(app.exec())
