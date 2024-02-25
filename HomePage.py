from tkinter import *
from PIL import ImageTk,Image
import os

# create a class
class Homepage:
    """A container for the homepage code"""

    
    def __init__(self, frame, oncomplete, app_settings):
        """Initialize Homepage class"""
        self.oncomplete = oncomplete
        self.frame = frame
        self.app_settings = app_settings
        self.selected_color = StringVar()
        self.selected_color.set("Red")
    # create labels and values for radio buttons
        self.COLORS = [
        ("Red", "Red"),
        ("Orange", "Orange"),
        ("Yellow", "Yellow"),
        ("Purple", "Purple"),
        ]

    def on_next_click(self):
        self.oncomplete(self.selected_color.get())

    def show(self):
        """Logic to add elements to screen and display the screen"""
        # import images
        module_path = os.path.dirname(os.path.realpath(__file__))
        input_path_root = os.path.join(module_path, "MaineStateMap.PNG")

        # add image
        global home_img
        home_img = ImageTk.PhotoImage(Image.open(input_path_root).resize(size = [400,400], resample = Image.Resampling.NEAREST))
        home_label = Label(self.frame, image = home_img)
        home_label.grid(row = 1, column = 0, rowspan = 6, columnspan = 3)

        #radiobutton label
        radiobutton_label = Label(self.frame, text = "Select a color", background = self.app_settings["app_background"])
        radiobutton_label.grid(row = 1, column = 3)


        # create radio buttons
        row = 2
        for text, color in self.COLORS: 
            Radiobutton(self.frame, text = text, variable = self.selected_color, value = color, background = self.app_settings["app_background"], borderwidth = 0).grid(row = row, column = 3, padx = 15)
            row += 1
        
        # add close button
        next_button = Button(self.frame, text = "Order Seeds",command = self.on_next_click)
        next_button.grid(row = 6, column = 3, columnspan = 3)
       

   

    def destroy(self):
        """Logic to close screen when user moves away from screen"""



