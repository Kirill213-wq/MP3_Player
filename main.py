from player.player import MP3PlayerApp
import customtkinter as ctk

if __name__ == "__main__":
    root = ctk.CTk()  # Створюємо кореневе вікно
    app = MP3PlayerApp(root)  # Передаємо кореневе вікно в MP3PlayerApp
    root.mainloop()