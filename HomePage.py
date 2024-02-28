from tkinter import *
from PIL import ImageTk,Image
import os

# create a class
class Homepage:
    """A container for the homepage code"""

    
    def __init__(self, frame, oncomplete, app_settings):
        """Instantiate Homepage class"""
        self.oncomplete = oncomplete
        self.frame = frame
        self.app_settings = app_settings
        self.selected_color = StringVar()
        self.selected_color.set("Red")
        self.Font_tuple_2 = ("Segoe UI", 14)
        
    # create labels and values for radio buttons
        self.COLORS = [
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Yellow", "Yellow"),
        ("Purple", "Purple"),
        ]

    def on_next_click(self):
        """Logic to send color selection to main application"""
        """Used to send customer to page with flowers in selected color"""
        self.oncomplete(self.selected_color.get())

    def show(self):
        """Logic to add elements to screen and display the screen"""
        # import images
        module_path = os.path.dirname(os.path.realpath(__file__))
        input_path_root = os.path.join(module_path, "MaineStateMap.PNG")

        # add image
        global home_img
        home_img = ImageTk.PhotoImage(Image.open(input_path_root).resize(size = [350,350], resample = Image.Resampling.NEAREST))
        home_label = Label(self.frame, image = home_img)
        home_label.grid(row = 1, column = 0, rowspan = 6, columnspan = 3)


        #radiobutton label]
        radiobutton_label = Label(self.frame, text = "Select a Flower Color:", font = self.Font_tuple_2, background = self.app_settings["app_background"])
        radiobutton_label.grid(row = 1, column = 3)


        # create radio buttons
        row = 2
        for text, color in self.COLORS: 
            Radiobutton(self.frame, text = text, font = self.Font_tuple_2, variable = self.selected_color, value = color, background = self.app_settings["app_background"], borderwidth = 0).grid(row = row, column = 3, padx = 15)
            row += 1
        
        # add close button
        next_button = Button(self.frame, text = "Order Seeds", font = self.Font_tuple_2, command = self.on_next_click)
        next_button.grid(row = 6, column = 3, columnspan = 3)
       

   

    def destroy(self):
        """Logic to close screen when user moves away from screen"""



