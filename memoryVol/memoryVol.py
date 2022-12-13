from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import tkinter as tk
import time
import sys
import subprocess
import threading 
from tkinter import ttk
import tkinter
import os
import tkinter.messagebox
import customtkinter
from tkinter import filedialog
import hashlib
import json 
#from Open_Func import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar


Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='memoryVol', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Game Of Squids", 40, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))

for i in range(5): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520


    def __init__(self):
        super().__init__()


        self.title("memoryVol")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed


        def open_1():
            #global file_name
            filename = filedialog.askopenfilename(initialdir="/", title="Select A File",filetypes=(("bin files", "*.bin"),("raw files", "*.raw"), ("bmp files", "*.bmp"), ("mem files", "*.mem"),("vmem files", "*.vmem"),("all files", "*.*")))
            file_path = os.path.abspath(filename)


            with open("Loc.json", "w") as outfile:
                json.dump(file_path, outfile)
        

        def imageinfofunc():
            with open('Loc.json', 'r') as openfile:
                    # Reading from json file
                    filepath = json.load(openfile)
            print("Thread: start")
           # filepath = "mem1.vmem"

                                                                                                                                                      
            val = "volatility.exe -f "+filepath+" imageinfo"
                    # executes the value of val variable
            os.system(val)



        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)    #empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)      #empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    #empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)   #empty row with minsize as spacing


        # ======================================== profile Save operation function =============================================================
        def get_profile():
            global Prof
            Prof = self.profile.get()
            print (Prof)

        #========================================= Plugin Executtion process function ==========================================================
        def plugins_selection():
            with open('Loc.json', 'r') as openfile:
                 # Reading from json file
                filepath = json.load(openfile)

            text = clicked.get()
            #print ("12345")
            if text == "kdbgscan":
                print (text)
                query = "volatility.exe -f "+filepath+" "+text+ " "
                os.system(query)

            elif text == "pslist":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "psscan":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)
            elif text == "dlllist":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "dlldump":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "handles":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "netscan":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "hivelist":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "timeliner":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "hashDump":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "lsadump":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "modscan":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "filescan":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "svcscan":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "cmdscan":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "iehistory":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "dumpregistry":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "moddump":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "procdump":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)

            elif text == "memdump":
                print (text)
                query = "volatility.exe -f "+filepath+" --profile="+Prof+" "+text+ " "
                os.system(query)


        #===================================== Add File Button ======================================================================

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,text="add file", fg_color="green",text_color="#ffffff", command=open_1)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)


        #===================================== Remove File Button ===================================================================
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="remove file",
                                                command=self.button_event, 
                                                fg_color="red",
                                                text_color="#ffffff")
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        #===================================== generatet report =====================================================================

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="generate report",
                                                command=self.button_event, 
                                                fg_color="#004d00",
                                                text_color="#ffffff")
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        def open_hash():
            os.system('py Hash_generattor_GUI.py')

        self.hashbutton = customtkinter.CTkButton(master=self.frame_left,
                                                text="hash generator",
                                                fg_color="#004d00",
                                                text_color="#ffffff",command = open_hash)
        self.hashbutton.grid(row=4, column=0, pady=10, padx=20)


        #===================================== Run Button =====================================================================
        self.button_4 = customtkinter.CTkButton(master=self.frame_right,
                                                text="RUN",
                                                command=plugins_selection, 
                                                fg_color="#ff9900",
                                                text_color="#ffffff")
        self.button_4.grid(row=6, column=2, pady=10, padx=20)

        #=========================== Labal: Appearance Mode: "Light", "Dark", "System" =========================================

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        #=========================== Button: Appearance Mode: "Light", "Dark", "System" =========================================
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=10, pady=20, padx=20, sticky="nsew")

    

        #============= Text Box  =============

       # def button_click_event():
       #     dialog = customtkinter.CTkInputDialog( text="Search:", title="Search for a keyword")
       #     print("Number:", dialog.get_input())


#        self.button = customtkinter.CTkButton(master=self, text="Search for a keyword", command=button_click_event)
#        self.button.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

         
        # ============ frame_right ============

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,text="Imageinfo",fg_color="#ff9900",text_color="#ffffff",command=imageinfofunc)
        self.button_5.grid(row=0, column=2, pady=10, padx=20)


        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Select the architecture")
        


        self.profile = customtkinter.CTkEntry( master=self.frame_right,placeholder_text="Enter Profile",height=40)
        self.profile.grid(row=2, column=2, pady=5, padx=20, sticky="we")



        self.button_6 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Profile",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None  # <- no fg_color
                                                ,command=get_profile)
        self.button_6.grid(row=3, column=2, pady=5, padx=20, sticky="we")


        plugins=["kdbgscan", "pslist","psscan","dlllist","dlldump","handles","getsids","netscan","hivelist","timeliner","hashdump","lsadump","modscan","filescan","svcscan","cmdscan","iehistory","dumpregistry","moddump","procdump","memdump"]

        global clicked
        clicked = StringVar()
        clicked.set(plugins[0])
        self.combobox_1 = customtkinter.CTkOptionMenu(master=self.frame_right,variable=clicked, values = plugins)
        self.combobox_1.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")


        def custom_command():
            with open('Loc.json', 'r') as openfile:
                 # Reading from json file
                filepath = json.load(openfile)

            text = self.entry.get()
            print(text)
            #print (Prof)
            exe_com="volatility.exe -f "+filepath+" "+text+" "
            os.system(exe_com)

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Enter Custom Query")
        self.entry.grid(row=10, column=0, columnspan=2, pady=20, padx=20, sticky="we")




        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Execute the Query",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=custom_command)
        self.button_5.grid(row=10, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")
        self.combobox_1.set("Type of Scan")

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

w.destroy()
w.mainloop()