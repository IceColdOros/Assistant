import requests
import json

#base url from ollama (cmd>ollama serve)
url = "http://127.0.0.1:11434/api/chat"
#we just use above to chat, can use different opperations (add,remove, etc.)

#input prompt for the model
payload = {
    "model": "deepseek-r1", #modle i want to speak to 
    "messages": [{
        "role": "user",
         "content": "Hello, how are you?"}]
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

