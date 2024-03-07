# Header and description:
# M08_final project
# created: 2024-02-15 (tll)
# revised: 2024-03-07 (tll)
# 
# Create a simple grapihical user interface with at least two screens, two images, two lables, three buttons, and two callback funcrtions

# Pseudocode:
# This file contains the applictions procedural code.
# The application communicates with the Home Page, Order Seeds Page, and Customer Order Page.
# Define the application variables, including GUI title, screen size, background color, fonts, and header.
# Create the fames for each page in the GUI.
# Define the on complete method for the homepage. This method hides the home page, and passses the selected color so that the correct Order Seeds Page 
# will display. 
# Define the on complete method for the Order Seeds Page. This method hides the order seeds page and passes the selected flower and seed packet quantity and price 
# to the order page.
# Define the on complete method for the Customer Order Page. This method hides the page when the Add More button is selected, but seed selections and price data
# are maintained so that the order total can be updated when user adds additional flowers to their order. 
# Define the method to close the application. 
# Write code to display each screen individually.
# Define the appliation label (this label appears on all pages) and display the home screen elements.
# Run the application.


# import TK inter
from tkinter import *

# import ImageTk
from PIL import ImageTk,Image

# import the classes created for each screen 
from OrderSeedsPage import OrderSeeds
from HomePage import Homepage
from CustomerOrderPage import CustomerOrder


# create app variables
app_settings = {"app_background":"#b8cfd9"}
item_array=[]

root = Tk()
root.title("ME Wildflower Finder")
root.geometry("600x500")
root.config(bg = app_settings["app_background"])
Font_tuple_1 = ("Gabriola", 20, "bold") 
app_settings["header_font"]=Font_tuple_1


# create all frames
homepage_frame = LabelFrame(root, background = app_settings["app_background"], borderwidth = 0)
orderseeds_frame = LabelFrame(root, background = app_settings["app_background"], borderwidth = 0)
customerorder_frame = LabelFrame(root, background = app_settings["app_background"], borderwidth = 0 )

# create on complete function for home page.  See pseudocode for function.
def homepage_oncomplete(selected_color):
    """Logic to send users to the Order Seeds Page after they have selected a flower color on the home page"""

    # unit testing to be sure selected color is passed appropriately from homepage to order seed page
    #print (f'{selected_color}')

    homepage_frame.grid_remove()
    orderpage.show(selected_color)
    orderseeds_frame.grid(row = 2, column = 0, columnspan = 6, pady = 0, sticky = EW)

# create on complete method for order seeds page.  See pseudocode for function. 
def orderseeds_oncomplete(flower, quantity):
    """Logic to send users to the Customer Order (Order Summary) page once they have selected seed packets on the order page"""
    orderseeds_frame.grid_remove()
    item_array.append(quantity)
    customerorder.show(flower, item_array)
    customerorder_frame.grid(row = 2, column = 0, columnspan = 6, sticky = EW)
    
    #Unit testing to be sure that the flower name and seed packet quantity are being passed to the order page as expected
    #print (flower)
    #print(quantity)

# create on complete method for customer order page.  See pseudocode for function. 
def customerorder_oncomplete():
    """Logic to return users back to the homepage if they click the Add More button on the customer order page"""
    customerorder_frame.grid_remove()
    homepage.show()
    homepage_frame.grid(row = 2, column = 0, columnspan = 6, pady = 0, sticky = EW)

# create method to close application
def exit_application():
    root.destroy()


#create each GUI screen
homepage = Homepage(homepage_frame, homepage_oncomplete, app_settings)
orderpage = OrderSeeds(orderseeds_frame, orderseeds_oncomplete, app_settings)
customerorder = CustomerOrder(customerorder_frame, customerorder_oncomplete, exit_application, app_settings)

# create generic app label that appears on every page
app_label = Label(root, text = "Maine Native Plant Finder Tool:  Find Your Native Joy!", font= app_settings["header_font"], justify="left", background= app_settings["app_background"], borderwidth=0)
app_label.grid(row = 1, column = 0, columnspan = 6, sticky = W)


# display home screen elements
homepage.show()
homepage_frame.grid(row = 2, column = 0, columnspan = 6, pady = 0, sticky = EW)


# run GUI
root.mainloop()
