# Header and description:
# M08_final project
# created: 2024-02-15 (tll)
# revised: 2024-03-07 (tll)
# 
# Create a simple grapihical user interface with at least two screens, two images, two lables, three buttons, and two callback funcrtions

# Pseudocode:
# This file contains Order Seeds class and associated methods.
# Selected color information is passed to this class from the Application when the "Order Seeds" button is clicked on the Home page. 
# Define and instantiate the class. Instantiation needs to include the app settings, the frame, a color dictionary, and a list of page elements and any additional formatting.
# Create an empty list to hold the screen elements to display.
# Create an empty dictionary for flower colors. 
# Use ImageTk and the os module to link to and import the flower images and create a variable for each image. 
# Append entries to the flower color dictionary. Each entry should be keyed on flower color and include the flower name, a picture, a label, and the seed packet values.
# The selected color data passed from the Home page is used to generate the screen elements to appended to the screen elements list.
# This page should display the following: The images of the flowers available in the selected color, a button to add a packet of 50 seeds to the customer's order, 
# a button to add a packet of 100 seeds to the customer's order, each button should also display the seed packet price. 
# When a seed packet selection is made, users should be sent to an order summary page.  


# Import TKInter and Image Tk
from tkinter import *
from PIL import ImageTk,Image

# import os to get full file paths
import os

# create class
class OrderSeeds:
    """A container for the code for the seed ordering pages"""

    def __init__(self, frame, oncomplete, app_settings):
        """Logic used to create an instance of the Order Seeds Page"""

        self.oncomplete = oncomplete
        self.frame = frame
        self.app_settings = app_settings
        self.selected_packet = StringVar()
        self.color_dictionary = {}
        self.page_elements = []

        #add fonts
        self.Font_tuple_2 = ("Segoe UI", 14)
        self.Font_tuple_3 = ("Papyrus", 14)
        

        # add image paths for flower images
        module_path = os.path.dirname(os.path.realpath(__file__))   
        milkweed_path_root = os.path.join(module_path, "swamp_milkweed.PNG")
        flower_img_milkweed = ImageTk.PhotoImage(Image.open(milkweed_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        cardinalflower_path_root = os.path.join(module_path, "cardinal_flower.PNG")
        flower_img_cardinalflower = ImageTk.PhotoImage(Image.open(cardinalflower_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        yellow_alexanders_path_root = os.path.join(module_path, "yellow_alexanders.PNG")
        flower_img_yellow_alexanders = ImageTk.PhotoImage(Image.open(yellow_alexanders_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        yellow_coneflower_path_root = os.path.join(module_path, "yellow_coneflower.PNG")
        flower_img_yellow_coneflower = ImageTk.PhotoImage(Image.open(yellow_coneflower_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        blue_bellflower_path_root = os.path.join(module_path, "blue_bellflower.PNG")
        flower_img_blue_bellflower = ImageTk.PhotoImage(Image.open(blue_bellflower_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        blue_delphinium_path_root = os.path.join(module_path, "blue_delphinium.PNG")
        flower_img_blue_delphinium = ImageTk.PhotoImage(Image.open(blue_delphinium_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        purple_aster_path_root = os.path.join(module_path, "purple_aster.PNG")
        flower_img_purple_aster = ImageTk.PhotoImage(Image.open(purple_aster_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        purple_ironweed_path_root = os.path.join(module_path,"purple_ironweed.PNG" )
        flower_img_purple_ironweed = ImageTk.PhotoImage(Image.open(purple_ironweed_path_root).resize(size = [260,260], resample = Image.Resampling.NEAREST))
        
        # create dictionary to hold seed ordering information
        self.color_dictionary["red"]= []
        self.color_dictionary["red"].append({
            "name": "Swamp Milkweed", 
            "picture": flower_img_milkweed, 
            "label": "flower_1_label", 
            "50_value": "swamp_milkweed_50",
            "100_value": "swamp_milkweed_100",
            })
        self.color_dictionary["red"].append({
            "name": "Cardinal Flower", 
            "picture": flower_img_cardinalflower, 
            "label": "flower_2_label",
            "50_value": "cardinalflower_50",
            "100_value": "cardinalflower_100",
            })
          
        self.color_dictionary["yellow"] = []
        self.color_dictionary["yellow"].append({
            "name": "Yellow Alexander",        
            "picture": flower_img_yellow_alexanders,
            "label": "flower_1_label",
            "50_value": "yellow_alexander_50",
            "100_value": "yellow_alexander_100",
            })
        
        self.color_dictionary["yellow"].append({
            "name": "Yellow Coneflower", 
            "picture": flower_img_yellow_coneflower,
            "label": "flower_2_label",
            "50_value": "yellow_coneflower_50",
            "100_value": "yellow_coneflower_100",
            })
        
        self.color_dictionary["blue"] = []
        self.color_dictionary["blue"].append({
            "name": "Bellflower", 
            "picture":flower_img_blue_bellflower,
            "label": "flower_1_label",
            "50_value": "blue_bellflower_50",
            "100_value": "blue_bellflower_100",
            })
        
        self.color_dictionary["blue"].append ({
            "name": "Blue Delphinium", 
            "picture": flower_img_blue_delphinium,
            "label": "flower_2_label",
            "50_value": "blue_delphinium_50",
            "100_value": "blue_delphinium_100",
            })
    
        self.color_dictionary["purple"] = []
        self.color_dictionary["purple"].append({
            "name": "Purple Aster", 
            "picture": flower_img_purple_aster,
            "label": "flower_1_label",
            "50_value": "purple_aster_50",
            "100_value": "purple_aster_100",
            })
        
        self.color_dictionary["purple"].append({
            "name": "Ironweed", 
            "picture": flower_img_purple_ironweed,
            "label": "flower_2_label",
            "50_value": "purple_ironweed_50",
            "100_value": "purple_ironweed_100",
            })
    

    # create a method to get selected flower data 
    def on_flower_select(self, flower, quantity):
        """Logic to send seed packet selections to main application"""
        """Used to create order and order total on order summary page"""

        self.oncomplete(flower, quantity)

    # create a method to show all screen elements for selected color
    def show(self, selected_color):
        """Logic to add elements to screen and display the screen"""

        self.selected_color = selected_color.lower()
        column = 1  

        # remove screen elements when user moves away from screen    
        for item in self.page_elements:
            item.destroy()
            
        # create empty list to hold images, flower names, and seed packet sizes and prices
        self.page_elements = [] 

        # create a loop to display images and seed packet prices for flowers in the selected color    
        for item in self.color_dictionary[self.selected_color]:
            
            flower_label = Label(self.frame, image = item["picture"])
            flower_label.grid(row = 1, column = column, padx = 20)
            flower_name = Label(self.frame, text = item["name"], font = self.Font_tuple_3, background = self.app_settings["app_background"])
            flower_name.grid(column= column, row= 2)
            small_packet = Button(self.frame, text = "50 seeds $5.95", font= self.Font_tuple_2, command = lambda name= item["name"],value=item["50_value"]: self.on_flower_select(name, value) )
            large_packet = Button(self.frame, text = "100 seeds $11.50", font = self.Font_tuple_2, command = lambda name = item["name"], value = item["100_value"]: self.on_flower_select(name, value))
            small_packet.grid (column = column, row = 3, pady = 15)
            large_packet.grid (column = column, row = 4, pady=15)
            column += 1
            self.page_elements.append(flower_label)
            self.page_elements.append(flower_name)
            self.page_elements.append(small_packet)
            self.page_elements.append(large_packet)

            # Unit testing to make sure seed packet information is getting passed to application as expected
            # print(self.color_dictionary[item]["name"])
            # print(self.price_dictionary[item]["value"])



        # add view order button
        """Used to send customers to order page to view their order totals"""
        next_button = Button(self.frame, text = "View Order",command = self.on_flower_select)
        next_button.grid(row = 8, column = 3, columnspan = 3)
        self.page_elements.append(next_button)
       


