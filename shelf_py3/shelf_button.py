import maya.cmds as cmds

class MenuItem():
    def __init__(self, label, command = None, submenu_items = [], option_box = False, divider = False):
        self.label = label
        self.command = command
        self.submenu_items = submenu_items
        self.option_box = option_box
        self.divider = divider

class ShelfButton():
    
    LEFT_CLICK = 1
    MIDDLE_CLICK = 2
    RIGHT_CLICK = 3
    
    def __init__(self, label="", double_click_enabled=False, button_click=LEFT_CLICK, iconPath="", icon="", icon_only=False):
        
        self.__label = label
        self.__button_click = button_click
        self.__double_click_enabled = double_click_enabled
        self.__icon = icon
        self.__icon_path = iconPath
        self.__icon_only = icon_only
        self.__menu_items = []
        self.__label_background = (0, 0, 0, 0)
        self.__label_colour = (.9, .9, .9)
        self.__default_icon = "commandButton"
        
    def single_click(self):
        print("SingleClick from ShelfButton class.")
        
    def double_click(self):
        print("DoubleClick from ShelfButton class.")
        
    def add_menu_items(self, menu_items):
        self.__menu_items = menu_items
        
    def add_to_shelf(self, shelf):

        cmds.setParent(shelf.name)

        icon_full_path = self.__get_icon_full_path(shelf)
        style = self.__get_style()
        no_default_popup = self.__button_click == ShelfButton.RIGHT_CLICK
        
        if self.__double_click_enabled:
            cmds.shelfButton(width=37, 
                            height=37, 
                            image=icon_full_path, 
                            label=self.__label, 
                            command=self.single_click,
                            doubleClickCommand=self.double_click, 
                            imageOverlayLabel=self.__label, 
                            overlayLabelBackColor=self.__label_background,
                            overlayLabelColor=self.__label_colour,
                            preventOverride = False,
                            noDefaultPopup = no_default_popup,
                            style=style,
                            flat = True,
                            annotation=self.__label)
        else:
            cmds.shelfButton(width=37, 
                            height=37, 
                            image=icon_full_path, 
                            label=self.__label, 
                            command=self.single_click,
                            imageOverlayLabel=self.__label, 
                            overlayLabelBackColor=self.__label_background,
                            overlayLabelColor=self.__label_colour,
                            preventOverride = False,
                            noDefaultPopup = no_default_popup,
                            style=style,
                            flat = True,
                            annotation=self.__label)
                            
        if self.__menu_items:
            self.__create_menu()

    def __create_menu(self):
        popup_menu = cmds.popupMenu(button=self.__button_click)
        for menu_item in self.__menu_items:
            if menu_item.submenu_items:
                created_menu_item = cmds.menuItem(parent=popup_menu, label=menu_item.label, subMenu=True)
                for submenu_item in menu_item.submenu_items:
                    cmds.menuItem(parent=created_menu_item, label=submenu_item.label, command=submenu_item.command)
            elif menu_item.divider:
                cmds.menuItem(divider=True)    
            else:
                cmds.menuItem(parent=popup_menu, label=menu_item.label, command=menu_item.command, optionBox=menu_item.option_box)

    def __get_style(self):
        style = "iconAndTextHorizontal"
        if self.__icon_only:
            style = "iconOnly"
        return style

    def __get_icon_full_path(self, shelf):

        icon_full_path = ""
        icon_path = ""
        
        if self.__icon_path:
            icon_path = self.__icon_path
        else:
            icon_path = shelf.default_icon_path

        if self.__icon:
            icon_full_path = icon_path + "\\" + self.__icon
        else:
            icon_full_path = icon_path + self.__default_icon
        icon_full_path += ".png"

        return icon_full_path
        
        