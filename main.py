import tkinter
import customtkinter
import re
import threading
import pyautogui
import pyscreeze #this import is needed for pyautogui even tho its not used
import time

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app settings
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Super Human Reaction")
app.resizable(False,False)
app.attributes("-topmost", True)

#defined this with integeres because it works for some reason
color_picker = 0
error_text = None
running = False

def reaction_module(R,G,B,posx,posy):
    while running:
        if(pyautogui.pixelMatchesColor(posx, posy,(R,G,B), tolerance=10)== True):
            pyautogui.click(x=posx,y=posy)

def validate_input_rgb(new_value):
    if new_value == "":
        return True
    if new_value.isdigit():
        if int(new_value) >= 0 and int(new_value) <= 255:
            return True
    print("Wrong Input Somewhere")
    return False

vrgb = app.register(validate_input_rgb)


def validate_input_hex(new_value):
    if new_value == "":
        return True
    if len(new_value) != 6:
        print("Wrong input somewhere")
        return False
    elif re.match(new_value,r'^#?([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$') != None:
        return True
    else:
        return False

vhex = app.register(validate_input_hex)


#function to block the editing of RGB and HEX Code
#basically just makes it so that there is no problem when running the program
def radiobutton_event():
    global color_picker
    var = radio_var_color.get()
    match var:
        case "RGB":
            print("Enabling RGB buttons")
            color_picker=1
            for child in frame_rgb.winfo_children():
                try:
                    child.configure(state="normal")
                except:
                    pass
            for child in frame_hex.winfo_children():
                try:
                    if child != radio_color_HEX:
                        child.configure(state="disabled")
                except:
                    pass

        case "HEX":
            print("Disabling RGB buttons")
            color_picker=2
            for child in frame_rgb.winfo_children():
                try:
                    if child != radio_color_RGB:
                        child.configure(state="disabled")
                except:
                    pass
            for child in frame_hex.winfo_children():
                try:
                    child.configure(state="normal")
                except:
                    pass
            
#func to disable everything at start, used to prevent bugs (might join with other functions later, choose px for e.g.)
def disable_elements():
    for child in frame_rgb.winfo_children():
                try:
                    if child != radio_color_RGB:
                        child.configure(state="disabled")
                    
                except:
                    pass
    for child in frame_hex.winfo_children():
                try:
                    if child != radio_color_HEX:
                        child.configure(state="disabled")
                except:
                    pass



def start_reaction_module():
    global running
    if not running:
        running = True
        posx,posy = int(pixel_x_entry.get()),int(pixel_y_entry.get()) 
        if color_picker == 1:

            print("Starting on RGB mode")
            R,G,B = int(red_rgb_entry.get()), int(green_rgb_entry.get()), int(blue_rgb_entry.get())
            threading.Thread(target=reaction_module,args=(R,G,B,posx,posy),daemon=True).start()
        
        elif color_picker == 2:
            print("Ainda n fiz")

def stop_reaction_module():
    global running
    running = False
    print("stopped")


#button selector for color mode
radio_var_color = tkinter.StringVar(value="Nothing Selected")

#RBG Colors inserter
frame_rgb = customtkinter.CTkFrame(app, fg_color="#242424", border_width=1, border_color="#D4D4D4")
frame_rgb.pack(padx=10,pady=(30,10),anchor="w")

radio_color_RGB = customtkinter.CTkRadioButton(frame_rgb, text="RBG",command=radiobutton_event, variable=radio_var_color, value="RGB")
radio_color_RGB.pack(padx=10,pady=10,side="left")

red_text = customtkinter.CTkLabel(frame_rgb, text="R")
red_text.pack(side="left",padx=(5,0), pady=5)
red_rgb_entry = customtkinter.CTkEntry(frame_rgb, placeholder_text="RED", width=60)
red_rgb_entry.pack(side="left", padx=5, pady=5)
red_rgb_entry._entry.configure(validate="focusout", validatecommand=(vrgb, "%P"))

green_text = customtkinter.CTkLabel(frame_rgb, text="G")
green_text.pack(side="left",padx=(5,0), pady=5)
green_rgb_entry = customtkinter.CTkEntry(frame_rgb, placeholder_text="GREEN", width=60)
green_rgb_entry.pack(side="left", padx=5, pady=5)
green_rgb_entry._entry.configure(validate="focusout", validatecommand=(vrgb, "%P"))

blue_text = customtkinter.CTkLabel(frame_rgb, text="B")
blue_text.pack(side="left",padx=(5,0), pady=5)
blue_rgb_entry = customtkinter.CTkEntry(frame_rgb, placeholder_text="BLUE", width=60)
blue_rgb_entry.pack(side="left", padx=5, pady=5)
blue_rgb_entry._entry.configure(validate="focusout", validatecommand=(vrgb, "%P"))

#hex colors inserter
frame_hex = customtkinter.CTkFrame(app, fg_color="#242424", border_width=1, border_color="#D4D4D4")
frame_hex.pack(padx=10,pady=(1,10),anchor="w")


radio_color_HEX = customtkinter.CTkRadioButton(frame_hex, text="Hex Code",command=radiobutton_event, variable= radio_var_color, value="HEX")
radio_color_HEX.pack(padx=10,pady=4, side="left")

hex_text = customtkinter.CTkLabel(frame_hex, text="HEX  #")
hex_text.pack(side="left",padx=(5,0), pady=5)
hex_entry = customtkinter.CTkEntry(frame_hex, placeholder_text="CODE", width=60)
hex_entry.pack(side="left", padx=5, pady=5)
hex_entry._entry.configure(validate="focusout", validatecommand=(vhex, "%P"))

#pixel selection, either manual (insert x and y) or automatic (press button select pixel and it gets the pos automatically)
frame_manual_pixel_insertiion = customtkinter.CTkFrame(app, fg_color="#242424", border_width=1, border_color="#D4D4D4")
frame_manual_pixel_insertiion.pack(padx=10, pady=10, anchor="w")

pixel_x_text = customtkinter.CTkLabel(frame_manual_pixel_insertiion, text="X")
pixel_x_text.pack(side="left",padx=(5,0))
pixel_x_entry = customtkinter.CTkEntry(frame_manual_pixel_insertiion, placeholder_text="Pos X", width=60)
pixel_x_entry.pack(side="left",padx=5, pady=5)

pixel_y_text = customtkinter.CTkLabel(frame_manual_pixel_insertiion, text="Y")
pixel_y_text.pack(side="left",padx=(5,0))
pixel_y_entry = customtkinter.CTkEntry(frame_manual_pixel_insertiion, placeholder_text="Pos Y", width=60)
pixel_y_entry.pack(side="left", padx=5, pady=5)


#frame for start and stop
frame_start_stop = customtkinter.CTkFrame(app,fg_color="#242424", border_width=1, border_color="#D4D4D4")
frame_start_stop.pack(pady=10, anchor="s")

start_button = customtkinter.CTkButton(frame_start_stop, text="START",text_color="#FFFFFF",fg_color="#00DD00",hover_color="#005500",command=start_reaction_module)
start_button.pack(side="left",padx=5,pady=5)
stop_button = customtkinter.CTkButton(frame_start_stop, text="STOP",text_color="#FFFFFF",fg_color="#DD0000",hover_color="#550000",command=stop_reaction_module)
stop_button.pack(side="left",padx=5,pady=5)

# Run app Loop
disable_elements()
app.mainloop()
