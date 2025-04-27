import ollama

from microphone import recognize
from tts import speak

# SYSPROMPT = """I'm a programmer. You are my rubber duck.
# Your responses should be short, concise, insightful and motivating.
# Your responses should be REALLY short. One sentence, not more than 15 words.
# You're not allowed to see the code.
# Be a good listener, give insightful hints."""

SYSPROMPT = "You are a helpful assistant. Your responses are short, not exceeding one sentence of not more than 16 words."

client = ollama.Client()
model = "llama3.2"
messages = [
    {
        "role": "system",
        "content": SYSPROMPT,
    },
]

while True:
    print("speak now.")
    messages.append({"role": "user", "content": recognize()})
    print(messages[-1]["content"])
    response = client.chat(model=model, messages=messages)
    messages.append({"role": "assistant", "content": response["message"].content})
    speak(response["message"].content)
    print(messages[-1]["content"])

