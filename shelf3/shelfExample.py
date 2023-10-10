import maya.cmds as cmds
import shelf.base 
import shelf.button

class ExampleShelf(ShelfBase):
    
    def __init__(self):
        ShelfBase.__init__(self, "Example_shelf")

class CustomSingleClickButton(ShelfButton):
    
    def __init__(self):
        ShelfButton.__init__(self, label="Single")
        
    def single_click(self):
        print("SingleClick from CustomSingleClickButton")
        
class CustomDoubleClickButton(ShelfButton):
    
    def __init__(self):
        ShelfButton.__init__(self, label="Double", double_click_enabled=True)
        
    def single_click(self):
        print("singleClick from CustomDoubleClickButton")
        
    def double_click(self):
        print("doubleClick from CustomDoubleClickButton")


class CustomMenuButton(ShelfButton):
    
    def __init__(self):
        ShelfButton.__init__(self, label="Menu", button_click=ShelfButton.LEFT_CLICK)
        
        self.add_menu_items([
            MenuItem("Menu Item 1", command=self.menu_item_1),
            MenuItem("Menu Item 2", submenu_items=[
                MenuItem("Submenu Item 1", command=self.menu_item_2_submenu_item_1),
                MenuItem("Submenu Item 2", command=self.menu_item_2_submenu_item_2),
            ]),
            MenuItem("Menu Item 3", command=self.menu_item_3)
        ])
    
    def menu_item_1(self, unknown):
        print("menu_item_1")
        
    def menu_item_3(self, unknown):
        print("menu_item_3")
        
    def menu_item_2_submenu_item_1(self, unknown):
        print("menu_item_2_submenu_item_1")
        
    def menu_item_2_submenu_item_2(self, unknown):
        print("menu_item_2_submenu_item_2")
        
class CustomActionMenuButton(ShelfButton):
    
    def __init__(self):
        ShelfButton.__init__(self, label="ActionMenu", button_click=ShelfButton.RIGHT_CLICK)
        
        self.add_menu_items([
            MenuItem("Menu Item 1", command=self.menu_item_1),
            MenuItem("Menu Item 2", submenu_items=[
                MenuItem("Submenu Item 1", command=self.menu_item_2_submenu_item_1),
                MenuItem("Submenu Item 2", command=self.menu_item_2_submenu_item_2),
            ]),
            MenuItem("Menu Item 3", command=self.menu_item_3)
        ])
    
    def single_click(self):
        print("singleClick from CustomActionMenuButton")
    
    def menu_item_1(self, unknown):
        print("menu_item_1")
        
    def menu_item_3(self, unknown):
        print("menu_item_3")
        
    def menu_item_2_submenu_item_1(self, unknown):
        print("menu_item_2_submenu_item_1")
        
    def menu_item_2_submenu_item_2(self, unknown):
        print("menu_item_2_submenu_item_2")
    

if __name__ == "__main__":
    exampleShelf = ExampleShelf()
    
    customSingleClickButton = CustomSingleClickButton()
    customSingleClickButton.add_to_shelf(exampleShelf)
    
    customDoubleClickButton = CustomDoubleClickButton()
    customDoubleClickButton.add_to_shelf(exampleShelf)
    
    customMenuButton = CustomMenuButton()
    customMenuButton.add_to_shelf(exampleShelf)
    
    customActionMenuButton = CustomActionMenuButton()
    customActionMenuButton.add_to_shelf(exampleShelf)
    
    exampleShelf.add_separator()
    
    customSingleClickButton.add_to_shelf(exampleShelf)
    customMenuButton.add_to_shelf(exampleShelf)