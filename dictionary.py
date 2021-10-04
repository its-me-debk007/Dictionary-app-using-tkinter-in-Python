import requests
from tkinter import *
from PIL import Image,ImageTk
from tkhtmlview import HTMLLabel
from playsound import playsound
from PyDictionary import PyDictionary

window=Tk()
window.title("Dictionary")
window.iconbitmap("icon.ico")
window.configure(bg= "black")
window.geometry("920x390")
# window.resizable(False, False)

# img=ImageTk.PhotoImage(Image.open("image.jpg"))
# Label(window,image=img).pack(side= RIGHT)

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
        
        try:
            dict = PyDictionary()
            ansDict = dict.meaning(word)
            print(ansDict, "\n\n")
            ans = "Noun:\n" + ansDict["Noun"][0]
            if len(ansDict["Noun"]) > 1:
                ans += "\n" + ansDict["Noun"][1]
            if "Verb" in ansDict:
                ans = ans + "\n\nVerb:\n" + ansDict["Verb"][0]
            
            meaning.config(text = ans)
            
            imgBaseUrl = F"https://api.unsplash.com/search/photos?query={word}&client_id=Evn8ALswgo93-PUHSwAOyD08lOFDyKX-I50TUbuCin0"
            imgData = requests.get(imgBaseUrl).json()
            
            imgLink = imgData["results"][0]["urls"]["small"]
            
            print(imgLink)
            html = F'''<img src="{imgLink}" alt="Image of {word}" width = 300 height = 300>'''

            imgTag = HTMLLabel(window, html = html)            
            imgTag.pack(fill = "both", expand = True)
            

            data = requests.get(base_url + word).json()
            sound= 'https:' + data[0]["phonetics"][0]["audio"]
            playsound(sound)
            print(sound)

        except:
            meaning.config(text= "There was an error! Please make sure that the spelling is correct and you're connected to the internet!")

search = ImageTk.PhotoImage(Image.open("searchIcon.jpg"))
Button(window, image = search, command = click).place(x= 290, y= 21)


window.bind("<Return>",lambda event=None: click() )



window.mainloop()
