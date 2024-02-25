from tkinter import *
from PIL import ImageTk,Image
import os
from HomePage import Homepage

# create app variables
app_settings = {"app_background":"#b8cfd9"}

root = Tk()
root.title("ME Wildflower Finder")
root.geometry("600x500")
root.config(bg = app_settings["app_background"])


# create all frames
homepage_frame = LabelFrame(root, background = app_settings["app_background"], borderwidth = 0)


# create on complete functions
def homepage_oncomplete(selected_color):
    """Logic to call when user choice has been made on homepage"""
    print (f'{selected_color}')
    homepage_frame.destroy()
    
#create screens
homepage = Homepage(homepage_frame, homepage_oncomplete, app_settings)

# create generic app label
app_label = Label(root, text = "Maine Native Plant Finder Tool", justify="left", background= app_settings["app_background"], borderwidth=0)
app_label.grid(row = 1, column = 0, columnspan = 6, sticky = EW)

# display home screen elements
homepage.show()
homepage_frame.grid(row = 2, column = 0, columnspan = 6, pady = 0, sticky = EW)


#add things to the frame

# run GUI
root.mainloop()
