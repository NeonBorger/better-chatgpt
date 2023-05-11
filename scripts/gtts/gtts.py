import openai
from gtts import gTTS
import os
api_key_path = "../../api_key.txt"
with open(api_key_path, 'r') as file:
    api_key = file.read().strip()

model_engine = "text-davinci-003"
openai.api_key = api_key

def GPT(query):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=query,
        max_tokens=2048,
        temperature=0.3,
    )
    return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

exit_words = ("q", "Q", "quit", "QUIT", "EXIT")

try:
    while True:
        print("Type q, Q, quit, QUIT, or EXIT and press Enter to end the chat session")
        query = input("What is your question?> ")
        if query in exit_words:
            print("ENDING CHAT")
            break
        else:
            (res, usage) = GPT(query)
            print(res)
            gttsFile = gTTS(text=res, lang='en', slow=False)
            gttsFile.save("gtts.mp3")
            os.system("mpg321 -q gtts.mp3")
            print("=" * 20)
            print("You have used %s tokens on this query" % usage)
            print("=" * 20)

except KeyboardInterrupt:
    exitSpeech = "Exiting Program"
    gttsFile = gTTS(text="Exiting Program.", lang='en', slow=False)
    gttsFile.save("gtts.mp3")
    os.system("mpg321 -q gtts.mp3")
    print("\nExited Better ChatGPT with gTTS.")
