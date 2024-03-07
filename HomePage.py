# Header and description:
# M08_final project
# created: 2024-02-15 (tll)
# revised: 2024-03-07 (tll)
# 
# Create a simple grapihical user interface with at least two screens, two images, two lables, three buttons, and two callback funcrtions

# Pseudocode:
# This file contains Home Page class and associated methods.
# Define and instantiate the class. Instantiation needs to include the app settings, the frame, a default value for the color radio buttons, and formatting. 
# Create a dictionary of color constants for the radio buttons. 
# Create an empty list to hold the screen elements to display.
# This page should display the following: A set of radio buttons for each available flower color, an image of a map of the state of ME, and an Order Seeds button.
# Create a method to get the user's color selection from the radio buttons. Selected color information should passed to the Application.
# When users click the Order Seeds button, users should be sent to the page displaying the flowers and seed packets available in their selected color. 


# Import TKInter and Image Tk
from tkinter import *
from PIL import ImageTk,Image

# import os to get full file paths
import os

# create class
class Homepage:
    """A container for the homepage code"""

    
    def __init__(self, frame, oncomplete, app_settings):
        """Logic used to create an instance of the Home Page"""

        self.oncomplete = oncomplete
        self.frame = frame
        self.app_settings = app_settings
        self.selected_color = StringVar()
        self.selected_color.set("Red")
        self.Font_tuple_2 = ("Segoe UI", 14)
        self.page_elements = []
        
        # create labels and values for radio buttons
        self.COLORS = [
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Yellow", "Yellow"),
        ("Purple", "Purple"),
        ]
    # create method to get color selection from the radio button selected by the user and send users to the next page in the GUI application
    def on_next_click(self):
        """Logic to send color selection to main application"""
        """Used to send customer to page with flowers in selected color"""

        self.oncomplete(self.selected_color.get())

    # create the method to display the screen elements
    def show(self):
        """Logic to add elements to Homepage screen and display the screen"""
        
        # remove screen elements when user moves away from screen  
        for item in self.page_elements:
            item.destroy()
            
        # create empty list of screen elements
        self.page_elements = []
        
        # import images
        module_path = os.path.dirname(os.path.realpath(__file__))
        input_path_root = os.path.join(module_path, "MaineStateMap.PNG")

        # add image to homepage frame
        global home_img
        home_img = ImageTk.PhotoImage(Image.open(input_path_root).resize(size = [350,350], resample = Image.Resampling.NEAREST))
        home_label = Label(self.frame, image = home_img)
        home_label.grid(row = 1, column = 0, rowspan = 6, columnspan = 3)
        self.page_elements.append(home_label)


        # create radiobutton label
        radiobutton_label = Label(self.frame, text = "Select a Flower Color:", font = self.Font_tuple_2, background = self.app_settings["app_background"])
        radiobutton_label.grid(row = 1, column = 3)
        self.page_elements.append(radiobutton_label)


        # create radio buttons to allow users to select flower colors
        row = 2
        for text, color in self.COLORS: 
            radiobutton = Radiobutton(self.frame, text = text, font = self.Font_tuple_2, variable = self.selected_color, value = color, background = self.app_settings["app_background"], borderwidth = 0)
            radiobutton.grid(row = row, column = 3, padx = 15)
            row += 1
            self.page_elements.append(radiobutton)
            
        
        # add close button
        next_button = Button(self.frame, text = "Order Seeds", font = self.Font_tuple_2, command = self.on_next_click)
        next_button.grid(row = 6, column = 3, columnspan = 3)
        self.page_elements.append(next_button)



