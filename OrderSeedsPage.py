from tkinter import *
from PIL import ImageTk,Image
import os

# create a class
class OrderSeeds:
    """A container for the code for the seed ordering pages"""

    def __init__(self, frame, oncomplete, app_settings):
        """Instantiate Homepage class"""
        self.oncomplete = oncomplete
        self.frame = frame
        self.app_settings = app_settings
        self.selected_packet = StringVar()
        self.color_dictionary = {}
        self.Font_tuple_2 = ("Segoe UI", 14)
        self.Font_tuple_3 = ("Papyrus", 14)
        # how does this page know what color was selected on the homepage?
        #global flower_img_milkweed
        ##global flower_img_cardinalflower
        #global flower_img_yellow_alexanders
        #global flower_img_yellow_coneflower
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
        
        # create dictionary to hold images.
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
            "100_value": "yellow_flower_100",
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
    
        # to call:  label = Label(self.frame, image = "color name"[loc. in array])
     
    def on_flower_select(self, flower, quantity):
        """Logic to send seed packet selections to main application"""
        """Used to create order and order total on order summary page"""
        self.oncomplete(flower, quantity)

    def show(self, selected_color):
        """Logic to add elements to screen and display the screen"""
        self.selected_color = selected_color.lower()
        column = 1  
         
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


        # add view order button
        """Used to send customers to order page to view their order totals"""
        next_button = Button(self.frame, text = "View Order",command = self.on_flower_select)
        next_button.grid(row = 8, column = 3, columnspan = 3)
       

   

    def destroy(self):
        """Logic to close screen when user moves away from screen"""



