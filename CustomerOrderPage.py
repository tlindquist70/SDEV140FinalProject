from tkinter import *
from PIL import ImageTk, Image
import os


# create a class
class CustomerOrder:
    """A container for the customer ordercode
    Displays name of flowers, number of seed packets and total for each flower type plus a total order for each customer"""
    
    
    def __init__(self, frame, oncomplete, app_settings):
        self.oncomplete = oncomplete
        self.frame = frame
        self.app_settings = app_settings
        self.price_dictionary = {}

    def show(self,flower, quantity_list):
        self.flower = flower
        self.quantity = quantity_list
        self.price_dictionary["swamp_milkweed_50"] = {"name": "Swamp Milkweed 50 seed packet", "price": 5.95}
        self.price_dictionary["swamp_milkweed_100"] = {"name": "Swamp Milkweed 100 seed packet", "price": 11.50}
        self.price_dictionary["cardinalflower_50"] = {"name": "Cardinalflower 50 seed packet", "price": 5.95}
        self.price_dictionary["cardinalflower_100"] = {"name": "Cardinalflower 100 seed packet", "price": 11.50}
        self.price_dictionary["yellow_alexander_50"] = {"name": "Yellow Alexander 50 seed packet", "price": 5.95}
        self.price_dictionary["yellow_alexander_100"] = {"name": "Yellow Alexander 100 seed packet", "price": 11.50}
        self.price_dictionary["yellow_coneflower_50"] = {"name": "Yellow Coneflower 50 seed packet", "price": 5.95}
        self.price_dictionary["yellow_coneflower_100"] = {"name": "Yellow Coneflower 100 seed packet", "price": 11.50}
        self.price_dictionary["blue_bellflower_50"] = {"name": "Blue Bellflower 50 seed packet", "price": 5.95}
        self.price_dictionary["blue_bellflower_100"] = {"name": "Blue Bellflower 100 seed packet", "price": 11.50}
        self.price_dictionary["blue_delphinium_50"] = {"name": "Blue Delphinium 50 seed packet", "price": 5.95}
        self.price_dictionary["blue_delphinium_100"] = {"name": "Blue Delphinium 100 seed packet", "price": 11.50}
        self.price_dictionary["purple_aster_50"] = {"name": "Purple Aster 50 seed packet", "price": 5.95}
        self.price_dictionary["purple_aster_100"] = {"name": "Purple Aster 100 seed packet", "price": 11.50}
        self.price_dictionary["purple_ironweed_50"] = {"name": "Purple Ironweed 50 seed packet", "price": 5.95}
        self.price_dictionary["purple_ironweed_100"] = {"name": "Purple Ironweed 100 seed packet", "price": 11.50}
        finish_button = Button(self.frame, text = "Add More",command = self.on_next_click)
        finish_button.grid(row = 3, column = 2)
        print(flower)
        print(quantity_list)
        row = 1
        for item in quantity_list: 
            print(self.price_dictionary[item]["name"])
            print(self.price_dictionary[item]["price"])
            label_flowername = Label(self.frame, text = self.price_dictionary[item]["name"])
            label_flowername.grid(row = row, column = 1)
            label_flowerprice = Label(self.frame, text = '${:,.2f}'.format(self.price_dictionary[item]["price"]))
            label_flowerprice.grid(row = row, column = 2)
            row += 1
            


    def on_next_click(self):
        """Logic to send color selection to main application"""
        """Used to send customer to page with flowers in selected color"""
        self.oncomplete()