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
    pathh, save_pathh = '', ''
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_resize.clicked.connect(
            lambda: [self.image_workout, self.on_resize_click]
            )
        self.pb_cancel.clicked.connect(self.close)
        self.pb_select_img_path.clicked.connect(self.path_to_file)
        self.pb_select_folder_path.clicked.connect(self.path_to_folder)
  
    def image_workout(self):
        image_name, num, image_extension = self.img_name_extension(self.pathh)
        
        with Image.open(self.pathh) as im:
            curr_size = self.sizes_dict[self.cb_sizes.currentText()]
            img = im.resize((curr_size, curr_size), Image.Resampling.LANCZOS)
            img_name = image_name+f'_thumb.{image_extension}'
            
            if img_name in os.listdir(self.save_pathh):
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
        self.lb_selected_img_path.clear()
        self.lb_message.setText('')

        file_path = qtw.QFileDialog.getOpenFileName()
        
        with Image.open(file_path[0]) as im:
            self.cb_sizes.clear()
            self.cb_sizes.addItems(
                [k for k, v in self.sizes_dict.items() if v < im.size[0]]
                )

        self.pathh = file_path[0]
        self.lb_selected_img_path.setText(file_path[0])


    def path_to_folder(self):
        self.lb_selected_folder_path.clear()
        self.lb_message.setText('')
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
    
    def on_resize_click(self):
        self.lb_message.setText('Resize successful')

        

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = ThumbResizer()
    window.show()
    sys.exit(app.exec())
