import maya.cmds as cmds

class ShelfBase():
    
    ALL_SHELVES_PARENT_NAME = "ShelfLayout"
    
    def __init__(self, name="custom_shelf", default_icon_path=""):
        
        self.name = name
        self.default_icon_path = default_icon_path
        
        self.__reset_or_create_shelf()
        
        cmds.setParent(self.name)
    
    def __reset_or_create_shelf(self):
        if self.__shelf_exists():
            self.__clean_old_shelf()
        else:
            self.__create_empty_shelf()
    
    def __shelf_exists(self):
        return cmds.shelfLayout(self.name, exists=True)
    
    def __clean_old_shelf(self):
        if cmds.shelfLayout(self.name, query=True, numberOfChildren=True) > 0:
            for item in cmds.shelfLayout(self.name, query=True, childArray=True):
                cmds.deleteUI(item)
            
    def __create_empty_shelf(self):
        cmds.shelfLayout(self.name, parent=self.ALL_SHELVES_PARENT_NAME)
                
    def add_separator(self):
        cmds.separator(parent=self.name, style="shelf", horizontal=False)
                