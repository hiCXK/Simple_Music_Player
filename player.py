from tkinter import *
from tkinter import filedialog
from PIL import *
import pygame
import os


window=Tk()        #Tk returns a widget on screen
window.title("Your Walkman :)") #title of the widget 
window.geometry("500x350")  #size of the widget

pygame.mixer.init() 
songlist=Listbox(window,background="black",foreground="white",width=100,height=18)
songlist.pack()     #adds songlist widget in window widget


songs=[]
current_song=''
paused=False



def loading_music():
    global current_song
    window.directory=filedialog.askdirectory()
    for song in os.listdir(window.directory):
        name,ext=os.path.splitext(song)
        if ext==".mp3":
            songs.append(song)
    for song in songs:
        songlist.insert("end",song)
    songlist.select_set(0)
    current_song=songs[songlist.curselection()[0]]

def play_m():
    global current_song,paused
    if not paused:
        pygame.mixer.music.load(os.path.join(window.directory,current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False
        
def pause_m():
    global paused
    pygame.mixer.music.pause()
    paused=True
    
def next_m():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song=songs[songlist.curselection()[0]]
        play_m()
    except:
        pass

def prev_m():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)-1)             #here, '-' is used
        current_song=songs[songlist.curselection()[0]]
        play_m()
    except:
        pass
def rewind_m():
    pygame.mixer.music.rewind()

def vol_up():
    x=pygame.mixer.music.get_volume()+0.2
    pygame.mixer.music.set_volume(x)
    
def vol_down():
    y=pygame.mixer.music.get_volume()-0.2
    pygame.mixer.music.set_volume(y)





menu_bar=Menu(window)
window.config(menu=menu_bar)

org_menu=Menu(menu_bar,tearoff=False)
org_menu.add_command(label="Select Folder",command=loading_music)
menu_bar.add_cascade(label="Find Music",menu=org_menu)

play_bt_img=PhotoImage(file="play2.png",)
pause_bt_img=PhotoImage(file="pause2.png")
next_bt_img=PhotoImage(file="next2.png")
prev_bt_img=PhotoImage(file="previous2.png")
vol_up_img=PhotoImage(file="volup1.png")
vol_down_img=PhotoImage(file="voldown1.png")
rewind_img=PhotoImage(file="rewind1.png")

Cframe=Frame(window)
Cframe.pack()

play_bt=Button(Cframe,image=play_bt_img,borderwidth=3,height=50,width=50,command=play_m)
pause_bt=Button(Cframe,image=pause_bt_img,borderwidth=3,height=50,width=50,command=pause_m)
next_bt=Button(Cframe,image=next_bt_img,borderwidth=3,height=50,width=50,command=next_m)
prev_bt=Button(Cframe,image=prev_bt_img,borderwidth=3,height=50,width=50,command=prev_m)
volup_bt=Button(Cframe,image=vol_up_img,borderwidth=3,height=50,width=50,command=vol_up)
voldown_bt=Button(Cframe,image=vol_down_img,borderwidth=3,height=50,width=50,command=vol_down)
rewind_bt=Button(Cframe,image=rewind_img,borderwidth=3,height=50,width=50,command=rewind_m)


prev_bt.grid(row=0,column=0,padx=0,pady=0)
pause_bt.grid(row=0,column=1,padx=0,pady=0)
play_bt.grid(row=0,column=2,padx=0,pady=0)
next_bt.grid(row=0,column=3,padx=0,pady=0)
voldown_bt.grid(row=0,column=4,padx=0,pady=0)
volup_bt.grid(row=0,column=5,padx=0,pady=0)
rewind_bt.grid(row=0,column=6,padx=0,pady=0)


window.mainloop()  #program starts when this line runs