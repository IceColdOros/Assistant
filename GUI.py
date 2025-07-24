import customtkinter as ctk
import keyboard 
import threading

#global window
app = None 

#tk appearence settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def hotkeyListener():
    keyboard.add_hotkey('F12', show_Window)
    keyboard.wait('') #block thread so it keeps listening

def show_Window():
    global app
    if app is not None and app.winfo_exists():
        return #already open
    
    #window settings
    app = ctk.CTk() #initialize app
    app.title("Crash") #name
    app.geometry("500x250") #size
    app.attributes('-topmost', True) #always on top
    app.attributes('-alpha', 0.9) #transparency
    app.configure(fg="1e1e1e") #foreground color
    app.configure(bg='black') #background color

    #close on escape
    app.bind("<Escape>", lambda e: app.destroy())

    #text input
    entry = ctk.CTkEntry(app, width=400, height=40, placeholder_text="Enter your text here")
    entry.pack(pady=20)

    #send button
    send_button = ctk.CTkButton(app, text="Send", command=lambda: print("Send:", entry.get()))
    send_button.pack()

    #voice toggle button
    mic_btn = ctk.CTkButton(app, text="Voice", command=lambda: print("Voice toggled"))
    mic_btn.pack(pady=10)

    app.mainloop() #start the app

threading.Thread(target=hotkeyListener, daemon=True).start() #start the hotkey listener thread

print("Hotkey listener started. Press F12 to show the window.")
keyboard.wait('esc') #wait for escape key to exit the program