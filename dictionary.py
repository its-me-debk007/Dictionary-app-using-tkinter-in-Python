import requests
from tkinter import *
from PIL import Image,ImageTk
from tkhtmlview import HTMLLabel
from PyDictionary import PyDictionary

window=Tk()
window.title("Dictionary")
window.iconbitmap("icon.ico")
window.configure(bg= "black")
window.geometry("920x385")
window.resizable(False, False)

img=ImageTk.PhotoImage(Image.open("galaxy.jpg"))
Label(window,image=img).place(x = 0, y = 0)

e = Entry(window, fg="black", bg="ivory3", font="Comic 18", width=20, borderwidth= 2)
e.pack(side= TOP, anchor= NW, padx= 15, pady= 20)

meaning = Label(window, text = "Meaning of the word will appear here", wraplength = 400, fg = "white", bg = "black", font = "Helvetica 17", justify = "left", width= 45, height= 14)
meaning.pack(side= LEFT, anchor= NW, padx= 15, pady= 20)

imgTag = HTMLLabel(window, html = "<h2>The image of the word will appear here!</h2>")
imgTag.pack()

def click():
    word = e.get().strip()
    e.delete(0,END)
    global meaning
    global imgTag

    if word == "":
        meaning.config(text= "Please enter a word!")

    else:
        
        try:
            dict = PyDictionary()
            ansDict = dict.meaning(word)
            print(ansDict, "\n\n")
            ans = "Noun:\n1) " + str(ansDict["Noun"][0]) + "."

            if len(ansDict["Noun"]) > 1:
                ans += "\n2) " + str(ansDict["Noun"][1]) + "."
            if "Verb" in ansDict:
                ans += "\n\nVerb:\n" + str(ansDict["Verb"][0]) + "."
            print(ans, "\n\n")
            meaning.config(text = ans)

            try:
                imgBaseUrl = F"https://api.unsplash.com/search/photos?query={word}&client_id=Evn8ALswgo93-PUHSwAOyD08lOFDyKX-I50TUbuCin0"

                imgData = requests.get(imgBaseUrl).json()
                
                imgLink = imgData["results"][0]["urls"]["small"]

                html = F'''<img src="{imgLink}" alt="Image of {word}" width = 300 height = 320>'''
                imgTag.pack_forget()

                imgTag = HTMLLabel(window, html = html)
                imgTag.pack(fill = "both", expand = True)
            
            except:
                imgTag.pack_forget()
                imgTag = HTMLLabel(window, html = "<h2>The image of the word you searched for can't be displayed :( </h2>")




        except:
            meaning.config(text= "There was an error! Please make sure that the spelling is correct and you're connected to the internet!")
            imgTag.pack_forget()
            imgTag = HTMLLabel(window, html = "<h2>The image of the word you searched for can't be displayed :( </h2>")


search = ImageTk.PhotoImage(Image.open("searchIcon.jpg"))
Button(window, image = search, command = click).place(x= 290, y= 21)


window.bind("<Return>",lambda event=None: click() )


window.mainloop()
