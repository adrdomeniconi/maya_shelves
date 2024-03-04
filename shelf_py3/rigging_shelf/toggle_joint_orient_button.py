import maya.cmds as cmds
from shelf_button import ShelfButton
from shelf_button import MenuItem

import joint_helpers as joint_helpers

class ToggleJointOrientButton(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, button_click=ShelfButton.RIGHT_CLICK, icon="orientation", icon_only=True)
        
        self._joint_helpers = joint_helpers
        
        self.add_menu_items([
            MenuItem("Toggle joint orientation on hierarchy", command=self.toggle_visibility_on_hierarchy),
            MenuItem("Toggle joint orientation on selected", command=self.toggle_visibility_on_selected)
        ]) 
        
    def single_click(self):
        self.toggle_visibility_on_hierarchy(False)
        
    def toggle_visibility_on_selected(self, p):
        self._joint_helpers.toggle_axis_visibility_on_selected()
        
    def toggle_visibility_on_hierarchy(self, p):
        self._joint_helpers.toggle_axis_visibility_on_hierarchy()

        
        