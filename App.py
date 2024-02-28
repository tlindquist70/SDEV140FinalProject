from tkinter import *
from PIL import ImageTk,Image
import os
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

# create on complete functions
def homepage_oncomplete(selected_color):
    """Logic to call when user choice has been made on homepage"""
    print (f'{selected_color}')
    homepage_frame.destroy()
    #orderseeds_frame = LabelFrame(root, background = app_settings["app_background"], borderwidth = 0)
    #orderpage = OrderSeeds(orderseeds_frame, orderseeds_oncomplete, app_settings)
    orderpage.show(selected_color)
    orderseeds_frame.grid(row = 2, column = 0, columnspan = 6, pady = 0, sticky = EW)


def orderseeds_oncomplete(flower, quantity):
    """Logic to call when user choice has been made on order seeds page"""
    orderseeds_frame.destroy()
    item_array.append(quantity)
    customerorder.show(flower, item_array)
    customerorder_frame.grid(row = 2, column = 0, columnspan = 6, sticky = EW)
    #print (flower)
    #print(quantity)

def customerorder_oncomplete():
    customerorder_frame.destroy()
    homepage_frame = LabelFrame(root, background = app_settings["app_background"], borderwidth = 0)
    homepage = Homepage(homepage_frame, homepage_oncomplete, app_settings)
    homepage.show()
    homepage_frame.grid(row = 2, column = 0, columnspan = 6, pady = 0, sticky = EW)




#create screens
homepage = Homepage(homepage_frame, homepage_oncomplete, app_settings)
orderpage = OrderSeeds(orderseeds_frame, orderseeds_oncomplete, app_settings)
customerorder = CustomerOrder(customerorder_frame, customerorder_oncomplete, app_settings)

# create generic app label
app_label = Label(root, text = "Maine Native Plant Finder Tool:  Find Your Native Joy!", font= app_settings["header_font"], justify="left", background= app_settings["app_background"], borderwidth=0)
app_label.grid(row = 1, column = 0, columnspan = 6, sticky = W)



# display home screen elements
homepage.show()
homepage_frame.grid(row = 2, column = 0, columnspan = 6, pady = 0, sticky = EW)


#add things to the frame

# run GUI
root.mainloop()
