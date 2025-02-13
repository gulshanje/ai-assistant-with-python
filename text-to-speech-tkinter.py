import pyttsx3
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_text():
    """Convert text to speech and play it."""
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

def save_audio():
    """Save the speech as an MP3 file."""
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                             filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        engine.save_to_file(text, file_path)
        engine.runAndWait()

def change_voice():
    """Change voice (Male/Female)."""
    voices = engine.getProperty("voices")
    selected_voice = voice_var.get()
    
    if selected_voice == "Male":
        engine.setProperty("voice", voices[0].id)
    elif selected_voice == "Female":
        engine.setProperty("voice", voices[1].id)

def change_speed(value):
    """Change speech rate."""
    engine.setProperty("rate", int(value))


root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x350")
MainFrame = tk.Frame(root, width=385, height=460, relief='raised', borderwidth=5)

title_label = tk.Label(root, text="Text-to-Speech", font=("Arial", 16, "bold"))
title_label.pack(pady=5)

text_entry = tk.Text(root, height=5, wrap=tk.WORD)
text_entry.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)


voice_var = tk.StringVar(value="Male")
voice_label = tk.Label(root, text="Select Voice:")
voice_label.pack()
voice_menu = ttk.Combobox(root, textvariable=voice_var, values=["Male", "Female"], state="readonly")
voice_menu.pack()


speed_label = tk.Label(root, text="Speed Rate:")
speed_label.pack()
speed_slider = tk.Scale(root, from_=50, to=300, orient="horizontal", command=change_speed)
speed_slider.set(150)
speed_slider.pack()


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

speak_button = tk.Button(button_frame, text="Speak", command=speak_text, bg="green", fg="white", width=10)
speak_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(button_frame, text="Save as MP3", command=save_audio, bg="blue", fg="white", width=10)
save_button.grid(row=0, column=1, padx=5)


voice_menu.bind("<<ComboboxSelected>>", lambda event: change_voice())


root.mainloop()
