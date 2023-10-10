import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om1
import maya.OpenMayaUI as ui
import maya.cmds as cmds

import joint_helpers as jnt

def maya_maya_window():
    main_window_pointer = ui.MQtUtil.mainWindow()
    
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_pointer), QtWidgets.QWidget)
    

class JointCreatorOptions(QtWidgets.QDialog):
    
    __instance = None
    
    @classmethod
    def show_dialog(cls):
        if cls.__instance is None:
            cls.__instance = JointCreatorOptions()
            
        if cls.__instance.isHidden():
            cls.__instance.show()
        else:
            cls.__instance.raise_()
            cls.__instance.activateWindow()
    
    def __init__(self, parent=maya_maya_window()):
        super(JointCreatorOptions, self).__init__(parent)
        
        self.setWindowTitle("Open import dialog")
        self.setMinimumWidth(400)
        self.__hide_question_mark_button()
        
        self.joint_name = None
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
            
    def __get_joint_name(self, e):
        joint_name = self.joint_name.text()
        
        if joint_name:
            jnt.create_joint_under_selected_node(joint_name)
        else:
            jnt.create_joint_under_selected_node()
            
        self.joint_name.clear()
        
        self.__close()
        
    def __close(self):
        
        self.joint_name.clear()
        self.close()
            
    def create_widgets(self):
        
        self.joint_name = QtWidgets.QLineEdit()
        
        confirm_btn_lbl = "Confirm"
        self.confirm_btn = QtWidgets.QPushButton(confirm_btn_lbl)
        
        cancel_btn_lbl = "Cancel"
        self.cancel_btn = QtWidgets.QPushButton(cancel_btn_lbl)
        
    def create_layouts(self):
        
        joint_name_layout = QtWidgets.QHBoxLayout()
        joint_name_layout.addWidget(self.joint_name)
        
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.confirm_btn)
        btn_layout.addWidget(self.cancel_btn)
        
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Joint name:", joint_name_layout)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)
        
    def create_connections(self):
        
        self.confirm_btn.clicked.connect(self.__get_joint_name)
        self.cancel_btn.clicked.connect(self.__close)
        

if __name__ == "__main__":
    
    try:    
        test_dialog.close()
        test_dialog.deleteLater()
    except:
        pass
    
    cmds.file(new=True, force=True)
    
    test_dialog = JointCreatorOptions()
    test_dialog.show()