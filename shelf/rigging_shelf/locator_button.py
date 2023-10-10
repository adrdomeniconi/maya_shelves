import maya.cmds as cmds
from shelf.button import ShelfButton
from shelf.button import MenuItem

import locator_helpers as lh

class LocatorButton(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, button_click=ShelfButton.RIGHT_CLICK, icon="locator", icon_only=True)
        
        self.lh = lh
        self.cmds = cmds
        
        self.add_menu_items([
            MenuItem("Create locator at the center", command=self.create_locator_at_the_center),
            MenuItem("Create locator at selected points", command=self.create_locator_at_point),
            MenuItem("Create locator at selected points with rotations", command=self.create_locator_at_point_with_rotations),
            MenuItem("Create locator at origin", command=self.create_locator_at_origin)
        ]) 
    
    def single_click(self):
        self.lh.create_locator_based_on_selection()
        
    def create_locator_at_point(self, *args):
        self.lh.create_locator_at_point()
        
    def create_locator_at_point_with_rotations(self, *args):
        self.lh.create_locator_at_point(match_rotation=True)
        
    def create_locator_at_the_center(self, *args):
        self.lh.create_locator_at_the_center()
        
    def create_locator_at_origin(self, *args):
        self.cmds.spaceLocator()
        
    
        
        