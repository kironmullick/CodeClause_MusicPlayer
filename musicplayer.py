import os
import pygame
from pygame import mixer
import tkinter as tk
from tkinter import filedialog

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("500x400")
        self.configure(background="black")  # Set background color

        self.music_folder = ""
        self.music_files = []
        self.current_index = 0

        self.mixer = mixer
        self.mixer.init()
        self.mixer.music.set_volume(0.5)

        self.play_button = tk.Button(self, text="Play", command=self.play_music, width=10, height=2)
        self.pause_button = tk.Button(self, text="Pause", command=self.pause_music, width=10, height=2)
        self.next_button = tk.Button(self, text="Next", command=self.next_music, width=10, height=2)
        self.previous_button = tk.Button(self, text="Previous", command=self.previous_music, width=10, height=2)
        self.shuffle_button = tk.Button(self, text="Shuffle", command=self.shuffle_music, width=10, height=2)
        self.repeat_button = tk.Button(self, text="Repeat", command=self.repeat_music, width=10, height=2)
        self.music_label = tk.Label(self, text="", bg="black", fg="white", font=("Helvetica", 14, "bold"))
        self.current_song_label = tk.Label(self, text="", bg="black", fg="white", font=("Helvetica", 12))
        self.song_listbox = tk.Listbox(self, selectbackground="gray", selectforeground="white", bg="black", fg="white", font=("Helvetica", 12))
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)

        self.play_button.pack(pady=10)
        self.pause_button.pack(pady=5)
        self.next_button.pack(pady=5)
        self.previous_button.pack(pady=5)
        self.shuffle_button.pack(pady=5)
        self.repeat_button.pack(pady=5)
        self.music_label.pack(pady=10)
        self.current_song_label.pack(pady=5)
        self.song_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.song_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.song_listbox.yview)

        self.select_music_folder()

    def select_music_folder(self):
        self.music_folder = filedialog.askdirectory()
        self.load_music_files()

    def load_music_files(self):
        self.music_files = [file for file in os.listdir(self.music_folder) if file.endswith('.mp3')]
        if not self.music_files:
            self.music_label.configure(text="No music files found in the folder.")
            return
        self.music_label.configure(text="Music files loaded.")
        self.update_song_listbox()

    def update_song_listbox(self):
        self.song_listbox.delete(0, tk.END)
        for i, song in enumerate(self.music_files, start=1):
            self.song_listbox.insert(tk.END, f"{i}. {song}")

    def play_music(self):
        if self.mixer.music.get_busy():
            self.mixer.music.unpause()
        else:
            self.load_current_music()
            self.mixer.music.play()
            self.music_label.configure(text="Now playing:")
            self.update_current_song_label()

    def pause_music(self):
        if self.mixer.music.get_busy():
            self.mixer.music.pause()

    def next_music(self):
        self.current_index = (self.current_index + 1) % len(self.music_files)
        self.play_music()

    def previous_music(self):
        self.current_index = (self.current_index - 1) % len(self.music_files)
        self.play_music()

    def shuffle_music(self):
        pass

    def repeat_music(self):
        pass

    def load_current_music(self):
        current_file = self.music_files[self.current_index]
        file_path = os.path.join(self.music_folder, current_file)
        self.mixer.music.load(file_path)

    def update_current_song_label(self):
        current_song = self.music_files[self.current_index]
        self.current_song_label.configure(text=current_song)

if __name__ == "__main__":
    music_player = MusicPlayer()
    music_player.mainloop()
