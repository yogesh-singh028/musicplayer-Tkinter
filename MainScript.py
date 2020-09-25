
from tkinter import *
from tkinter import ttk,filedialog
import pygame
import os
class MusicPlayer():
    def __init__(self,root,style):
        self.root = root
        self.style = style
        self.root.title("Music Player")
        self.root.geometry("600x350")
        #self.root.configure(cursor="dotbox gray")
        self.root.configure(bg='gray')
        # initializing pygame constructor ....
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()

        self.colors = ['pink','blue','red','green','purple','cyan','orange','yellow','gray']
        self.i = 0
        self.song_playing = False
        self.song_pause = False
        self.current_song = ''
        self.fps = 0
        self.songs = []

        #self.color_change()

        # widgets ..

        self.main_frame = Frame(self.root,bd=2,relief=GROOVE,bg='black')
        self.main_frame.place(x=10,y=10,width=580,height=280)

        self.button_frame = Frame(self.root,bd=1,bg='black')
        self.button_frame.place(x=30,y=300,width=550,height=40)

        self.playlist_frame = Frame(self.main_frame,bd=1,bg='gray')
        self.playlist_frame.place(x=250,y=5,width=320,height=220)

        # Music Label ...
        music_image = PhotoImage(file='mus.png')
        music_lbl = Label(self.main_frame,image=music_image,bd=0)
        music_lbl.image =music_image
        music_lbl.place(x=30,y=5)

        self.canvas=Canvas(self.main_frame,bg="black",width=230,height=40,bd=0,relief=RIDGE)
        self.canvas.place(x=5,y=230)

        # playlist ..
        # Inserting scrollbar
        # configure the style

        scrol_y = ttk.Scrollbar(self.playlist_frame, orient=VERTICAL)
        # Inserting Playlist listbox

        self.song_list = Listbox(self.playlist_frame,bg='black',fg='white', height=13, bd=3, font=('arial', 9),
                                 yscrollcommand=scrol_y.set,selectbackground="gray")

        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.song_list.yview)
        self.song_list.pack(fill=BOTH)

        #-------------------


        self.vol = Scale(self.main_frame, orient=HORIZONTAL, from_=0, to=100, fg='gray', bg='black', relief='flat',
                         activebackground='black', bd=0, highlightthickness=0, sliderlength=10, width=10, length=320,
                         sliderrelief=RIDGE,command=self.volume)
        self.vol.set(20)
        self.vol.place(x=250, y=230)

        #self.pg_length = ttk.Progressbar(self.main_fra)

        #adding buttons  ...
        path = os.getcwd()

        self.previous = PhotoImage(file=os.path.join(path, 'icon\\previous.png'))
        self.pre_btn = Button(self.button_frame, image=self.previous, bg='gray')
        self.pre_btn.image = self.previous
        self.pre_btn.place(x=10, y=0)


        self.play = PhotoImage(file=os.path.join(path, 'icon\\play.png'))
        self.play_btn = Button(self.button_frame, image=self.play, bg='gray',command=self.playsong)
        self.play_btn.image = self.play
        self.play_btn.place(x=50, y=0)

        self.pause = PhotoImage(file=os.path.join(path, 'icon\\pause.png'))
        self.stop= PhotoImage(file=os.path.join(path, 'icon\\stop-button.png'))

        self.stop_btn = Button(self.button_frame, image=self.stop, bg='gray',command=self.stop_song)
        self.stop_btn.image = self.stop
        self.stop_btn.place(x=90, y=0)

        self.next = PhotoImage(file=os.path.join(path, 'icon\\next.png'))
        self.next_btn = Button(self.button_frame, image=self.next, bg='gray',)
        self.next_btn.image = self.next
        self.next_btn.place(x=130, y=0)

        self.open = PhotoImage(file=os.path.join(path, 'icon\\folder.png'))
        self.open_btn = Button(self.button_frame, image=self.open, bg='gray',command=self.open)
        self.open_btn.image = self.open
        self.open_btn.place(x=170, y=0)

        self.sound = PhotoImage(file=os.path.join(path, 'icon\\speaker.png'))
        self.sound_btn = Button(self.button_frame, image=self.sound, bg='gray')
        self.sound_btn.image = self.sound
        self.sound_btn.place(x=210, y=0)


        self.close = PhotoImage(file=os.path.join(path, 'icon\\power-button.png'))
        self.close_btn = Button(self.button_frame, image=self.close, bg='gray',command=self.root.quit)
        self.close_btn.image = self.close
        self.close_btn.place(x=250, y=0)



    def open(self):
        path = filedialog.askdirectory()
        if(path):
            songss = os.listdir(path)
            for song in songss:
                if song.endswith('.mp3') or song.endswith('.wav'):
                    self.songs.append(song)
                    self.song_list.insert(END,song)

    def color_change(self):
        self.root.configure(bg=self.colors[self.i])
        if self.i >=8:
            self.i=0
        else:
            self.i += 1
        self.root.after(500,self.color_change)


    def playsong(self,song):
        self.current_song =song
        # Displaying Selected Song title
        pygame.mixer.music.load(self.current_song)
        # Playing Selected Song
        pygame.mixer.music.set_volume(0.1)
        #print(pygame.mixer.music.get_volume())
        pygame.mixer.music.play(-1)
        self.song_playing = True
        self.add_text(self.current_song)

    def stop_song(self):
        if (self.song_playing):
            pygame.mixer.music.stop()
            self.song_playing= False


    def pause_song(self):
        if(self.song_playing):
            pygame.mixer.music.pause()
            self.song_pause = True

    def unpause(self):
        if(self.song_pause):
            pygame.mixer.music.unpause()
            self.song_pause = False

    def next_song(self):
        next_song = int(self.songs.index(self.current_song))
        next_song +=1
        if(len(self.songs)<=next_song):
            next_song = 0
        self.playsong(self.songs[next_song])


    def previous_song(self):
        prev_song = int(self.songs.index(self.current_song))
        prev_song -=1
        if (prev_song < 0):
            prev_song = len(self.songs)-1
        self.playsong(self.songs[prev_song])


    def get_song(self):
        self.current_song = self.song_list.get(ACTIVE)
        self.playsong(self.current_song)


    def volume(self,val):
        pygame.mixer.music.set_volume(int(val) / 1000)

    def mute_song(self):
        pygame.mixer.music.set_volume(0)

    def un_mute(self):
        pygame.mixer.music.set_volume(self.vol.get())

    def add_text(self,song):
        text_var = song
        text = self.canvas.create_text(0, -2000, text=text_var, font=('Times New Roman', 10, 'bold'), fill='white',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = self.canvas.bbox("marquee")
        width = x2 - x1
        height = y2 - y1
        self.canvas['width'] = width
        self.canvas['height'] = height
        self.fps = 40  # Change the fps to make the animation faster/slower
        self.shift()

    def shift(self):
        x1, y1, x2, y2 = self.canvas.bbox("marquee")
        if (x2 < 0 or y1 < 0):  # reset the coordinates
            x1 = self.canvas.winfo_width()
            y1 = self.canvas.winfo_height() // 2
            self.canvas.coords("marquee", x1, y1)
        else:
            self.canvas.move("marquee", -2, 0)
        self.canvas.after(1000 // self.fps, self.shift)






root = Tk()
style = ttk.Style()
style.theme_use('alt')#clam
# opacity/tranparency applies to image and frame
#root.wm_attributes('-alpha', 0.7)
MusicPlayer(root,style)
root.mainloop()
