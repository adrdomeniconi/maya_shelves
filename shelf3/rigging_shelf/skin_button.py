import maya.cmds as cmds
from button import ShelfButton
from button import MenuItem

import skin_helpers as sh

class SkinButton(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, label="Copy Skin", button_click=ShelfButton.RIGHT_CLICK, icon="skin", icon_only=True)
        
        self.sh = sh
        
        self.add_menu_items([
            MenuItem("Copy skin in hierarchy", command=self.copy_skin_in_hierarchy),
            MenuItem("Copy selected skin", command=self.copy_selected_skin)
        ]) 
        
    def single_click(self):
        self.sh.copy_skin_in_hierarchy()
    
    def copy_selected_skin(self, *args):
        self.sh.copy_skin()
    
    def copy_skin_in_hierarchy(self, *args):
        self.sh.copy_skin_in_hierarchy()
    
        
        