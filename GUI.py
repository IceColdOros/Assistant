import customtkinter as ctk
import keyboard 
import threading

# global window
app = None 

# tk appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def hotkeyListener():
    keyboard.add_hotkey('F12', show_Window)
    keyboard.wait('')  # block thread so it keeps listening

def show_Window():
    global app
    if app is not None and app.winfo_exists():
        return  # already open

    # window settings
    app = ctk.CTk()
    app.title("Crash") #app title
    app.geometry("500x250") # window size
    app.attributes('-topmost', True) # keep on top
    app.attributes('-alpha', 1) #transparency
    app.configure(fg_color="#1e1e1e")  # correct way in customtkinter
    app.configure(bg='black')  # not really needed with fg_color, but okay

    app.bind("<Escape>", lambda e: app.destroy())

    # BOTTOM FRAME for input and buttons
    input_frame = ctk.CTkFrame(app, fg_color="transparent")
    input_frame.pack(side="bottom", fill="x", pady=10, padx=10)

    # text input
    entry = ctk.CTkEntry(input_frame, width=300, height=40, placeholder_text="Enter your text here")
    entry.pack(side="left", padx=(0, 10))

    # send button
    def send_text():
        print("Send:", entry.get())
        entry.delete(0, 'end')

    send_button = ctk.CTkButton(input_frame, text="Send", width=60, command=send_text)
    send_button.pack(side="left", padx=(0, 10))

    # voice toggle button
    mic_btn = ctk.CTkButton(input_frame, text="voice", width=60, command=lambda: print("Voice toggled"))
    mic_btn.pack(side="left", padx=(0, 10))

    app.mainloop()

# start hotkey listener
threading.Thread(target=hotkeyListener, daemon=True).start()

print("Hotkey listener started. Press F12 to show the window.")
keyboard.wait('esc')  # wait for escape to exit
