import maya.cmds as cmds
from button import ShelfButton
from button import MenuItem

import group_helpers as gh

class GroupHelperBtn(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, button_click=ShelfButton.RIGHT_CLICK, icon="groups", icon_only=True)
        
        self.add_menu_items([
            MenuItem("Create parent groups", command=self.create_group_parent),
            MenuItem("Create child group", command=self.create_child_group)
        ]) 
        
    def single_click(self, *args):
        self.create_group_parent()
    
    def create_group_parent(self, *args):
        gh.create_group_parent_by_selection()
    
    def create_child_group(self, *args):
        gh.create_child_group()
        
    
        
        