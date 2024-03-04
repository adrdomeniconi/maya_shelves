import maya.cmds as cmds
from shelf_button import ShelfButton
from shelf_button import MenuItem

import offset_parent_matrix_helpers as opm

class OPMButton(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, button_click=ShelfButton.RIGHT_CLICK, icon="opm", icon_only=True)
        
        self.add_menu_items([
            
            MenuItem("Move transform to opm", command=self.transforms_to_opm_by_selection),
            MenuItem("Move transform to opm by hierarchy", command=self.transforms_to_opm_by_hierarchy),
            MenuItem("Move opm to transform", command=self.opm_to_transforms_by_selection),
            MenuItem("Move opm to transform by hierarchy", command=self.opm_to_transforms_by_hierarchy),
            
            MenuItem("", divider=True),
            MenuItem("Opm parent", command=self.opm_parent),
            MenuItem("Opm parent with offset", command=self.opm_parent_with_offset),
            
            MenuItem("", divider=True),
            MenuItem("Zero out opm", command=self.zero_out_opm),
            MenuItem("Zero out opm by hierarchy", command=self.zero_out_opm),
            MenuItem("Zero out opm keeping position", command=self.zero_out_opm_keeping_position),
            MenuItem("Zero out opm keeping position by hierarchy", command=self.zero_out_opm_keeping_position_by_hierarchy),
            MenuItem("Zero out transform and opm", command=self.zero_out_all),
            MenuItem("Zero out transform and opm by hierarchy", command=self.zero_out_all_by_hierarchy),
        ]) 
        
    def single_click(self):
        self.transforms_to_opm_by_selection()
        
    def transforms_to_opm_by_selection(self, *args):
        opm.transformations_to_offset_parent_matrix()
        
    def transforms_to_opm_by_hierarchy(self, *args):  
        opm.transformations_to_offset_parent_matrix(hierarchy = True)
    
    def opm_to_transforms_by_selection(self, *args):
        opm.offset_parent_matrix_to_transformations()
    
    def opm_to_transforms_by_hierarchy(self, *args):
        opm.offset_parent_matrix_to_transformations(hierarchy = True)
        
    def zero_out_opm(self, *args): 
        opm.zero_out_opm()
        
    def zero_out_opm(self, *args): 
        opm.zero_out_opm(hierarchy = True)
                
    def zero_out_opm_keeping_position(self, *args): 
        opm.zero_out_opm_keeping_position()
            
    def zero_out_opm_keeping_position_by_hierarchy(self, *args): 
        opm.zero_out_opm_keeping_position(hierarchy = True)
        
    def zero_out_all(self, *args): 
        opm.zero_out_all()
        
    def zero_out_all_by_hierarchy(self, *args): 
        opm.zero_out_all(hierarchy = True)
        
    def opm_parent(self, *args): 
        opm.offset_parent_matrix_parent()
        
    def opm_parent_with_offset(self, *args): 
        opm.offset_parent_matrix_parent_with_offset()