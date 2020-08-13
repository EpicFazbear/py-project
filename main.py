from tkinter import *
import pygame
import os

Player = pygame.mixer_music


class MusicPlayer:
    def __init__(self, root):
        # Initialize Variables + Functions
        self.root = root
        self.root.title("Totally not a WINAMP clone")
        self.root.geometry("500x410+200+200")
        self.track = StringVar()
        self.status = StringVar()
        self.last_pos = DoubleVar()
        pygame.init()
        pygame.mixer.init()

        # GUI stuff
        # Track Frames
        # Todo: Add time stamps

        track_frame = LabelFrame(
            self.root,
            text="Current Track",
            font=("times new roman", 15, "bold"),
            bg="navy blue",
            fg="white",
            bd=5,
            relief=FLAT
        )

        track_frame.place(
            x=0,
            y=0,
            width=500,
            height=110
        )

        track_name = Label(
            track_frame,
            textvariable=self.track,
            font=("comic sans ms", 15, "bold"),
            bg="light grey",
            fg="navy blue",
            width=30
        ).grid(row=0, column=0, padx=10, pady=5)

        track_status = Label(
            track_frame,
            textvariable=self.status,
            font=("comic sans ms", 15, "bold"),
            bg="light grey",
            fg="navy blue",
            width=30
        ).grid(row=1, column=0, padx=10, pady=5)

        # Playlist Frame

        songs_frame = LabelFrame(
            self.root,
            text="Song Playlist",
            font=("times new roman", 15, "bold"),
            bg="navy blue",
            fg="white",
            bd=5,
            relief=FLAT,
            padx=5,
            pady=5
        )

        songs_frame.place(
            x=0,
            y=110,
            width=500,
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
            font=("arial", 15),
            bg="light grey",
            fg="navy blue",
            relief=FLAT
        )

        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # Control Buttons

        button_frame = LabelFrame(
            self.root,
            bg="navy blue",
            bd=5,
            relief=FLAT
        )

        button_frame.place(
            x=0,
            y=310,
            width=500,
            height=100
        )

        play_button = Button(
            button_frame,
            text="Play",
            font=("times new roman", 15, "bold"),
            bg="light grey",
            fg="navy blue",
            width=6,
            height=1,
            command=self.play
        ).grid(row=0, column=0, padx=5, pady=3)

        pause_button = Button(
            button_frame,
            text="Pause",
            font=("times new roman", 15, "bold"),
            bg="light grey",
            fg="navy blue",
            width=6,
            height=1,
            command=self.pause
        ).grid(row=0, column=1, padx=5, pady=3)

        resume_button = Button(
            button_frame,
            text="Resume",
            font=("times new roman", 15, "bold"),
            bg="light grey",
            fg="navy blue",
            width=6,
            height=1,
            command=self.resume
        ).grid(row=0, column=2, padx=5, pady=3)

        stop_button = Button(
            button_frame,
            text="Stop",
            font=("times new roman", 15, "bold"),
            bg="light grey",
            fg="navy blue",
            width=6,
            height=1,
            command=self.stop
        ).grid(row=0, column=3, padx=5, pady=3)

        rewind_button = Button(
            button_frame,
            text="Rewind",
            font=("times new roman", 15, "bold"),
            bg="light grey",
            fg="navy blue",
            width=6,
            height=1,
            command=self.rewind
        ).grid(row=0, column=4, padx=5, pady=3)

        # Load the songs
        os.chdir("ogg")
        # Insert the songs into playlist
        for track in os.listdir():
            self.playlist.insert(END, track)

    # Define the music functions

    def play(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("Playing")
        Player.load(self.playlist.get(ACTIVE))
        Player.play()

    def pause(self):
        self.status.set("Paused")
        self.last_pos = Player.get_pos()
        Player.stop()

    def resume(self):
        self.status.set("Playing")
        Player.play(0, self.last_pos)

    def stop(self):
        self.status.set("Stopped")
        self.last_pos = DoubleVar()
        Player.pause()

    def rewind(self):
        self.status.set("Rewinding")
        Player.rewind()
        self.status.set("Playing")


# Start TK and run the application
Tkinter = Tk()
App = MusicPlayer(Tkinter)
mainloop()
