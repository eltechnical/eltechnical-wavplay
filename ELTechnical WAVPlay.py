import tkinter as tk
from tkinter import filedialog
import winsound

class ELTechnicalWAVPlay:
    def __init__(self, root):
        self.root = root
        self.root.title("ELTechnical WAVPlay")
        self.root.geometry("380x200")
        self.root.configure(bg="#202020")

        self.current_file = None
        self.is_playing = False

        # Label to show status
        self.label = tk.Label(root, text="🎧 No song loaded", bg="#202020", fg="#ffffff", font=("Segoe UI", 11))
        self.label.pack(pady=15)

        # Load button
        self.load_button = tk.Button(root, text="📁 Load WAV", command=self.load_file, width=20, bg="#3a3a3a", fg="white")
        self.load_button.pack(pady=5)

        # Play button
        self.play_button = tk.Button(root, text="▶️ Play", command=self.play, width=10, bg="#00a86b", fg="white")
        self.play_button.pack(pady=5)

        # Info label for closing
        self.stop_label = tk.Label(root, text="(Close the app to stop)", bg="#202020", fg="#888888", font=("Segoe UI", 8))
        self.stop_label.pack(pady=10)

        # Gracefully handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_file(self):
        """Load a WAV file for playback"""
        self.current_file = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if self.current_file:
            self.label.config(text="Loaded: " + self.current_file.split("/")[-1])

    def play(self):
        """Play the loaded WAV file"""
        if self.current_file:
            if not self.is_playing:
                self.is_playing = True
                self.play_button.config(text="▶️ Playing")
                self._play_audio()

    def _play_audio(self):
        """Handle audio playback using winsound (without blocking UI)"""
        try:
            winsound.PlaySound(self.current_file, winsound.SND_FILENAME)
            self.is_playing = False  # Mark the audio as not playing after it's done
            self.play_button.config(text="▶️ Play")  # Reset the button text after playback
        except Exception as e:
            print(f"Error playing audio: {e}")
            self.is_playing = False
            self.play_button.config(text="▶️ Play")

    def on_close(self):
        """Handle the window close event"""
        if self.is_playing:
            # Stop the current sound playing before closing
            winsound.PlaySound(None, winsound.SND_PURGE)
        self.root.destroy()  # Close the program window

# Create the main application window
root = tk.Tk()
app = ELTechnicalWAVPlay(root)
root.mainloop()
