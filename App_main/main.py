import os
import pathlib
import sys

from PIL import Image
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw
from UI.untitled_ui import Ui_fm_main


class ThumbResizer(qtw.QWidget, Ui_fm_main):
    sizes_dict = {
        '16px':16, '32px':32, '64px':64, '128px':128,'256px': 256,'512px': 512
        }
    image_size = 0
    pathh, save_pathh = '', ''
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cb_sizes.addItems([k for k in self.sizes_dict.keys()])
        self.pb_resize.clicked.connect(self.image_workout)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_select_img_path.clicked.connect(self.path_to_file)
        self.pb_select_folder_path.clicked.connect(self.path_to_folder)

    def image_open(self):
        pass

    
    def image_workout(self):
        image_name, num, image_extension = self.img_name_extension(self.pathh)
        
        with Image.open(self.pathh) as im:
            self.image_size = im.size[0]
            curr_size = self.sizes_dict[self.cb_sizes.currentText()]
            img = im.resize((curr_size, curr_size), Image.Resampling.LANCZOS)
            img_name = image_name+f'_thumb.{image_extension}'
            
            if self.already_exists(self.save_pathh, img_name):
                img.save(
                os.path.join(
                    self.save_pathh,
                    image_name+f'{num+1}_thumb.{image_extension}'
                    )
                )
            else:
                img.save(
                    os.path.join(
                        self.save_pathh, img_name
                        )
                    )
    
    def path_to_file(self):
        file_path = qtw.QFileDialog.getOpenFileName()
        self.pathh = file_path[0]
        self.lb_selected_img_path.setText(file_path[0])

    def path_to_folder(self):
        folder_path = qtw.QFileDialog.getExistingDirectory()
        self.save_pathh = folder_path
        self.lb_selected_folder_path.setText(folder_path)
    
    def img_name_extension(self, p:str):
        img_name, img_extension = p.split('/')[-1].split('.')
        nums = [x for x in img_name if x.isdigit()]
        if len(nums):
            return img_name, int(''.join(nums)), img_extension
        else:
            return img_name, 0, img_extension
    
    def already_exists(self, p:str, file):
        return file in os.listdir(p)
    
    def check_icon_sizes(self):
        self.cb_sizes.addItems(
            [k for k, v in self.sizes_dict.items() if v < self.image_size]
            )

        

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = ThumbResizer()
    window.show()
    sys.exit(app.exec())
