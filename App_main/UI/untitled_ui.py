# Form implementation generated from reading ui file 'd:\Python_PORTFOLIO\10_thumbnail_resizer_tool\App_main\UI\untitled.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_fm_main(object):
    def setupUi(self, fm_main):
        fm_main.setObjectName("fm_main")
        fm_main.resize(514, 187)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        fm_main.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(fm_main)
        self.gridLayout.setObjectName("gridLayout")
        self.hl_buttons = QtWidgets.QHBoxLayout()
        self.hl_buttons.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.hl_buttons.setObjectName("hl_buttons")
        self.pb_resize = QtWidgets.QPushButton(parent=fm_main)
        self.pb_resize.setObjectName("pb_resize")
        self.hl_buttons.addWidget(self.pb_resize)
        self.pb_cancel = QtWidgets.QPushButton(parent=fm_main)
        self.pb_cancel.setObjectName("pb_cancel")
        self.hl_buttons.addWidget(self.pb_cancel)
        self.gridLayout.addLayout(self.hl_buttons, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.gb_path_size = QtWidgets.QGroupBox(parent=fm_main)
        self.gb_path_size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_path_size.setObjectName("gb_path_size")
        self.widget = QtWidgets.QWidget(parent=self.gb_path_size)
        self.widget.setGeometry(QtCore.QRect(10, 30, 451, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_image_path = QtWidgets.QLabel(parent=self.widget)
        self.lb_image_path.setObjectName("lb_image_path")
        self.horizontalLayout.addWidget(self.lb_image_path)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.widget1 = QtWidgets.QWidget(parent=self.gb_path_size)
        self.widget1.setGeometry(QtCore.QRect(10, 70, 181, 31))
        self.widget1.setObjectName("widget1")
        self.hl_image_size = QtWidgets.QHBoxLayout(self.widget1)
        self.hl_image_size.setContentsMargins(0, 0, 0, 0)
        self.hl_image_size.setObjectName("hl_image_size")
        self.lb_image_size = QtWidgets.QLabel(parent=self.widget1)
        self.lb_image_size.setObjectName("lb_image_size")
        self.hl_image_size.addWidget(self.lb_image_size)
        self.cb_sizes = QtWidgets.QComboBox(parent=self.widget1)
        self.cb_sizes.setObjectName("cb_sizes")
        self.hl_image_size.addWidget(self.cb_sizes)
        self.gridLayout.addWidget(self.gb_path_size, 0, 0, 1, 2)

        self.retranslateUi(fm_main)
        QtCore.QMetaObject.connectSlotsByName(fm_main)

    def retranslateUi(self, fm_main):
        _translate = QtCore.QCoreApplication.translate
        fm_main.setWindowTitle(_translate("fm_main", "Tumbnail Resizer Tool"))
        self.pb_resize.setText(_translate("fm_main", "Resize"))
        self.pb_cancel.setText(_translate("fm_main", "Cancel"))
        self.gb_path_size.setTitle(_translate("fm_main", "Resize"))
        self.lb_image_path.setText(_translate("fm_main", "Image Path:"))
        self.lb_image_size.setText(_translate("fm_main", "Image size:"))
