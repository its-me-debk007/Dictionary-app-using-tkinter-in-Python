import requests
from tkinter import *
from PIL import Image,ImageTk


window=Tk()
window.title("Dictionary")
window.iconbitmap("icon.ico")
window.configure(bg= "black")
window.geometry("700x440")
window.resizable(False, False)

img=ImageTk.PhotoImage(Image.open("image.jpg"))
Label(window,image=img).pack(side= RIGHT)

e=Entry(window,fg="black",bg="ivory3",font="Comic 18",width=20, borderwidth= 2)
e.pack(side= TOP, anchor= NW, padx= 15, pady= 20)

meaning = Label(window, text = "Meaning of the word will appear here", wraplength = 400, fg = "white", bg = "black", font = "Helvetica 17", justify = "left", width= 45, height= 14)
meaning.pack(side= LEFT, anchor= NW, padx= 15, pady= 20)


def click():
    word = e.get().strip()
    e.delete(0,END)
    global meaning

    if word== "":
        meaning.config(text= "Please enter a word!")

    else:
        base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        data = requests.get(base_url + word).json()

        try:
            ans = data[0]["meanings"][0]["definitions"][0]["definition"]
            meaning.config(text = ans)

        except:
            meaning.config(text= "There was an error! Please make sure that the spelling is correct")

search = ImageTk.PhotoImage(Image.open("searchIcon.jpg"))
Button(window, image = search, command = click).place(x= 290, y= 21)


window.bind("<Return>",lambda event=None: click() )



window.mainloop()
