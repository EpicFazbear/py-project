from tkinter import *
import pygame
import os

Player = pygame.mixer_music


class MusicPlayer:
    def __init__(self, root):
        # Initialize Variables + Functions
        self.root = root
        self.root.title("Totally not a WINAMP clone")
        self.root.geometry("1000x200+200+200")
        self.track = StringVar()
        self.status = StringVar()
        pygame.init()
        pygame.mixer.init()

        # GUI stuff
        songs_frame = LabelFrame(
            self.root,
            text="Song Playlist",
            font=("comic sans", 15, "bold"),
            bg="blue",
            fg="black",
            bd=5,
            relief=FLAT,
            padx=5,
            pady=5
        )

        songs_frame.place(
            x=600,
            y=0,
            width=400,
            height=200
        )

        scrollbar = Scrollbar(
            songs_frame,
            orient=VERTICAL
        )

        self.playlist = Listbox(
            songs_frame,
            yscrollcommand=scrollbar.set,
            selectbackground="dark grey",
            selectmode=SINGLE,
            font=("comic sans", 15, "bold"),
            bg="cyan",
            fg="navy blue",
            bd=5,
            relief=FLAT
        )

        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # Todo: Add buttons: Play, Pause, Stop, Unpause, Rewind

        track_frame = LabelFrame(
            self.root,
            text="track",
            font=("comic sans", 15, "bold"),
            bg="blue",
            fg="black",
            bd=5,
            relief=FLAT
        )

        track_frame.place(
            x=0,
            y=0,
            width=600,
            height=100
        )

        oggs = Label(
            track_frame,
            textvariable=self.track,
            width=20,
            font=("comic sans", 15, "bold"),
            bg="cyan",
            fg="black"
        ).grid(row=0, column=0, padx=10, pady=5)

        track_status = Label(
            track_frame,
            textvariable=self.status,
            width=20,
            font=("comic sans", 15, "bold"),
            bg="cyan",
            fg="black"
        ).grid(row=1, column=0, padx=10, pady=5)

        # Load the songs
        os.chdir("ogg")
        oggs = os.listdir()
        # self.playlist = list()
        # Insert the songs into playlist
        for track in oggs:
            self.playlist.insert(END, track)
            # self.playlist.append(track)

    # Display status play/paused/stopped = 0=stopped, 1=playing, 2=paused

    def play(self):
        self.track.set(self.playlist)
        self.status.set("(Playing)")
        Player.load(self.playlist[ACTIVE])
        Player.play()

    def stop(self):
        self.status.set("(Stopped)")
        Player.pause()

    def pause(self):
        self.status.set("(Paused)")
        Player.stop()

    def resume(self):
        self.status.set("(Playing)")
        Player.unpause()

    def rewind(self):
        self.status.set("(Rewinding)")
        Player.rewind()
        self.status.set("(Playing)")

    # Add time stamps


# Start TK and run the application
Tkinter = Tk()
App = MusicPlayer(Tkinter)
mainloop()
