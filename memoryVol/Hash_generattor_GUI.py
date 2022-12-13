from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import filedialog
import os
import hashlib
import json 

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1024x480")
app.title("hash generator")
label = ttk.Label(app,text="Hello")
label.pack()

def button_callback():
    print("Button click")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

#frame_1.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",filetypes=(("exe files", "*.exe*"),("all files", "*.*")))


#Open File Button
def open_file():
    global file_name
    frame_1.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",filetypes=(("exe files", "*.exe*"),("all files", "*.*")))
    file_path = os.path.abspath(frame_1.filename)
    File_Location = Label(frame_1, text=str(file_path),width =100).grid(row=0, column=1,pady=10, padx=20)
    #def show_path():
    file_name = frame_1.filename
    #print (file_name)
    dictionary = file_name
 
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)
    


#with open('sample.json', 'r') as openfile:
    # Reading from json file
    #filepath = json.load(openfile)
#file_path=filepath

def hash_file_SHA1(filename1):
    """"This function returns the SHA-1 hash of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename1,'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

       # return the hex representation of digest
    return h.hexdigest()

def hash_file_MD5(filename):
    with open(filename,"rb") as f:
        bytes = f.read() # read file as bytes
        readable_hash = hashlib.md5(bytes).hexdigest();
        print(readable_hash)
        

def hash_file_SHA256(filename):
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)



#file_loc()
#print (filepath)


def print_hash(value):
    if value ==1:
        #Opening JSON file
        with open('sample.json', 'r') as openfile:
            # Reading from json file
            filepath = json.load(openfile)
        file_path=filepath

        hash_value_SHA1 = hash_file_SHA1(file_path)
        print(hash_value_SHA1)
        #label = frame_1.Label(app,text=hash_value_SHA1)
        #label.pack()


    elif value==2:
        #Opening JSON file
        with open('sample.json', 'r') as openfile:
            # Reading from json file
            filepath = json.load(openfile)
        file_path=filepath


        hash_value_SHA256 = hash_file_SHA256(file_path)
        print(hash_value_SHA256)
        #label = frame_1.Label(app,text=hash_value_SHA256)
        #label.pack()
    elif value==3:
        #Opening JSON file
        with open('sample.json', 'r') as openfile:
            # Reading from json file
            filepath = json.load(openfile)
        file_path=filepath

        hash_value_MD5 = hash_file_MD5(file_path)
        print(hash_value_MD5)
        #label = frame_1.Label(app,text=hash_value_MD5)
        #label.pack()
    #else:

#BUTTON TO OPEN A FILE
button_1 = customtkinter.CTkButton(master=frame_1,text="add file", fg_color="green",text_color="#ffffff", command=open_file)
button_1.grid(row=0, column=0,pady=10, padx=20)

#BUTTON TO RUN 
button_2 = customtkinter.CTkButton(master=frame_1,text="Generate Hash Value", fg_color="#ff1a1a",command=lambda:print_hash(radio_var.get()))
button_2.grid(row=1, column=0,pady=12, padx=10)


#BADIO BUTTONS FOR SELECTTING TTHE HASHING METTHOD
radio_var = tkinter.IntVar(value=0)

SHA_1 = customtkinter.CTkRadioButton(master=frame_1, text="SHA_1",variable= radio_var,value=1)
SHA_1.grid(row=2, column=0,pady=12, padx=10)

SHA_256 = customtkinter.CTkRadioButton(master=frame_1, text="SHA_256",variable= radio_var,value=2)
SHA_256.grid(row=3, column=0,pady=12, padx=10)

MD5 = customtkinter.CTkRadioButton(master=frame_1, text="MD5",variable= radio_var,value=3)
MD5.grid(row=4, column=0,pady=12, padx=10)


app.mainloop()
