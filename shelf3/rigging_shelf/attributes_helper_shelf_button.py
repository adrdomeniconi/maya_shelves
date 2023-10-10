from shelf.button import ShelfButton
from shelf.button import MenuItem
import maya.cmds as cmds
import maya.OpenMaya as om

import attributes_helpers as ah

class AttributesHelperShelfButton(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, button_click=ShelfButton.RIGHT_CLICK, icon="attrs_cp", icon_only=True)
        
        from shelf.rigging_shelf.category_prompt_ui import CategoryPromptUI
        from shelf.rigging_shelf.divider_prompt_ui import DividerPromptUI
        
        self.__category_ui = CategoryPromptUI(callback=self.create_category_callback)
        self.__divider_ui = DividerPromptUI(callback=self.create_divider_callback)
        self.add_menu_items([
            MenuItem("Copy attributes", command=lambda *atrs: ah.copy_selected()),
            MenuItem("Proxy attributes", command=lambda *atrs: ah.proxy_selected()),
            MenuItem("Lock and hide attributes", command=lambda *atrs: ah.lock_and_hide_all_attributes()),
            MenuItem("Restore default attributes", command=lambda *atrs: ah.restore_default_attributes_visibility()),
            MenuItem("Create category", command=lambda *atrs: self.__category_ui.show()),
            MenuItem("Create attribute divider", command=lambda *atrs: self.__divider_ui.show()),
        ]) 
        
    def single_click(self):
        ah.copy_selected()
    
    def create_category_callback(self, text):
        ah.create_category_by_selection(text)
        
    def create_divider_callback(self, text):
        ah.create_divider(text)
        
        