import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om1
import maya.OpenMayaUI as ui
import maya.cmds as cmds

import attributes_helpers as ah


def maya_maya_window():
    main_window_pointer = ui.MQtUtil.mainWindow()
    
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_pointer), QtWidgets.QWidget)
    

class CategoryPromptUI(QtWidgets.QDialog):
    
    __instance = None
    
    @classmethod
    def show_dialog(cls):
        if cls.__instance is None:
            cls.__instance = CategoryPromptUI()
            
        if cls.__instance.isHidden():
            cls.__instance.show()
        else:
            cls.__instance.raise_()
            cls.__instance.activateWindow()
    
    def __init__(self, parent=maya_maya_window()):
        super(CategoryPromptUI, self).__init__(parent)
        
        self.setWindowTitle("Category name")
        self.setMinimumWidth(400)
        self.__hide_question_mark_button()
        
        self.category_name = None
        self.confirm_btn = None
        self.cancel_btn = None
        
        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        
    def __hide_question_mark_button(self):
        if sys.version_info.major >= 3:
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        else:
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
            
    def __get_category_name(self, e):
        
        category_name = self.category_name.text()
        
        # Add the code here
            
        self.category_name.clear()
        
        self.__close()
        
    def __close(self):
        
        self.category_name.clear()
        self.close()
            
    def create_widgets(self):
        
        self.category_name = QtWidgets.QLineEdit()
        
        confirm_btn_lbl = "Confirm"
        self.confirm_btn = QtWidgets.QPushButton(confirm_btn_lbl)
        
        cancel_btn_lbl = "Cancel"
        self.cancel_btn = QtWidgets.QPushButton(cancel_btn_lbl)
        
    def create_layouts(self):
        
        category_name_layout = QtWidgets.QHBoxLayout()
        category_name_layout.addWidget(self.category_name)
        
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.confirm_btn)
        btn_layout.addWidget(self.cancel_btn)
        
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Category name:", category_name_layout)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)
        
    def create_connections(self):
        
        self.confirm_btn.clicked.connect(self.__get_category_name)
        self.cancel_btn.clicked.connect(self.__close)
        

if __name__ == "__main__":
    
    try:    
        test_dialog.close()
        test_dialog.deleteLater()
    except:
        pass
    
    cmds.file(new=True, force=True)
    
    test_dialog = CategoryPromptUI()
    test_dialog.show()