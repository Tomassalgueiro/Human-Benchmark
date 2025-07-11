import tkinter
import customtkinter
#import reaction
import re

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app settings
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Super Human Reaction")
app.resizable(False,False)
app.attributes("-topmost", True)

color_picker = ''
error_text = None

def validate_input_rgb(new_value):
    if new_value == "":
        return True
    if new_value.isdigit():
        if int(new_value) >= 0 and int(new_value) <= 255:
            return True
    print("Wrong Input Somewhere")
    return False
    
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


vrgb = app.register(validate_input_rgb)
vhex = app.register(validate_input_hex)
#function to block the editing of RGB and HEX Code
#basically just makes it so that there is no problem when running the program
def radiobutton_event():
    var = radio_var_color.get()
    match var:
        case "RGB":
            print("Enabling RGB buttons")
            color_picker="RBG"
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
            color_picker="HEX"
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

#button selector for color mode
radio_var_color = tkinter.StringVar(value="Nothing Selected")
#hard coding the position because its not an app that big



#RBG Colors inserter
frame_rgb = customtkinter.CTkFrame(app, fg_color="#242424", border_width=1, border_color="#D4D4D4")
frame_rgb.pack(padx=10,pady=(30,10),anchor="w")

radio_color_RGB = customtkinter.CTkRadioButton(frame_rgb, text="RBG",command=radiobutton_event, variable= radio_var_color, value="RGB")
radio_color_RGB.pack(padx=10,pady=10,side="left")

red_text = customtkinter.CTkLabel(frame_rgb, text="R")
red_text.pack(side="left",padx=(5,0))
red_rgb_entry = customtkinter.CTkEntry(frame_rgb, placeholder_text="RED", width=60)
red_rgb_entry.pack(side="left", padx=5, pady=5)
red_rgb_entry._entry.configure(validate="focusout", validatecommand=(vrgb, "%P"))

green_text = customtkinter.CTkLabel(frame_rgb, text="G")
green_text.pack(side="left",padx=(5,0))
green_rgb_entry = customtkinter.CTkEntry(frame_rgb, placeholder_text="GREEN", width=60)
green_rgb_entry.pack(side="left", padx=5, pady=5)
green_rgb_entry._entry.configure(validate="focusout", validatecommand=(vrgb, "%P"))

blue_text = customtkinter.CTkLabel(frame_rgb, text="B")
blue_text.pack(side="left",padx=(5,0))
blue_rgb_entry = customtkinter.CTkEntry(frame_rgb, placeholder_text="BLUE", width=60)
blue_rgb_entry.pack(side="left", padx=5, pady=5)
blue_rgb_entry._entry.configure(validate="focusout", validatecommand=(vrgb, "%P"))

#hex colors inserter
frame_hex = customtkinter.CTkFrame(app, fg_color="#242424", border_width=1, border_color="#D4D4D4")
frame_hex.pack(padx=10,pady=(1,10),anchor="w")


radio_color_HEX = customtkinter.CTkRadioButton(frame_hex, text="Hex Code",command=radiobutton_event, variable= radio_var_color, value="HEX")
radio_color_HEX.pack(padx=10,pady=4, side="left")

hex_text = customtkinter.CTkLabel(frame_hex, text="HEX  #")
hex_text.pack(side="left",padx=(5,0))
hex_entry = customtkinter.CTkEntry(frame_hex, placeholder_text="CODE", width=60)
hex_entry.pack(side="left", padx=5, pady=5)
hex_entry._entry.configure(validate="focusout", validatecommand=(vhex, "%P"))

#pixel selection, either manual (insert x and y) or automatic (press button select pixel and it gets the pos automatically)


# Run app Loop
disable_elements()
app.mainloop()
