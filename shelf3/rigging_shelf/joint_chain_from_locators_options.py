import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om1
import maya.OpenMayaUI as ui
import maya.cmds as cmds

import joint_helpers as jnts

def maya_maya_window():
    main_window_pointer = ui.MQtUtil.mainWindow()
    
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_pointer), QtWidgets.QWidget)
    

class JointChainFromLocatorsOptions(QtWidgets.QDialog):
    
    __instance = None
    
    @classmethod
    def show_dialog(cls):
        if cls.__instance is None:
            cls.__instance = JointChainFromLocatorsOptions()
            
        if cls.__instance.isHidden():
            cls.__instance.show()
        else:
            cls.__instance.raise_()
            cls.__instance.activateWindow()
    
    def __init__(self, parent=maya_maya_window()):
        super(JointChainFromLocatorsOptions, self).__init__(parent)
        
        self.setWindowTitle("Joint chain from locators options")
        self.setMinimumWidth(400)
        self.__hide_question_mark_button()
        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        
    def __hide_question_mark_button(self):
        if sys.version_info.major >= 3:
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        else:
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
            
    def __confirm(self, e):
                
        # Execution code
        aim_vector = []
        up_vector = []
        
        for axis in self.aim_axis_widgets:
            value = float(axis.text())
            aim_vector.append(value)
            
        for axis in self.up_vector_axis_widgets:
            value = float(axis.text())
            up_vector.append(value)
        
        jnts.create_joint_chain_from_locators_by_selection(aim_vector = aim_vector, up_vector = up_vector)
        ##
        
        self.__close()
        
    def __close(self):
        
        self.close()
            
    def create_widgets(self):
    
        self.aim_axis_widgets = []
        self.up_vector_axis_widgets = []
        self.onlyFloat = QtGui.QDoubleValidator()
        
        for idx in range(3):
            aim_vector = QtWidgets.QLineEdit()
            aim_vector.setValidator(self.onlyFloat)
            if idx == 0:
                aim_vector.insert("1.0000")
            else:
                aim_vector.insert("0.0000")
            self.aim_axis_widgets.append(aim_vector)

            up_vector_axis = QtWidgets.QLineEdit()
            up_vector_axis.setValidator(self.onlyFloat)
            if idx == 1:
                up_vector_axis.insert("1.0000")
            else:
                up_vector_axis.insert("0.0000")
            self.up_vector_axis_widgets.append(up_vector_axis)
        
        confirm_btn_lbl = "Confirm"
        self.confirm_btn = QtWidgets.QPushButton(confirm_btn_lbl)
        
        cancel_btn_lbl = "Cancel"
        self.cancel_btn = QtWidgets.QPushButton(cancel_btn_lbl)
        
    def create_layouts(self):
        
        aim_vectors_layout = QtWidgets.QHBoxLayout()
        up_vectors_layout = QtWidgets.QHBoxLayout()
        
        for widget in self.aim_axis_widgets:
            aim_vectors_layout.addWidget(widget)
        
        for widget in self.up_vector_axis_widgets:
            up_vectors_layout.addWidget(widget)
        
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.confirm_btn)
        btn_layout.addWidget(self.cancel_btn)
        
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Aim vector:", aim_vectors_layout)
        form_layout.addRow("Up vector:", up_vectors_layout)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)
        
    def create_connections(self):
        
        self.confirm_btn.clicked.connect(self.__confirm)
        self.cancel_btn.clicked.connect(self.__close)
        

if __name__ == "__main__":
    
    try:    
        test_dialog.close()
        test_dialog.deleteLater()
    except:
        pass
    
    cmds.file(new=True, force=True)
    
    test_dialog = JointChainFromLocatorsOptions()
    test_dialog.show()