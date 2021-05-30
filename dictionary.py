import requests
from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title("Dictionary")
window.geometry("1066x600")
load=Image.open("im.jpg")
img=ImageTk.PhotoImage(load)
Label(window,image=img).place(x=0,y=0)
txt=Entry(window,fg="white",bg="grey",font=("Comic",20),width=20)
txt.place(x=379,y=10)
c=0

def clicked():
    global c,l1,l2,l3
    if c==1:
        l1.destroy()
        l2.destroy()
        l3.destroy()
    API="3e38a4e20f4a7b563cbe3736a5e91e95"
    base_url="https://od-api.oxforddictionaries.com/api/v2/"
    app_id="7c5cca17"
    language_code="en-us"
    endpoint="entries"
    word=txt.get().lower()
    txt.delete(0,'end')
    url=base_url+endpoint+"/"+language_code+"/"+word
    try:
        content=requests.get(url,headers={"app_id":app_id,"app_key":API}).json()
        l1=Label(window,text=f"TYPE OF WORD: {content['results'][0]['lexicalEntries'][0]['lexicalCategory']['id']}",font=("Arial",18),bg="black",fg="White")
        l1.place(x=10,y=175)
        s=content['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        if len(s)>92:
            
            for i in range(93,len(s)):
                if i==" ":
                    k=i
                    break
            s2=s[k::]
            s1=s[:k:]
            s=s1+"\n"+s2
        l2=Label(window,text=f"PROPER DEFINITION:\n\n{s}",fg="white",bg="black",font=("Arial",18))
        l2.place(x=10,y=230)
        l3=Label(window,text=f"SHORT DEFINITION:\n\n{content['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'][0]}",bg="black",fg="white",font=("Arial",18))
        l3.place(x=10,y=350)
        c=1
    except:
        Label(window,text="There was an error in searching for the word :\nPlease try searching for another word",font=("Arial",18),fg="white",bg="black").place(x=2,y=175)

Button(window,text="Search for meaning",font=("Arial",14),command=clicked,fg="black",bg="grey").pack(side="bottom")

window.mainloop



