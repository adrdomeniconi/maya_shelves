import maya.cmds as cmds
from shelf.button import ShelfButton
from shelf.button import MenuItem

import ik_helper as ik

class IkHelperBtn(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, button_click=ShelfButton.RIGHT_CLICK, icon="ik", icon_only=True)
        
        self.add_menu_items([
            MenuItem("Create PV", command=self.create_pv)
        ]) 
        
    def single_click(self, *args):
        self.create_pv()
        
    def create_pv(self, *args):
        ik.create_pv()
    
        
        