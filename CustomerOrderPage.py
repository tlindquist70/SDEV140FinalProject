# Header and description:
# M08_final project
# created: 2024-02-15 (tll)
# revised: 2024-03-07 (tll)
# 
# Create a simple grapihical user interface with at least two screens, two images, two lables, three buttons, and two callback funcrtions

# Pseudocode:
# This file contains Customer Order class and associated methods.
# Define and instantiate the class. Instantiation needs to include the app settings, the frame, a price dictionary, and a list of page elements and any additional formatting.
# Create the method used to close the GUI.
# Create an empty list to hold the screen elements to display.
# Create a price dictionary to hold flower names, seed packet sizes, and associated prices using data passed from the application code.  
# Seed order details are passed to this class from the Application.  The elements passed should be appended to the screen elements list.
# This page should display the following: The name of each selected flower and seed packet size, the seed packet price, an order total
# a button that allows users to return to the home page to order additional flowers, and a button to close the application. 

# import TK inter  and Image Tk
from tkinter import *
from PIL import ImageTk, Image


# create a class
class CustomerOrder:
    """A container for the customer ordercode
    Displays name of flowers, number of seed packets and total for each flower type plus a total order for each customer"""
    
    # instantiate the class
    def __init__(self, frame, oncomplete, on_quit, app_settings):
        """Logic used to create an instance of the Customer Order Page"""

        self.oncomplete = oncomplete
        self.onquit = on_quit
        self.frame = frame
        self.app_settings = app_settings
        self.price_dictionary = {}
        self.page_elements = []
        #add fonts to this class
        self.Font_tuple_2 = ("Segoe UI", 14)

    # define the method used to close the GUI    
    def close_application(self):
        """Logic used to close the application when user clicks the Close Application button"""
        self.onquit()
       
    # define the method used to show the screen elements
    def show(self,flower, quantity_list):
        """Logic to build the elements that will display on the Customer Order Page"""
        
       # remove screen elements when user moves away from screen 
        for item in self.page_elements:
            item.destroy()
            
        # create an empty list to hold the name and price of each seed packet ordered, as well as the order total button and running total of the full
        # customer order
            
        self.page_elements = []

        # add seed packet names and prices to price dictionary
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

        # Unit testing to be sure flower and quantity are being passed to the application class successfully        
        #print(flower)
        #print(quantity_list)

        
        # set row number to align page elements
        row = 1

        # set initial order amount to 0
        order_sum = 0

        # create loop to add selected seed packets and prices to order page and calcualte and display totals
           
        for item in quantity_list: 
            # Unit testing to make sure seed packet information is getting passed to the loop as expected
            # print(self.price_dictionary[item]["name"])
            # print(self.price_dictionary[item]["price"])
            label_flowername = Label(self.frame, text = self.price_dictionary[item]["name"],font = self.Font_tuple_2, background = self.app_settings["app_background"])
            label_flowername.grid(row = row, column = 1, sticky = W )
            
            label_flowerprice = Label(self.frame, text = '${:,.2f}'.format(self.price_dictionary[item]["price"]),font = self.Font_tuple_2,background = self.app_settings["app_background"])
            label_flowerprice.grid(row = row, column = 2, sticky = E)
            row = row + 1
            order_sum = order_sum + self.price_dictionary[item]["price"] 
            self.page_elements.append(label_flowername)
            self.page_elements.append(label_flowerprice)

        # create the order total label
        label_ordertotal = Label(self.frame, text = "Order Total", font = self.Font_tuple_2, padx = 15,background = self.app_settings["app_background"])
        label_ordertotal.grid(row = row + 1, column  = 1, sticky = E)
        
        # display the order total         
        label_order_sum = Label(self.frame, text = ('${:,.2f}'.format(order_sum)), font = self.Font_tuple_2,background = self.app_settings["app_background"])
        label_order_sum.grid(row = row + 1, column = 3, sticky = E)              

        # add all generated elements to the Customer Order page to display    
        self.page_elements.append(label_ordertotal)
        self.page_elements.append(label_order_sum)
           

             
        # create button that allows users to return to application home page and add more seeds to their order 
        finish_button = Button(self.frame, text = "Add More",font = self.Font_tuple_2, command = self.on_next_click)
        finish_button.grid(row = row + 2, column = 2)      
        self.page_elements.append(finish_button)

        # create a button that allows users to exit the application
        exit_button = Button(self.frame, text = "Close Application",font = self.Font_tuple_2, command = self.close_application)
        exit_button.grid(row = row + 3, column = 2)      
        self.page_elements.append(exit_button) 
           

    # define the method used to return user to the home page
    def on_next_click(self):
        """Returns user to Home page to select additional flowers"""
       
        self.oncomplete()
        