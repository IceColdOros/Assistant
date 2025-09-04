# GUI
import customtkinter as ctk

# Keyboard
import keyboard 
import threading

# Local LLM
import requests
import json

# Volume Control
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER


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
    app.geometry("1100x600") # window size
    app.attributes('-topmost', True) # keep on top
    app.attributes('-alpha', 1) #transparency
    app.configure(fg_color="#1e1e1e")  # correct way in customtkinter
    app.configure(bg='black')  # not really needed with fg_color, but okay

    app.bind("<Escape>", lambda e: app.destroy())


    input_frame = ctk.CTkFrame(app, fg_color="transparent")
    input_frame.pack(side="bottom", fill="x", pady=10, padx=10)

    # text input
    entry = ctk.CTkEntry(input_frame, width=300, height=40, placeholder_text="Enter your text here")
    entry.pack(side="left", padx=(0, 10))

    # send button
    def send_text():
        print("Sending to LLM...", LLM())
        entry.delete(0, 'end')

    def LLM():
        #base url from ollama (cmd>ollama serve)
        url = "http://127.0.0.1:11434/api/chat"
        #we just use above to chat, can use different opperations (add,remove, etc.)

        x = entry.get() #input prompt for the model

        #input prompt for the model
        payload = {
            "model": "deepseek-r1", #modle i want to speak to 
            "messages": [{
                "role": "user",
                "content": x}]
        }

        #send HTTP POST request to the model, with streaming enabled
        response = requests.post(url, json=payload, stream=True) #stream graps responses as it is typed

        #check response status
        if response.status_code == 200:
            print("streaming Ollama response: ") 
            for line in response.iter_lines(decode_unicode=True):
                if line: #ignore empty lines
                    try:
                        #parse each line as a JSON object
                        json_data = json.loads(line)
                        #print the content of the response
                        if "message" in json_data and "content" in json_data["message"]:
                            print(json_data["message"]["content"], end='', flush=True)

                    except json.JSONDecodeError:
                        print("Error decoding JSON:", line)
            print()
        else:
            print("Error:", response.status_code)
            print(response.text)  # Print the error message if available
        

    send_button = ctk.CTkButton(input_frame, text="Send", width=60, command=send_text)
    send_button.pack(side="left", padx=(0, 10))

    # voice toggle button
    mic_btn = ctk.CTkButton(input_frame, text="voice", width=60, command=lambda: print("Voice toggled"))
    mic_btn.pack(side="left", padx=(0, 10))

    app.mainloop()




def setAppVolume(app_name, volume_level):
# Sets volume of specific application
    
    #args:
    #app_name (str): Name of application
    #volume_level (float): Desired volume 0.0 to 1.0

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == app_name:
            volume = session.SimpleAudioVolume
            # Gets the ISimpleAudioVolume interface fro sessions

            volume_interface = cast(session.SimpleAudioVolume, POINTER(ISimpleAudioVolume))
            volume_interface.SetMasterVolume(volume_level, None)
            print(f"Volume for {app_name} set to {volume_level * 100}%")
            return
    print(f"Application '{app_name}' not found.")

def textGenerate(self, prompt):
    # Generate text using the model
    pass

def voiceGenerate(self, prompt):
    # Generate voice output using the model
    pass

#figure out how to let model save previous conversations

class Calander():
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events

    def clear_events(self):
        self.events.clear()

    #add DB so event can be saved and loaded



# start hotkey listener
threading.Thread(target=hotkeyListener, daemon=True).start()

print("Hotkey listener started. Press F12 to show the window.")
keyboard.wait('esc')  # wait for escape to exit



