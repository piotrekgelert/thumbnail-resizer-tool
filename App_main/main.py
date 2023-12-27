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
        self.setup_icons()
        self.pb_resize.clicked.connect(self.image_workout)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_select_img_path.clicked.connect(self.path_to_file)
        self.pb_select_folder_path.clicked.connect(self.path_to_folder)

    def setup_icons(self):
        root_folder = r''.format(pathlib.Path(__file__).parent.absolute().parent)
        main_path = os.path.join(root_folder, 'App_icons')
        self.setWindowIcon(
            qtg.QIcon(
                '{}\\{}'.format(main_path, 'content-management_thumb.png')))
        self.pb_select_img_path.setIcon(
            qtg.QIcon('{}\\{}'.format(main_path, 'image_in_thumb.png')))
        self.pb_select_folder_path.setIcon(
            qtg.QIcon('{}\\{}'.format(main_path, 'image_out_thumb.png')))
        self.pb_resize.setIcon(
            qtg.QIcon('{}\\{}'.format(main_path, 'scalability_thumb.png')))
        self.pb_cancel.setIcon(
            qtg.QIcon('{}\\{}'.format(main_path, 'cross_thumb.png')))
        self.lb_selected_img_path_image.setPixmap(
            qtg.QPixmap('{}\\{}'.format(main_path, 'pointer_icon_thumb.png')))
        self.lb_selected_folder_path_image.setPixmap(
            qtg.QPixmap('{}\\{}'.format(main_path, 'pointer_folder_thumb.png')))
        self.lb_image_size_image.setPixmap(
            qtg.QPixmap('{}\\{}'.format(main_path, 'icon_sizes_thumb.png')))
        self.lb_message_image.setPixmap(
            qtg.QPixmap('{}\\{}'.format(main_path, 'mail_thumb.png')))
    
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
                self.on_resize_click()
            else:
                img.save(
                    os.path.join(
                        self.save_pathh, img_name
                        )
                    )
                self.on_resize_click()
    
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
        self.lb_message.setText('Path to icon added')


    def path_to_folder(self):
        self.lb_selected_folder_path.clear()
        self.lb_message.setText('')
        folder_path = qtw.QFileDialog.getExistingDirectory()
        self.save_pathh = folder_path
        self.lb_selected_folder_path.setText(folder_path)
        self.lb_message.setText('Path to folder added')
    
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
