import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om1
import maya.OpenMayaUI as ui
import maya.cmds as cmds

def maya_maya_window():
    main_window_pointer = ui.MQtUtil.mainWindow()
    
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_pointer), QtWidgets.QWidget)
    

class DividerPromptUI(QtWidgets.QDialog):
    
    __instance = None
    
    @classmethod
    def show_dialog(cls):
        if cls.__instance is None:
            cls.__instance = DividerPromptUI()
            
        if cls.__instance.isHidden():
            cls.__instance.show()
        else:
            cls.__instance.raise_()
            cls.__instance.activateWindow()
    
    def __init__(self, parent=maya_maya_window(), callback=None):
        super(DividerPromptUI, self).__init__(parent)
        
        self.setWindowTitle("New Divider")
        self.setMinimumWidth(400)
        self.__hide_question_mark_button()
        self.__callback = callback
        
        self.divider_name = None
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
            
    def __get_divider_name(self, e):
        
        divider_name = self.divider_name.text()
        
        if divider_name:
            self.__callback(divider_name)
        else:
            self.__close()
            
        self.divider_name.clear()
        
        self.__close()
        
    def __close(self):
        
        self.divider_name.clear()
        self.close()
            
    def create_widgets(self):
        
        self.divider_name = QtWidgets.QLineEdit()
        
        confirm_btn_lbl = "Confirm"
        self.confirm_btn = QtWidgets.QPushButton(confirm_btn_lbl)
        
        cancel_btn_lbl = "Cancel"
        self.cancel_btn = QtWidgets.QPushButton(cancel_btn_lbl)
        
    def create_layouts(self):
        
        divider_name_layout = QtWidgets.QHBoxLayout()
        divider_name_layout.addWidget(self.divider_name)
        
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.confirm_btn)
        btn_layout.addWidget(self.cancel_btn)
        
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Divider name:", divider_name_layout)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)
        
    def create_connections(self):
        
        self.confirm_btn.clicked.connect(self.__get_divider_name)
        self.cancel_btn.clicked.connect(self.__close)

if __name__ == "__main__":
    
    try:    
        test_dialog.close()
        test_dialog.deleteLater()
    except:
        pass
    
    cmds.file(new=True, force=True)
    
    test_dialog = DividerPromptUI(callback=my_callback)
    test_dialog.show()