from tkinter import *

from PIL import ImageTk,Image 
from tkinter import messagebox
root=Tk()
root.title("country flags")
root.configure(background="teal")
root.geometry("600x600")
india_flag=ImageTk.PhotoImage(Image.open("india.png"))
korea_flag=ImageTk.PhotoImage(Image.open("korea.png"))
china_flag=ImageTk.PhotoImage(Image.open("china.png"))
flag_dictionary={"india":india_flag,"korea":korea_flag,"china":china_flag}
get_input=Entry(root)
get_input.place(relx=0.5,rely=0.2,anchor=CENTER)
label_img=Label(root)
label_img.place(relx=0.5,rely=0.5,anchor=CENTER)
def showflag():
    try:
        country_name=get_input.get()
        print(country_name)
        label_img["image"]=flag_dictionary[country_name]
    except:
        messagebox.showinfo("error","the country name you have entered is not there in the system")
button1=Button(root,text="show flag",command=showflag)
button1.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()
