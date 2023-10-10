import maya.cmds as cmds
from shelf.button import ShelfButton
from shelf.button import MenuItem

import joint_helpers as jnt
import rigging_shelf.joint_creator_options_btn as jnt_creator_options
import rigging_shelf.joint_chain_from_locators_options as jnt_chain_from_loc_options
import rigging_shelf.joint_reposition_options as jnt_reposition_options

class JointHelperButton(ShelfButton):
    def __init__(self):
        ShelfButton.__init__(self, button_click=ShelfButton.RIGHT_CLICK, double_click_enabled=True, icon="kinInsert", icon_only=True)
        
        self._joint_creator_options = jnt_creator_options.JointCreatorOptions()
        self._jnt_chain_from_locations_options = jnt_chain_from_loc_options.JointChainFromLocatorsOptions()
        self._jnt_reposition_options = jnt_reposition_options.JointRepositionOptions()
        
        self.add_menu_items([
            MenuItem("Create at selected points", command=self.create_joint_at_point),
            MenuItem("Create under selected nodes", command=self.create_joint_under_selected_node),
            MenuItem("Create options", command=self.create_joint_at_point_options, option_box=True),
            MenuItem("Create joint hierarchy", command=self.create_joint_hierarchy),
            MenuItem("Clean tip joints by hierarchy", command=self.clean_tip_joints_orientations_by_hierarchy),
            MenuItem("Clean tip joints by selection", command=self.clean_tip_joints_orientations_by_selection),
            MenuItem("Create joints from locators on the same plane", command=self.create_joints_from_locators),
            MenuItem("Create joints from locators options", command=self.create_joints_from_locators_options, option_box=True),
            MenuItem("Reposition joints on the same plane", command=self.reposition_joints_from_locators),
            MenuItem("Reposition joints options", command=self.reposition_joints_from_locators_options, option_box=True),
            MenuItem("Joint tool", command=self.joint_tool)
        ]) 
        
    def single_click(self):
        self.create_joint_at_point(False)
        
    def double_click(self):
        self._joint_creator_options.show()
        
    def create_joint_at_point(self, p):
        jnt.create_joint_at_point()
        
    def create_joint_at_point_options(self, p):
        self._joint_creator_options.show()
        
    def create_joint_under_selected_node(self, p):
        jnt.create_joint_under_selected_node()
    
    def create_joint_hierarchy(self, *args):
        jnt.create_joint_hierarchy()
        
    def clean_tip_joints_orientations_by_hierarchy(self, *args):
        jnt.clean_tip_joints_orientations_by_hierarchy()
        
    def clean_tip_joints_orientations_by_selection(self, *args):
        jnt.clean_tip_joints_orientations_by_selection()
    
    def create_joints_from_locators(self, *args):
        self._jnt_chain_from_locations_options.show()
    
    def create_joints_from_locators_options(self, *args):
        self._jnt_chain_from_locations_options.show()
        
    def reposition_joints_from_locators(self, *args):
        self._jnt_reposition_options.show()
        
    def reposition_joints_from_locators_options(self, *args):
        self._jnt_reposition_options.show()
    
    def joint_tool(self, p):
        cmds.JointTool()
        
        