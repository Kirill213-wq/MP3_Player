# import customtkinter as ctk
# from PIL import Image
# import os

# class GUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Spotify-Style MP3 Player")
#         self.root.geometry("454x570")

#         self.track_label = ctk.CTkLabel(self.root, text="Choose a song", font=("Arial", 20))
#         self.track_label.pack(pady=10)

#         # Місце для обкладинки треку
#         self.cover_image = ctk.CTkLabel(self.root, text="[Cover Art]", width=200, height=200)
#         self.cover_image.pack(pady=10)

#         # Список треків
#         self.track_listbox = ctk.CTkTextbox(self.root, width=400, height=180)
#         self.track_listbox.pack(pady=10)

#         # Кнопки управління
#         button_frame = ctk.CTkFrame(self.root)
#         button_frame.pack(pady=5)

#         self.prev_button = ctk.CTkButton(button_frame, text="⏮", width=40)
#         self.prev_button.grid(row=0, column=0, padx=2)

#         self.play_button = ctk.CTkButton(button_frame, text="▶", width=40)
#         self.play_button.grid(row=0, column=1, padx=2)

#         self.pause_button = ctk.CTkButton(button_frame, text="⏸", width=40)
#         self.pause_button.grid(row=0, column=2, padx=2)

#         self.next_button = ctk.CTkButton(button_frame, text="⏭", width=40)
#         self.next_button.grid(row=0, column=3, padx=2)

#         self.loop_button = ctk.CTkButton(button_frame, text="Loop", width=40)
#         self.loop_button.grid(row=0, column=4, padx=2)

#         # Кнопка для завантаження музики
#         self.load_button = ctk.CTkButton(self.root, text="+", width=100, height=30)
#         self.load_button.pack(pady=5)

#         # Регулювання гучності
#         self.volume_slider = ctk.CTkSlider(self.root, from_=0, to=1)
#         self.volume_slider.set(0.5)
#         self.volume_slider.pack(pady=5)

#         # Відображення часу треку
#         self.time_label = ctk.CTkLabel(self.root, text="00:00 / 00:00", font=("Arial", 16))
#         self.time_label.pack(pady=5)

#     def set_cover_image(self, image_path):
#         """Оновлення обкладинки треку"""
#         if image_path and os.path.exists(image_path):
#             image = Image.open(image_path)
#             image = image.resize((200, 200), Image.ANTIALIAS)
#             ctk_image = ctk.CTkImage(light_image=image, size=(200, 200))
#             self.cover_image.configure(image=ctk_image, text="")
#         else:
#             self.cover_image.configure(image=None, text="[No Cover]")

import customtkinter as ctk
from PIL import Image
import os

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify-Style MP3 Player")
        self.root.geometry("454x640")

        self.track_label = ctk.CTkLabel(self.root, text="Choose a song", font=("Arial", 20))
        self.track_label.pack(pady=10)

        # Місце для обкладинки треку
        self.cover_image = ctk.CTkLabel(self.root, text="[Cover Art]", width=200, height=200)
        self.cover_image.pack(pady=10)

        # Список треків
        self.track_listbox = ctk.CTkTextbox(self.root, width=400, height=180)
        self.track_listbox.pack(pady=10)

        # Кнопки управління
        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=5)

        self.prev_button = ctk.CTkButton(button_frame, text="⏮", width=40)
        self.prev_button.grid(row=0, column=0, padx=2)

        self.play_button = ctk.CTkButton(button_frame, text="▶", width=40)
        self.play_button.grid(row=0, column=1, padx=2)

        self.pause_button = ctk.CTkButton(button_frame, text="⏸", width=40)
        self.pause_button.grid(row=0, column=2, padx=2)

        self.next_button = ctk.CTkButton(button_frame, text="⏭", width=40)
        self.next_button.grid(row=0, column=3, padx=2)

        self.loop_button = ctk.CTkButton(button_frame, text="Loop", width=40)
        self.loop_button.grid(row=0, column=4, padx=2)

        # Кнопка для завантаження музики
        self.load_button = ctk.CTkButton(self.root, text="Load Music", width=100, height=30)
        self.load_button.pack(pady=5)

        # Кнопка для видалення пісні
        self.delete_button = ctk.CTkButton(self.root, text="Delete Song", width=100, height=30)
        self.delete_button.pack(pady=5)

        # Регулювання гучності
        self.volume_slider = ctk.CTkSlider(self.root, from_=0, to=1)
        self.volume_slider.set(0.5)
        self.volume_slider.pack(pady=5)

        # Відображення часу треку
        self.time_label = ctk.CTkLabel(self.root, text="00:00 / 00:00", font=("Arial", 16))
        self.time_label.pack(pady=5)

    def set_cover_image(self, image_path):
        """Оновлення обкладинки треку"""
        if image_path and os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.ANTIALIAS)
            ctk_image = ctk.CTkImage(light_image=image, size=(200, 200))
            self.cover_image.configure(image=ctk_image, text="")
        else:
            self.cover_image.configure(image=None, text="[No Cover]")