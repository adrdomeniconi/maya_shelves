import os
from shelf.base import ShelfBase

from shelf.rigging_shelf.attributes_helper_shelf_button import AttributesHelperShelfButton
from shelf.rigging_shelf.joint_helper_shelf_button import JointHelperButton
from shelf.rigging_shelf.opm_button import OPMButton
from shelf.rigging_shelf.toggle_joint_orient_button import ToggleJointOrientButton
from shelf.rigging_shelf.locator_button import LocatorButton
from shelf.rigging_shelf.group_helper_btn import GroupHelperBtn
from shelf.rigging_shelf.skin_button import SkinButton
from shelf.rigging_shelf.ik_helper_btn import IkHelperBtn

ICON_DIR = os.path.join(os.path.dirname(__file__), 'icons')

class CustomRiggingShelf(ShelfBase):
    
    def __init__(self):
        ShelfBase.__init__(self, "Custom_rigging", ICON_DIR)
        self.build()
        print("Custom Rigging Shelf loaded succesfuly!")
    
    def build(self):    
        AttributesHelperShelfButton().add_to_shelf(self)
        JointHelperButton().add_to_shelf(self)
        ToggleJointOrientButton().add_to_shelf(self)
        OPMButton().add_to_shelf(self)
        LocatorButton().add_to_shelf(self)
        GroupHelperBtn().add_to_shelf(self)
        SkinButton().add_to_shelf(self)
        IkHelperBtn().add_to_shelf(self)
        