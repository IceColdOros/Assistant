import ollama

client = ollama.Client()

model = "deepseek-r1"
promt = input("Enter your prompt: ")

response = client.generate(model=model, prompt=promt)

print("Response:", response.response)
