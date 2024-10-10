from tkinter import *
from PIL import ImageTk
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

eng=pyttsx3.init()

voice=eng.getProperty('voices')
eng.setProperty('voice',voice[1].id)

#get_close_matches(word,possibilities,n,cutoff)
#close_match=get_close_matches('appel',['ape','apple','app'],n=3,cutoff=0.7)
#print(close_match)

##function part
def search():
    data=json.load(open('data.json'))
    word=enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        meaningEntry.delete(0,END)
        for item in meaning:
            meaningEntry.insert(END,u''+item+'\n')

    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        print(close_match)
        res=messagebox.askyesno('confirm',f'Did you mean {close_match} instead ?')

        if res==True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)
            meaning=data[close_match]
            meaningEntry.delete(0,END)
            for item in meaning:
                meaningEntry.insert(END,u'\u2022'+item+'\n\n')
        else:
            messagebox.showerror('Error','The word doesnt exist,Please double check it.')
            enterwordEntry.delete(0, END)
            meaningEntry.delete(0, END)
    else:
            messagebox.showinfo('information','The word doesnt exist')
            enterwordEntry.delete(0,END)
            meaningEntry.delete(0,END)

def clear():
    enterwordEntry.delete(0,END)
    meaningEntry.delete(0,END)

def iexit():
    ques=messagebox.askyesno('comfirm','Do you want to exit ?')
    if ques==True:
        root.destroy()

    else:
        pass

def wordaudio():
    eng.say(enterwordEntry.get())
    eng.runAndWait()

def meanaudio():
    eng.say(meaningEntry.get())
    eng.runAndWait()


##GUI part

root=Tk()

root.geometry('1279x854+100+20')

root.title('Fun dictionary created by Priya')

root.resizable(False,False)

bgimage=ImageTk.PhotoImage(file='C:/Users/PRIYA/PycharmProjects/Talking Dictionary/pythonProject1/bgmi.jpg')
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=0,y=0)

enterwordlabel=Label(root,text='Enter word',font=('cambria',30))
enterwordlabel.place(x=750,y=40)

enterwordEntry=Entry(root,font=('arial',20,'bold'),justify=CENTER,bd=8,relief=GROOVE)
enterwordEntry.place(x=700,y=120)

searchimage=ImageTk.PhotoImage(file='C:/Users/PRIYA/PycharmProjects/Talking Dictionary/pythonProject1/search2.png')
searchButton=Button(root,image=searchimage,bd=0,bg='whitesmoke',cursor='hand2',command=search)
searchButton.place(x=760,y=200)

micimage=ImageTk.PhotoImage(file='C:/Users/PRIYA/PycharmProjects/Talking Dictionary/pythonProject1/microphone.png')
micButton=Button(root,image=micimage,bd=0,bg='whitesmoke',cursor='hand2',command=wordaudio)
micButton.place(x=900,y=200)

meaninglabel=Label(root,text='Meaning',font=('cambria',30))
meaninglabel.place(x=770,y=300)

meaningEntry=Entry(root,font=('arial',20,'bold'),justify=CENTER,bd=8,relief=GROOVE)
meaningEntry.place(x=550,y=380,width=630,height=180)

microimage=ImageTk.PhotoImage(file='C:/Users/PRIYA/PycharmProjects/Talking Dictionary/pythonProject1/mic.png')
microButton=Button(root,image=microimage,bg='whitesmoke',bd=0,cursor='hand2',command=meanaudio)
microButton.place(x=700,y=610)

crossimage=ImageTk.PhotoImage(file='C:/Users/PRIYA/PycharmProjects/Talking Dictionary/pythonProject1/cross.png')
crossButton=Button(root,image=crossimage,bd=0,bg='whitesmoke',cursor='hand2',command=clear)
crossButton.place(x=835,y=610)

exitimage=ImageTk.PhotoImage(file='C:/Users/PRIYA/PycharmProjects/Talking Dictionary/pythonProject1/exit.png')
exitButton=Button(root,image=exitimage,bd=0,bg='whitesmoke',cursor='hand2',command=iexit)
exitButton.place(x=960,y=610)

def enter_function(event):
    searchButton.invoke()

root.bind('<Return>',enter_function)

root.mainloop()