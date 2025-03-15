import os
import threading
import pygame
from tkinter import filedialog
from mutagen.mp3 import MP3
from .gui import GUI

class MP3PlayerApp(GUI):
    def __init__(self, root):
        super().__init__(root)  # Передаємо root до батьківського класу
        self.track_list = []
        self.current_track = 0
        self.is_playing = False
        self.is_paused = False
        self.is_looping = False

        # Ініціалізація pygame.mixer
        pygame.mixer.init()

        self.prev_button.configure(command=self.prev_track)
        self.play_button.configure(command=self.play_music)
        self.pause_button.configure(command=self.pause_music)
        self.next_button.configure(command=self.next_track)
        self.loop_button.configure(command=self.toggle_loop)
        self.load_button.configure(command=self.load_music)
        self.volume_slider.configure(command=self.set_volume)

    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        self.track_list.extend(files)
        if files:
            self.current_track = 0
            self.display_track_info()
            self.update_track_list()

    def update_track_list(self):
        self.track_listbox.delete("1.0", "end")
        for index, track in enumerate(self.track_list):
            if index == self.current_track:
                self.track_listbox.insert("end", f"▶ {index + 1}. {os.path.basename(track)}\n")
            else:
                self.track_listbox.insert("end", f"  {index + 1}. {os.path.basename(track)}\n")

    def display_track_info(self):
        track = self.track_list[self.current_track]
        self.track_label.configure(text=os.path.basename(track))
        self.load_cover_art()
        self.update_track_list()

    def load_cover_art(self):
        track = self.track_list[self.current_track]
        cover_path = track.replace('.mp3', '.png')
        self.set_cover_image(cover_path)

    def play_music(self):
        if not self.track_list:
            return

        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            track = self.track_list[self.current_track]
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()

        self.is_playing = True
        threading.Thread(target=self.update_time_display, daemon=True).start()

    def pause_music(self):
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True

    def prev_track(self):
        if not self.track_list:
            return
        self.current_track = (self.current_track - 1) % len(self.track_list)
        self.display_track_info()
        self.play_music()

    def next_track(self):
        if not self.track_list:
            return
        self.current_track = (self.current_track + 1) % len(self.track_list)
        self.display_track_info()
        self.play_music()

    def toggle_loop(self):
        self.is_looping = not self.is_looping
        self.loop_button.configure(text="Loop On" if self.is_looping else "Loop Off")

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))