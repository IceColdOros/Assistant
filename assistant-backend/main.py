#API
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

#Audio
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER


app = FastAPI()


#--------Models--------
class ChatRequest(BaseModel):
    prompt: str

class VolumeRequest(BaseModel):
    app_name: str
    volume: float #0.0 to 1.0

class CalendarEvent(BaseModel):
    event: str


def LLM(prompt: str) -> str:
    #base url from ollama (cmd>ollama serve)
    url = "http://127.0.0.1:11434/api/chat"

    #input prompt for the model
    payload = {
        "model": "deepseek-r1", #modle i want to speak to 
        "messages": [{
            "role": "user",
            "content": prompt}]
    }

    #send HTTP POST request to the model, with streaming enabled
    response = requests.post(url, json=payload, stream=True) #stream graps responses as it is typed
    result = ""

    #check response status
    if response.status_code == 200:
        for line in response.iter_lines(decode_unicode=True):
            if line: #ignore empty lines
                try:
                    #parse each line as a JSON object
                    json_data = json.loads(line)
                    #print the content of the response
                    if "message" in json_data and "content" in json_data["message"]:
                        result += json_data["message"]["content"]

                except json.JSONDecodeError:
                    pass
    else:
        return f"Error: {response.status_code} - {response.text}"
    
    return result.strip()


#API endpoint for chat
@app.post("/chat")
def chat(request: ChatRequest):
    reply = LLM(request.prompt)
    return {"response": reply}


#--------Volume Control--------
def setAppVolume(app_name: str, volume_level: float):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == app_name:
            volume_interface = cast(session.SimpleAudioVolume, POINTER(ISimpleAudioVolume))
            volume_interface.SetMasterVolume(volume_level, None)
            return f"Volume for {app_name} set to {volume_level * 100}%"
    return f"Application '{app_name}' not found."


@app.post("/set-volume")
def set_volume(request: VolumeRequest):
    msg = setAppVolume(request.app_name, request.volume)
    return {"message": msg}


#--------Calandar--------
class Calender():
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events

    def clear_events(self):
        self.events.clear()

calender = Calender()

@app.post("/calendar/add")
def add_event(event: CalendarEvent):
    calender.add_event(event.event)
    return {"events": calender.get_events()}

@app.get("/calendar")
def get_events():
    return {"events": calender.get_events()}

@app.post("/calendar/clear")
def clear_events():
    return {"events": []}
