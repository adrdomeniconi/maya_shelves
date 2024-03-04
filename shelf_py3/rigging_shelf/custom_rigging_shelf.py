import os
from importlib import reload
from shelf_base import ShelfBase

from rigging_shelf.attributes_helper_shelf_button import AttributesHelperShelfButton
from rigging_shelf.joint_helper_button import JointHelperButton
from rigging_shelf.toggle_joint_orient_button import ToggleJointOrientButton
from rigging_shelf.opm_button import OPMButton
from rigging_shelf.locator_button import LocatorButton
from rigging_shelf.group_helper_btn import GroupHelperBtn
from rigging_shelf.skin_button import SkinButton

ICON_DIR = os.path.join(os.path.dirname(__file__), 'icons')

class CustomRiggingShelf(ShelfBase):
    
    def __init__(self):
        print("Loading rigging shelf...")
        ShelfBase.__init__(self, "Custom_rigging", ICON_DIR)
        self.create()
        self.add_items()
        print("Rigging Shelf loaded succesfuly!")
    
    def add_items(self):    
        AttributesHelperShelfButton().add_to_shelf(self)
        JointHelperButton().add_to_shelf(self)
        ToggleJointOrientButton().add_to_shelf(self)
        OPMButton().add_to_shelf(self)
        LocatorButton().add_to_shelf(self)
        GroupHelperBtn().add_to_shelf(self)
        SkinButton().add_to_shelf(self)
        